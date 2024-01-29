import os
import sys

from pydantic import ValidationError


sys.path.append(
    os.path.join(os.path.dirname(__file__), "bioterm/common/services/authentik/")
)

import authentikApiClient  # noqa: E402


class AuthentikService:
    def __init__(
        self,
        config: authentikApiClient.Configuration = None,
    ):
        print(f"Base Path is: {config._base_path}")
        self.ApiClient = authentikApiClient.ApiClient(configuration=config)

    def _get_default_authentication_flow(self) -> authentikApiClient.Flow:
        flows = authentikApiClient.FlowsApi(self.ApiClient)
        return flows.flows_instances_retrieve(slug="default-authentication-flow")

    def get_default_provider_authorization_explicit_consent_pk(
        self,
    ) -> str:
        flows = authentikApiClient.FlowsApi(self.ApiClient)
        return flows.flows_instances_retrieve(
            slug="default-provider-authorization-explicit-consent"
        ).pk

    def get_oauth_openid_property_mappings(self):
        scopes = []
        mappings = authentikApiClient.PropertymappingsApi(self.ApiClient)
        results = mappings.propertymappings_scope_list().results
        for result in results:
            if result.name in [
                "authentik default OAuth Mapping: OpenID 'email'",
                "authentik default OAuth Mapping: OpenID 'openid'",
                "authentik default OAuth Mapping: OpenID 'profile'",
            ]:
                scopes.append(result.pk)
        return scopes

    def get_saml_nameid_property_mapping(self):
        mappings = authentikApiClient.PropertymappingsApi(self.ApiClient)
        results = mappings.propertymappings_saml_list().results
        for result in results:
            if result.name in [
                "authentik default SAML Mapping: Email",
            ]:
                return result.pk

    def get_saml_property_mappings(self):
        mappings = authentikApiClient.PropertymappingsApi(self.ApiClient)
        results = mappings.propertymappings_saml_list().results
        property_mappings = []
        for result in results:
            property_mappings.append(result.pk)
        return property_mappings

    def brand_default_authentication_flow(self) -> None:
        # flow = self._get_default_authentication_flow()
        # flow.name = "Welcome to the bioterm SSO!"
        # flow.title = flow.name
        flows = authentikApiClient.FlowsApi(self.ApiClient)
        flows.flows_instances_partial_update(
            slug="default-authentication-flow",
            patched_flow_request=authentikApiClient.PatchedFlowRequest(
                title="Welcome to the bioterm SSO!",
                name="Welcome to the bioterm SSO!",
                compatibility_mode=True,
            ),
        )

    def brand_authentik_default_tenant(self, domain: str) -> None:
        core = authentikApiClient.CoreApi(self.ApiClient)
        default_tenant = core.core_tenants_list(domain="authentik-default")
        core.core_tenants_partial_update(
            tenant_uuid=default_tenant.results[0].tenant_uuid,
            patched_tenant_request=authentikApiClient.PatchedTenantRequest(
                domain=domain,
                branding_title="bioterm",
                branding_logo="/media/bioterm_logo_inverted.svg.svg",
                branding_favicon="/media/bioterm_icon_512x512.png",
            ),
        )

    def get_certificate_pk(self):
        return (
            authentikApiClient.CryptoApi(self.ApiClient)
            .crypto_certificatekeypairs_list(name="authentik Self-signed Certificate")
            .results[0]
            .pk
        )

    def download_certificate(self) -> str:
        crypto = authentikApiClient.CryptoApi(self.ApiClient)
        self_signed_certificate = crypto.crypto_certificatekeypairs_list(
            name="authentik Self-signed Certificate"
        )
        return crypto.crypto_certificatekeypairs_view_certificate_retrieve_without_preload_content(
            kp_uuid=self_signed_certificate.results[0].pk, download=False
        ).data

    def create_saml_provider(self, provider: authentikApiClient.SAMLProviderRequest):
        try:
            providers = authentikApiClient.ProvidersApi(self.ApiClient)
            providers.providers_saml_create(saml_provider_request=provider)
        except ValidationError as e:
            # the schema provided by authentik seems to be broken or the restframework
            # serializer requires fixing, needs to be investigated
            for error in e.errors():
                if error["loc"][0] in [
                    "assigned_application_slug",
                    "assigned_application_name",
                    "assigned_backchannel_application_slug",
                    "assigned_backchannel_application_name",
                ]:
                    print(
                        f"More or less expected validation error in {error['loc'][0]}: "
                        f"{error['msg']}"
                    )
                else:
                    # Handle other validation errors
                    print(f"Unexpected validation error: {error}")
                    break

    def create_oauth_provider(self, provider: authentikApiClient.OAuth2ProviderRequest):
        try:
            providers = authentikApiClient.ProvidersApi(self.ApiClient)
            providers.providers_oauth2_create(o_auth2_provider_request=provider)
        except ValidationError as e:
            # the schema provided by authentik seems to be broken or the restframework
            # serializer requires fixing, needs to be investigated
            for error in e.errors():
                if error["loc"][0] in [
                    "assigned_application_slug",
                    "assigned_application_name",
                    "assigned_backchannel_application_slug",
                    "assigned_backchannel_application_name",
                ]:
                    print(
                        f"More or less expected validation error in {error['loc'][0]}: "
                        f"{error['msg']}"
                    )
                else:
                    # Handle other validation errors
                    print(f"Unexpected validation error: {error}")
                    break

    def get_providers(self):
        providerapi = authentikApiClient.ProvidersApi(self.ApiClient)
        results = providerapi.providers_all_list().results
        providers = {}
        for result in results:
            providers[result.name] = result.pk
        return providers

    def create_application(self, application: authentikApiClient.ApplicationRequest):
        try:
            core = authentikApiClient.CoreApi(api_client=self.ApiClient)
            core.core_applications_create(application_request=application)
        except ValidationError as e:
            # the schema provided by authentik seems to be broken or the restframework
            # serializer requires fixing, needs to be investigated
            for error in e.errors():
                if error["loc"][0] in [
                    "assigned_backchannel_application_slug",
                    "assigned_backchannel_application_name",
                ]:
                    print(
                        f"More or less expected validation error in {error['loc'][0]}: "
                        f"{error['msg']}"
                    )
                else:
                    # Handle other validation errors
                    print(f"Unexpected validation error: {error}")
                    break

    def _get_flows():
        pass
