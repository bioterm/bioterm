import locale
import os
import secrets
import subprocess
import sys
import time
from dataclasses import dataclass

import requests

from bioterm.common.core.logger import get_module_logger
from bioterm.common.utils.apt import install_package
from bioterm.common.utils.apt import is_package_installed
from bioterm.common.utils.docker import create_docker_network
from bioterm.common.utils.docker import does_docker_network_exist
from bioterm.common.utils.docker import install_docker_sources
from bioterm.common.utils.docker import is_docker_source_added
from bioterm.common.utils.env import check_existing_env_files
from bioterm.common.utils.env import write_env_file
from bioterm.common.utils.validators import validate_domain
from bioterm.common.utils.validators import validate_email

sys.path.append(
    os.path.join(os.path.dirname(__file__), "bioterm/common/services/authentik/")
)
sys.path.append(
    os.path.join(os.path.dirname(__file__), "bioterm/common/services/grafana/")
)

import authentikApiClient  # noqa: E402
from bioterm.common.services.authentikService import AuthentikService  # noqa: E402
import grafanaApiClient  # noqa: E402

# from bioterm.common.services.grafanaService import GrafanaService

logger = get_module_logger(__name__)

#  from bioterm.common.services.authentik.openapi_client.api_client import (
#     ApiClient as AuthentikApiClient,
# )
# from bioterm.common.services.authentik.openapi_client.configuration import (
#     Configuration as AuthentikConfiguration,
# )

AUTH_ENV_FILE_LOCATION = "./bioterm/server/auth/.env"
PROXY_ENV_FILE_LOCATION = "./bioterm/server/proxy/.env"
ELN_ENV_FILE_LOCATION = "./bioterm/server/eln/.env"
GRAFANA_ENV_FILE_LOCATION = "./bioterm/server/grafana/.env"
API_ENV_FILE_LOCATION = "./bioterm/server/backend/.env"
APP_ENV_FILE_LOCATION = "./bioterm/server/frontend/.env"

PACKAGES = [
    "pwgen",
    "dialog",
    "docker-ce",
    "docker-ce-cli",
    "containerd.io",
    "docker-buildx-plugin",
    "docker-compose-plugin",
]


# Define a function to check if the server is available
def is_server_available(server_url: str):
    try:
        response = requests.get(server_url, verify=False)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


@dataclass()
class UserInputsServerInstallation:
    base_domain: str
    subdomains: dict
    password: str
    email: str
    useletsencrypt: bool
    staging: str
    letsencryptemail: str
    imprint: bool


@dataclass()
class FullSubDomains:
    auth: str
    backend: str
    eln: str
    frontend: str
    grafana: str
    teleport: str


@dataclass()
class ServerSettings:
    docker_network_name: str = None
    base_domain: str = None
    domains: FullSubDomains = FullSubDomains(
        auth=None, backend=None, eln=None, frontend=None, grafana=None, teleport=None
    )
    useletsencrypt: bool = False
    admin_email: str = None
    admin_password: str = None
    authentik_apikey: str = None
    authentik_secret_key: str = None
    NGINX_PRIMARY_DOMAIN: str = None
    NGINX_PROXY_PASS: str = None
    letsencryptemail: str = ""
    letsencrypt_staging: str = "1"
    API_PUBLIC_DOMAIN: str = None
    APP_PUBLIC_DOMAIN: str = None
    AUTH_PUBLIC_DOMAIN: str = None
    ELN_PUBLIC_DOMAIN: str = None
    GRAFANA_PUBLIC_DOMAIN: str = None
    TELEPORT_PUBLIC_DOMAIN: str = None
    domains_list: str = None
    auth_pg_pass: str = None
    authentik_secret_key: str = None
    admin_password: str = None
    authentik_apikey: str = None
    authentik_authorization_flow_pk: str = None
    authentik_provider_grafana_client_id: str = None
    authentik_provider_grafana_client_secret: str = None
    authentik_provider_backend_client_id: str = None
    project_name: str = None
    BACKEND_SECRET_KEY: str = None
    BACKEND_POSTGRES_SERVER: str = None
    BACKEND_POSTGRES_DB: str = None
    BACKEND_POSTGRES_USER: str = None
    BACKEND_POSTGRES_PASSWORD: str = None
    grafana_password: str = None
    pg_password: str = None
    GF_SECURITY_ADMIN_USERNAME: str = None
    GF_SECURITY_ADMIN_PASSWORD: str = None
    GF_SERVER_DOMAIN: str = None
    GF_SERVER_ROOT_URL: str = None
    AUTHENTIK_CLIENT_ID: str = None
    AUTHENTKIK_CLIENT_SECRET: str = None
    AUTHENTIK_URL: str = None
    AUTHENTIK_ISSUER: str = None
    USE_TLS: bool = False
    authentik_public_key: str = None
    REDIS_SERVER: str = None
    REDIS_PORT: int = 6379
    imprint: bool = False


class ServerInstaller:
    def __init__(self, settings: ServerSettings):
        self.settings = settings

    def init_docker_network(self):
        logger.info("### CREATING DOCKER NETWORK ###")
        # Check if the Docker network exists
        if not does_docker_network_exist(self.settings.docker_network_name):
            create_docker_network(self.settings.docker_network_name)

    def update_hostfile(
        self, user_input: UserInputsServerInstallation, base_domain: str
    ) -> None:
        logger.info("### UPDATING HOSTFILE ###")

        run_command("sudo cp /etc/hosts /etc/hosts.old")

        def add_entry_to_hostfile(entry_to_add: str):
            # Check if the entry already exists in /etc/hosts
            command_check = f"grep -q '{entry_to_add}' /etc/hosts"
            subdomain_exists = subprocess.call(command_check, shell=True) == 0
            if not subdomain_exists:
                add_subdomain_command = (
                    f"echo '{entry_to_add}' | sudo tee -a /etc/hosts"
                )
                run_command(add_subdomain_command)

        add_entry_to_hostfile(f"172.17.0.1 {base_domain}")

        for subdomain in user_input.subdomains:
            subdomain_to_add = (
                f"172.17.0.1 {user_input.subdomains[subdomain]}.{base_domain}"
            )
            add_entry_to_hostfile(subdomain_to_add)

    def init_credentials(self):
        logger.info("### INITIALIZING CREDENTIALS ###")

        self.settings.auth_pg_pass, _ = run_command("pwgen -s 40 1")
        self.settings.authentik_secret_key, _ = run_command("pwgen -s 50 1")
        self.settings.authentik_apikey = secrets.token_urlsafe(20)

        self.settings.authentik_provider_grafana_client_id = secrets.token_hex(20)
        self.settings.authentik_provider_grafana_client_secret = secrets.token_hex(64)
        self.settings.authentik_provider_backend_client_id = secrets.token_hex(20)

        self.settings.grafana_password, _ = run_command("pwgen -s 40 1")

        self.settings.pg_password, _ = run_command("pwgen -s 40 1")

        eln_dbpw, _ = run_command("pwgen -s 31 1")
        eln_key, _ = run_command('curl -s "https://get.elabftw.net/?key"')
        eln_mysqlpw, _ = run_command("pwgen -s 31 1")

    def init_proxy(self):
        logger.info("### INITIALIZING PROXY ###")

        proxy_env_variables = {
            "NGINX_PRIMARY_DOMAIN": self.settings.base_domain,
            "NGINX_PROXY_PASS": f"http://{self.settings.base_domain}",
            "LETSENCRYPT_EMAIL": self.settings.letsencryptemail,
            "LETSENCRYPT_STAGING": self.settings.letsencrypt_staging,
            "API_PUBLIC_DOMAIN": f"{self.settings.domains.backend}",
            "APP_PUBLIC_DOMAIN": f"{self.settings.domains.frontend}",
            "AUTH_PUBLIC_DOMAIN": f"{self.settings.domains.auth}",
            "ELN_PUBLIC_DOMAIN": f"{self.settings.domains.eln}",
            "GRAFANA_PUBLIC_DOMAIN": f"{self.settings.domains.grafana}",
            "TELEPORT_PUBLIC_DOMAIN": f"{self.settings.domains.teleport}",
            "NGINX_DOMAIN_LIST": self.settings.domains_list,
        }

        proxy_vars_to_be_quoted = {
            "NGINX_DOMAIN_LIST",
            "LETSENCRYPT_EMAIL",
            "LETSENCRYPT_STAGING",
        }

        write_env_file(
            PROXY_ENV_FILE_LOCATION, proxy_env_variables, proxy_vars_to_be_quoted
        )

        run_command("cd ./bioterm/server/proxy/ && sudo ./init.sh yes")

        # f"{'yes' if self.settings.letsencrypt_staging == '1' else 'no'}"

    def init_authentik(self):
        """
        Initializes the authentik environment for the bioterm application.

        This method performs several steps to configure and initialize the authentik
        environment, including setting environment variables, starting Docker compose
        for Authentik, copying branding files, and creating the required OAuth2 and
        SAML providers as well as respective applications.

        Raises:
        Exception: If there is an error in extracting the public key.
        """
        logger.info("### INITIALIZING AUTHENTIK ###\n### THIS MAY TAKE A WHILE...")

        auth_env_variables = {
            "PG_PASS": self.settings.auth_pg_pass,
            "AUTHENTIK_SECRET_KEY": self.settings.authentik_secret_key,
            "AUTHENTIK_BOOTSTRAP_PASSWORD": self.settings.admin_password,
            "AUTHENTIK_BOOTSTRAP_TOKEN": self.settings.authentik_apikey,
            "AUTHENTIK_BOOTSTRAP_EMAIL": f"{self.settings.admin_email}",
        }

        if self.settings.imprint:
            auth_env_variables["AUTHENTIK_FOOTER_LINKS"] = (
                f'[{{"name": "Imprint & Privacy Policy",'
                f'"href":"https://{self.settings.domains.frontend}/#/imprint"}}]'
            )

        auth_vars_to_be_quoted = {"AUTHENTIK_BOOTSTRAP_EMAIL"}

        write_env_file(
            AUTH_ENV_FILE_LOCATION, auth_env_variables, auth_vars_to_be_quoted
        )

        run_command("cd bioterm/server/auth/ && sudo docker compose up -d")

        run_command(
            "sudo cp bioterm/server/auth/bioterm_icon_512x512.png "
            "/srv/docker/authentik/media/"
        )

        run_command(
            "sudo cp bioterm/server/auth/bioterm_logo_inverted.svg "
            "/srv/docker/authentik/media/"
        )

        # timeout for how long we want to wait for the authentik server to become
        # available (in seconds)
        start_time = time.time()
        timeout = 120
        while time.time() - start_time < timeout:
            logger.info("Waiting for authentik container to complete starting...")
            time.sleep(5)

        # # Wait for the authentik server to become available
        # start_time = time.time()
        # # filelogger(
        # #     f"Waiting for https://{authentik_subdomain}.{base_domain} "
        # #     f"to become available...",
        # #     output_file_path,
        # # )
        # while not is_server_available(f"https://{authentik_subdomain}.{base_domain}"):
        #     if time.time() - start_time > timeout:
        #         filelogger(
        #             "Timed out waiting for authentik to become available...",
        #             output_file_path,
        #         )
        #         break
        #     filelogger(
        #         "Waiting for authentik to become available...",
        #         output_file_path,
        #     )
        #     time.sleep(5)  # Wait for 5 second before checking again

        host_url = f"https://{self.settings.domains.auth}/api/v3/"

        authentik_config = authentikApiClient.Configuration(host=host_url)
        authentik_config.api_key["authentik"] = self.settings.authentik_apikey
        authentik_config.api_key_prefix["authentik"] = "Bearer"
        if self.settings.letsencrypt_staging == "1":
            authentik_config.verify_ssl = False

        service = AuthentikService(config=authentik_config)
        service.brand_authentik_default_tenant(domain=self.settings.base_domain)
        service.brand_default_authentication_flow()
        certificate_data = service.download_certificate()
        try:
            pubkey = extract_pubkey_from_cert(certificate_data)
        except Exception as e:
            print(f"Error: {e}")
            exit(1)

        # Format the result and store the pubkey in settings
        self.settings.authentik_public_key = pubkey.replace("\n", "\\n")

        self.settings.authentik_authorization_flow_pk = (
            service.get_default_provider_authorization_explicit_consent_pk()
        )

        authentik_provider_backend_certificate_pk = service.get_certificate_pk()

        backend_redirect_uris = (
            f"https://{self.settings.domains.backend}"
            f"/docs/ouath2-redirect\n"
            f"https://{self.settings.domains.frontend}"
            f"/callback.html"
        )
        grafana_redirect_uris = (
            f"https://{self.settings.domains.grafana}" f"/login/generic_oauth"
        )

        scopes = service.get_oauth_openid_property_mappings()

        oauth2providers = []
        oauth2providers.append(
            authentikApiClient.OAuth2ProviderRequest(
                name="grafana",
                authorization_flow=self.settings.authentik_authorization_flow_pk,
                client_type="confidential",
                client_id=self.settings.authentik_provider_grafana_client_id,
                client_secret=self.settings.authentik_provider_grafana_client_secret,
                redirect_uris=grafana_redirect_uris,
                access_code_validity="minutes=1",
                access_token_validity="minutes=5",
                refresh_token_validity="days=30",
                sub_mode="hashed_user_id",
                issuer_mode="per_provider",
                include_claims_in_id_token=True,
                property_mappings=scopes,
            )
        )

        oauth2providers.append(
            authentikApiClient.OAuth2ProviderRequest(
                name="backend",
                authorization_flow=self.settings.authentik_authorization_flow_pk,
                client_type="public",
                client_id=self.settings.authentik_provider_backend_client_id,
                redirect_uris=backend_redirect_uris,
                signing_key=authentik_provider_backend_certificate_pk,
                access_code_validity="minutes=1",
                access_token_validity="minutes=5",
                refresh_token_validity="days=30",
                sub_mode="hashed_user_id",
                issuer_mode="per_provider",
                include_claims_in_id_token=True,
                property_mappings=scopes,
            )
        )

        for oauthprovider in oauth2providers:
            service.create_oauth_provider(oauthprovider)

        nameid_mapping = service.get_saml_nameid_property_mapping()
        mappings = service.get_saml_property_mappings()

        samlproviders = []
        samlproviders.append(
            authentikApiClient.SAMLProviderRequest(
                name="eln",
                authorization_flow=self.settings.authentik_authorization_flow_pk,
                acs_url=f"https://{self.settings.domains.eln}/index.php?acs",
                issuer=f"https://{self.settings.domains.auth}",
                sp_binding="post",
                name_id_mapping=nameid_mapping,
                property_mappings=mappings,
                assertion_valid_not_before="minutes=-5",
                assertion_valid_not_on_or_after="minutes=5",
                session_valid_not_on_or_after="minutes=30",
                digest_algorithm="http://www.w3.org/2001/04/xmlenc#sha256",
                signature_algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
            )
        )

        for samlprovider in samlproviders:
            service.create_saml_provider(samlprovider)

        # providers = service.get_providers() # this does not work,
        # due to the false openapi schema so instead of fetching the
        # provider ids, the order of provider creation has to be recalled

        applications = []
        applications.append(
            authentikApiClient.ApplicationRequest(
                name="grafana",
                slug="grafana",
                provider=1,
                policy_engine_mode="all",
                meta_launch_url=f"https://{self.settings.domains.grafana}",
            )
        )

        applications.append(
            authentikApiClient.ApplicationRequest(
                name="bioterm",
                slug="bioterm",
                provider=2,
                policy_engine_mode="all",
                meta_launch_url=f"https://{self.settings.domains.frontend}",
            )
        )

        applications.append(
            authentikApiClient.ApplicationRequest(
                name="eln",
                slug="eln",
                provider=3,
                policy_engine_mode="all",
                meta_launch_url=f"https://{self.settings.domains.eln}",
            )
        )

        for application in applications:
            service.create_application(application)

    def init_eln(self):
        pass

    def init_grafana(self):
        logger.info("### INITIALIZING GRAFANA ###")

        run_command("sudo mkdir -p /srv/docker/grafana")
        run_command("sudo chown 472 /srv/docker/grafana")

        gf_auth_url = f"https://{self.settings.domains.auth}/application/o/authorize/"
        gf_token_url = f"https://{self.settings.domains.auth}/application/o/token/"
        gf_api_url = f"https://{self.settings.domains.auth}/application/o/userinfo/"
        gf_redirect_url = (
            f"https://{self.settings.domains.auth}/if/session-end/grafana/"
        )
        gf_jwt_url = f"https://{self.settings.domains.auth}/application/o/bioterm/jwks/"
        gf_client_id = self.settings.authentik_provider_grafana_client_id
        gf_client_secret = self.settings.authentik_provider_grafana_client_secret
        skip_tls = "true" if self.settings.letsencrypt_staging == "1" else "false"

        grafana_env_variables = {
            "GF_SECURITY_ADMIN_PASSWORD": self.settings.grafana_password,
            "GF_SERVER_DOMAIN": self.settings.domains.grafana,
            "GF_SERVER_ROOT_URL": f"https://{self.settings.domains.grafana}",
            "GF_AUTH_GENERIC_OAUTH_TLS_SKIP_VERIFY_INSECURE": skip_tls,
            "GF_AUTH_GENERIC_OAUTH_AUTH_URL": gf_auth_url,
            "GF_AUTH_GENERIC_OAUTH_TOKEN_URL": gf_token_url,
            "GF_AUTH_GENERIC_OAUTH_API_URL": gf_api_url,
            "GF_AUTH_SIGNOUT_REDIRECT_URL": gf_redirect_url,
            "GF_AUTH_GENERIC_OAUTH_CLIENT_ID": gf_client_id,
            "GF_AUTH_GENERIC_OAUTH_CLIENT_SECRET": gf_client_secret,
            "GF_AUTH_JWT_JWK_SET_URL": gf_jwt_url,
        }

        grafana_vars_to_be_quoted = {}

        write_env_file(
            GRAFANA_ENV_FILE_LOCATION, grafana_env_variables, grafana_vars_to_be_quoted
        )

        run_command(
            "cd bioterm/server/grafana "
            "&& cp docker-compose.yml.template docker-compose.yml"
        )
        run_command("cd bioterm/server/grafana && sudo docker compose up -d")

        time.sleep(20)

        config = grafanaApiClient.Configuration(
            host=f"https://{self.settings.domains.grafana}/api",
            username="admin",
            password=self.settings.grafana_password,
        )
        if self.settings.letsencrypt_staging == "1":
            config.verify_ssl = False

        client = grafanaApiClient.ApiClient(configuration=config)

        datasources = grafanaApiClient.DatasourcesApi(api_client=client)

        datasources.get_data_sources()

        json_data = {
            "sslmode": "disable",
            "postgresVersion": 1200,
            "timescaledb": True,
        }

        secure_json_data = {"password": self.settings.pg_password}

        postgres_datasource = grafanaApiClient.AddDataSourceCommand(
            basicAuth=True,
            basicAuthUser="postgres",
            name="PostgreSQL",
            type="grafana-postgresql-datasource",
            url="timescaledb:5432",
            user="postgres",
            is_default=True,
            json_data=json_data,
            secureJsonData=secure_json_data,
            access="proxy",
            database="bioterm",
        )

        loki_datasource = grafanaApiClient.AddDataSourceCommand(
            name="Loki",
            type="loki",
            url="http://loki:3100",
            is_default=False,
            access="proxy",
        )

        prometheus_datasource = grafanaApiClient.AddDataSourceCommand(
            name="Prometheus",
            type="prometheus",
            url="http://prometheus:9090",
            is_default=False,
            access="proxy",
        )

        datasources.add_data_source(loki_datasource)
        datasources.add_data_source(prometheus_datasource)
        datasources.add_data_source(postgres_datasource)

    def init_backend(self):
        logger.info("### INITIALIZING BACKEND ###")

        secret_key, _ = run_command("openssl rand -base64 32")

        issue = f"https://{self.settings.domains.auth}/application/o/bioterm/"

        api_env_variables = {
            "SECRET_KEY": secret_key,
            "POSTGRES_USER": "postgres",
            "POSTGRES_DB": "bioterm",
            "POSTGRES_PASSWORD": self.settings.pg_password,
            "GF_SECURITY_ADMIN_PASSWORD": self.settings.grafana_password,
            "GF_SERVER_DOMAIN": self.settings.domains.grafana,
            "GF_SERVER_ROOT_URL": f"https://{self.settings.domains.grafana}",
            "AUTHENTIK_CLIENT_ID": self.settings.authentik_provider_backend_client_id,
            "AUTHENTIK_URL": f"https://{self.settings.domains.auth}",
            "AUTHENTIK_ISSUER": issue,
            "AUTHENTIK_PUBLIC_KEY": self.settings.authentik_public_key,
        }

        api_vars_to_be_quoted = {"AUTHENTIK_PUBLIC_KEY"}

        write_env_file(API_ENV_FILE_LOCATION, api_env_variables, api_vars_to_be_quoted)

        # build the backend docker image, then start it and run the database init
        run_command(
            "sudo docker buildx build -t bioterm/server/backend "
            "-f bioterm/server/backend/Dockerfile ."
        )
        run_command(
            "cd bioterm/server/backend "
            "&& cp docker-compose.yml.template docker-compose.yml "
            "&& sudo docker compose up -d"
        )

        # start_time = time.time()
        # timeout = 30
        # while time.time() - start_time < timeout:
        #     logger.info("Waiting for timescaledb container to complete starting...")
        #     time.sleep(5)

        time.sleep(10)

        run_command(
            "cd bioterm/server/backend "
            "&& sudo docker compose exec -it bioterm-dbworker /bin/bash "
            "-c 'alembic -c bioterm/server/backend/alembic.ini upgrade head'"
        )

    def init_frontend(self):
        logger.info("### INITIALIZING FRONTEND ###")
        metadata_url = (
            f"https://{self.settings.domains.auth}"
            f"/application/o/bioterm/.well-known/openid-configuration"
        )
        redirect_url = f"https://{self.settings.domains.frontend}/callback.html"
        post_logout_redirect_url = f"https://{self.settings.domains.frontend}"
        authorize_url = (
            f"https://{self.settings.domains.frontend}/application/o/authorize/"
        )

        app_env_variables = {
            "API_URL": f"https://{self.settings.domains.backend}",
            "BASE_URL": f"https://{self.settings.domains.frontend}",
            "AUTH0_DOMAIN": f"https://{self.settings.domains.auth}/application/o",
            "AUTHENTIK_METADATA_URL": metadata_url,
            "AUTHENTIK_CLIENT_ID": self.settings.authentik_provider_backend_client_id,
            "AUTHENTIK_REDIRECT_URI": redirect_url,
            "AUTHENTIK_POST_LOGOUT_REDIRECT_URI": post_logout_redirect_url,
            "AUTHENTIK_AUTHORIZE_URI": authorize_url,
            "ELN_DOMAIN": f"{self.settings.domains.eln}",
            "GRAFANA_DOMAIN": f"{self.settings.domains.grafana}",
        }

        app_vars_to_be_quoted = {}

        write_env_file(APP_ENV_FILE_LOCATION, app_env_variables, app_vars_to_be_quoted)

        run_command(
            "cd bioterm/server/frontend "
            "&& sudo docker buildx build -t bioterm/server/frontend ."
        )
        run_command(
            "cd bioterm/server/frontend "
            "&& cp docker-compose.yml.template docker-compose.yml "
            "&& sudo docker compose up -d"
        )


def get_env_or_prompt(d, env_name, prompt, is_password=False, validate_func=None):
    """Get an environment variable or prompt the user if not set."""
    value = os.getenv(env_name)
    if value is None:
        while True:
            if is_password:
                code, value = d.passwordbox(prompt, insecure=True)
            else:
                code, value = d.inputbox(prompt)

            if code != d.OK:
                d.clear()
                exit(0)  # Exit if user cancels

            if is_password:
                code, confirm_value = d.passwordbox("Confirm password:", insecure=True)
                if value != confirm_value:
                    d.msgbox("Passwords do not match. Please try again.")
                    continue

            if validate_func and not validate_func(value):
                d.msgbox("Invalid input. Please try again.")
            else:
                break
    return value


def get_subdomain_selection(d, base_domain, subdomains):
    """Prompt user to select which default subdomains to modify."""
    choices = [
        (key, f"{value}.{base_domain}", False) for key, value in subdomains.items()
    ]
    code, selected = d.checklist(
        f"Select subdomains to modify for {base_domain}:", choices=choices
    )

    if code != d.OK:
        d.clear()
        exit(0)  # Exit if user cancels

    # Prompt for custom subdomains if selected for modification
    for key in selected:
        while True:
            code, custom_subdomain = d.inputbox(f"Enter custom subdomain for '{key}':")
            if code != d.OK:
                d.clear()
                exit(0)
            full_domain = (
                f"{custom_subdomain}.{base_domain}"
                if custom_subdomain
                else f"{key}.{base_domain}"
            )
            if validate_domain(full_domain):
                subdomains[key] = custom_subdomain or key
                break
            else:
                d.msgbox("Invalid domain. Please try again.")

    return subdomains


# def run_command(command):
#     return (
#         subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
#         .stdout.decode("utf-8")
#         .strip()
#     )


def run_command(command, output_file=None):
    if output_file:
        with open(output_file, "w") as file:
            subprocess.run(command, shell=True, check=True, stdout=file, stderr=file)
    else:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return (
            result.stdout.decode("utf-8").strip(),
            result.stderr.decode("utf-8").strip(),
        )


def extract_pubkey_from_cert(certificate_data: bytes) -> str:
    """
    Extracts the public key from a given certificate using OpenSSL.

    This function takes a certificate in bytes format and uses the 'openssl' command
    line utility to extract the public key. The certificate data should be in a format
    compatible with OpenSSL (e.g., PEM or DER). The function returns the public key as
    a UTF-8 encoded string.

    :param bytes certificate_data: The certificate data in bytes from which the public
                                    key is to be extracted.
    :return: The public key extracted from the given certificate.
    :rtype: str
    :raises Exception: If an error occurs while running the 'openssl' command.

    Example:
        >>> with open('certificate.pem', 'rb') as f:
        ...     cert_data = f.read()
        >>> pubkey = extract_pubkey_from_cert(cert_data)
        >>> print(pubkey)
        -----BEGIN PUBLIC KEY-----
        ...
        -----END PUBLIC KEY-----
    """
    try:
        openssl_output_bytes = subprocess.check_output(
            [
                "openssl",
                "x509",
                "-pubkey",
                "-noout",
            ],
            input=certificate_data,
        )
        # Decode the output to a string (UTF-8 encoded)
        openssl_output = openssl_output_bytes.decode("utf-8")
        return openssl_output.strip()
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running openssl: {e}")


# def run_bash_scripts_in_thread(script_commands, output_file, error_flag, error_msg):
#     def target():
#         for command in script_commands:
#             with open(output_file, "a") as file:
#                 script_args = command.split()
#                 result = subprocess.run(script_args, stdout=file, stderr=file)
#                 if result.returncode != 0:
#                     error_flag[0] = True
#                     error_msg[0] = f"Error occurred during script: {command}"
#                     break

#     thread = threading.Thread(target=target)
#     thread.start()
#     return thread


# Function to run bash scripts and handle installation
def run_installation(
    user_input: UserInputsServerInstallation,
    output_file_path=None,
    error_flag=None,
    error_msg=None,
):
    base_domain = user_input.base_domain
    subdomains = FullSubDomains(
        auth=f"{user_input.subdomains['authentik']}.{base_domain}",
        backend=f"{user_input.subdomains['backend']}.{base_domain}",
        eln=f"{user_input.subdomains['eln']}.{base_domain}",
        frontend=f"{user_input.subdomains['frontend']}.{base_domain}",
        grafana=f"{user_input.subdomains['grafana']}.{base_domain}",
        teleport=f"{user_input.subdomains['teleport']}.{base_domain}",
    )

    all_domains = (
        base_domain
        + " "
        + " ".join([f"{v}.{base_domain}" for v in user_input.subdomains.values()])
    )

    settings = ServerSettings(
        domains=subdomains,
        base_domain=base_domain,
        docker_network_name="bioterm",
        NGINX_PRIMARY_DOMAIN=base_domain,
        NGINX_PROXY_PASS=f"http://{base_domain}",
        letsencryptemail=user_input.letsencryptemail,
        letsencrypt_staging=user_input.staging,
        API_PUBLIC_DOMAIN=subdomains.backend,
        APP_PUBLIC_DOMAIN=subdomains.frontend,
        AUTH_PUBLIC_DOMAIN=subdomains.auth,
        ELN_PUBLIC_DOMAIN=subdomains.eln,
        GRAFANA_PUBLIC_DOMAIN=subdomains.grafana,
        TELEPORT_PUBLIC_DOMAIN=subdomains.teleport,
        domains_list=all_domains,
        admin_email=user_input.email,
        admin_password=user_input.password,
        project_name="bioterm",
        BACKEND_SECRET_KEY="",
        imprint=user_input.imprint,
    )

    installer = ServerInstaller(settings=settings)

    installer.update_hostfile(user_input=user_input, base_domain=base_domain)
    installer.init_credentials()
    installer.init_proxy()
    installer.init_authentik()
    # installer.init_eln()
    installer.init_backend()
    installer.init_frontend()
    installer.init_grafana()

    logger.info("### FINISHED SETUP ###")

    # bash_script_paths = [f"./bioterm/server/proxy/init.sh {user_input.staging}"]

    # except Exception as e:
    #     logger.error(f"This did not work: {e}")
    # error_flag[0] = True
    # error_msg[0] = str(e)


# Function to display the tailbox
def display_tailbox(d, file_path, error_flag):
    while not error_flag[0]:  # Check for error flag
        d.tailbox(file_path, width=80, height=20, exit_label="Exit")
        time.sleep(0.1)


def main():
    # Check if script is running with elevated rights
    if not os.geteuid() == 0:
        print("Elevated rights required, terminating...")
        sys.exit(1)

    locale.setlocale(locale.LC_ALL, "")

    if not is_docker_source_added():
        install_docker_sources()

    for package in PACKAGES:
        if not is_package_installed(package):
            print(f"Package {package} is not installed. Installing...")
            install_package(package)
        else:
            print(f"Package {package} is already installed.")

    module_name = "dialog"
    try:
        dialog = __import__(module_name)
    except ImportError:
        print(f"Failed to import module {module_name}.")
        sys.exit(1)

    d = dialog.Dialog(dialog="dialog")
    d.set_background_title("bioterm Server Configuration")

    # Dictionary of locations to check for existing .env files
    server_locations_to_check = {
        "auth": "./bioterm/server/auth",
        "backend": "./bioterm/server/backend",
        "eln": "./bioterm/server/eln",
        "frontend": "./bioterm/server/frontend/web_ui",
        "grafana": "./bioterm/server/grafana",
        "proxy": "./bioterm/server/proxy",
        "teleport": "./bioterm/server/teleport",
    }

    # Check for existing .env files
    found, location_name = check_existing_env_files(server_locations_to_check)
    if found:
        d.msgbox(
            f"Existing .env file found in {location_name} directory. "
            f"Terminating script."
        )
        d.clear()
        exit(0)

    # Ask the user if this is a production setup
    code = d.yesno(
        "Do you want to use certificates provided by lets-encrypt using certbot?",
        width=80,
        height=20,
    )
    if code == d.OK:
        useletsencrypt = True  # User selected 'Yes'
        code = d.yesno("Do you want to enable staging?", width=80, height=20)
        enable_staging = "1" if code == d.OK else "0"

    else:
        useletsencrypt = False  # User selected 'No'
        d.msgbox("Currently not supported.")
        d.clear()
        exit(0)

    # TODO: add actual functionality behind this query
    gdpr = d.yesno(
        "Do you want to display an 'Imprint & Data Policy' link on frontpages?",
        width=80,
        height=20,
    )

    if gdpr == d.OK:
        display_imprint = True
    else:
        display_imprint = False

    # Get environment variables or prompt user
    email = get_env_or_prompt(
        d,
        "EMAIL",
        "Enter the admin user's email address.",
        validate_func=validate_email,
    )

    letsencryptemail = ""
    if useletsencrypt:
        code = d.yesno(
            f"Do you want to set {email} as contact address for letsencrypt "
            f"to update you on upcoming certificate renewals? The renewal itself"
            f"should be automatically handled.",
            width=80,
            height=20,
        )
        if code == d.OK:
            letsencryptemail = email
        else:
            letsencryptemail = get_env_or_prompt(
                d,
                "LETSENCRYPTEMAIL",
                "Enter the email address to be used with letsencrypt:",
                validate_func=validate_email,
            )

    password = get_env_or_prompt(
        d,
        "PASSWORD",
        "Enter a one-time password to be used during the authentik setup.",
        is_password=True,
    )
    base_domain = get_env_or_prompt(
        d, "DOMAIN", "Enter your base domain name:", validate_func=validate_domain
    )

    # Default subdomains
    subdomains = {
        "frontend": "app",
        "backend": "api",
        "eln": "eln",
        "grafana": "grafana",
        "authentik": "auth",
        "teleport": "teleport",
    }

    # Get subdomain selection and customization
    customized_subdomains = get_subdomain_selection(d, base_domain, subdomains)

    # Prepare subdomain summary
    subdomain_summary = "\n, ".join(
        [f"{v}.{base_domain} ({k})" for k, v in customized_subdomains.items()]
    )

    # Confirmation page
    confirmation_message = (
        f"""Please confirm the entered information:\n\n"""
        f"""Using Letsencrypt: {useletsencrypt}"""
        f"""Display Imprint Link: {display_imprint}"""
        f"""Email: {email}\n"""
        f"""Password: [HIDDEN]\n"""
        f"""Letsencrypt Email: {letsencryptemail}"""
        f"""Domains: {subdomain_summary}\n\n"""
        f"""The displayed domains will be added to /etc/hosts mapping to 127.0.0.1 ."""
        f"""Current hostfile will be stored as /etc/hosts.old"""
    )
    code = d.yesno(confirmation_message, height=20, width=80)

    if code != d.OK:
        d.msgbox("Configuration cancelled.")
        d.clear()
        exit(0)

    user_input = UserInputsServerInstallation(
        base_domain=base_domain,
        subdomains=customized_subdomains,
        password=password,
        email=email,
        useletsencrypt=useletsencrypt,
        staging=enable_staging,
        letsencryptemail=letsencryptemail,
        imprint=display_imprint,
    )

    d.clear()

    run_installation(user_input=user_input)

    d.msgbox(
        "Installation finished.\n\n"
        "Please remember to change the authentik one-time password and enable 2FA.",
        width=80,
        height=20,
    )

    d.clear()
    # d.msgbox("Configuration saved to .env file.")

    # # Create a temporary file to store the scripts' output
    # with tempfile.NamedTemporaryFile(delete=False) as temp_output_file:
    #     error_flag = [False]  # Flag to indicate if an error occurs
    #     error_msg = [""]  # Message to store error information

    #     # Initialize Dialog
    #     d = dialog.Dialog(dialog="dialog")

    #     # Start the installation thread
    #     install_thread = threading.Thread(
    #         target=run_installation,
    #         args=(user_input, temp_output_file.name, error_flag, error_msg),
    #     )
    #     install_thread.start()

    #     # Start the tailbox thread
    #     tailbox_thread = threading.Thread(
    #         target=display_tailbox,
    #         args=(d, temp_output_file.name, error_flag),
    #     )
    #     tailbox_thread.start()

    #     # Wait for both threads to finish
    #     install_thread.join()
    #     tailbox_thread.join()

    #     if error_flag[0]:
    #         d.clear()
    #         d.msgbox(error_msg[0])
    #     else:
    #         d.msgbox("Script execution completed successfully.")

    #     # Copy the content of the temporary file to the log file
    #     log_file_path = "./server_installation.log"
    #     shutil.copy(temp_output_file.name, log_file_path)

    #     # Remove the temporary file after use
    #     os.remove(temp_output_file.name)

    # # Copy the content of the temporary file to the log file
    # shutil.copy(temp_output_file.name, log_file_path)

    # # Remove the temporary file after use
    # os.remove(temp_output_file.name)

    # d.clear()


if __name__ == "__main__":
    main()
