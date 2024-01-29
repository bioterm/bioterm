#!/bin/bash
set -e
docker compose version || exit 1

if [[ -f .env ]]; then
    echo "The .env file already exists. Make a backup of the .env file before removing it. Then run this script again. Exiting..."
    exit 1
fi

if [[ -f docker-compose.yml ]]; then
    echo "The docker-compose.yml file already exists. Make a backup of the docker-compose.yml file before removing it. Then run this script again. Exiting..."
    exit 1
fi

read -p "Please enter the domain name of the bioterm instance (without https://, e.g. example.org): " domain

/bin/bash ../../common/utils/domaincheck.sh $domain

echo "### Writing .env file..."
touch .env

echo "GF_SECURITY_ADMIN_PASSWORD: \"$(pwgen -s 40 1)\"" >.env
echo "GF_SERVER_DOMAIN: \"grafana.${domain}\"" >>.env
echo "GF_SERVER_ROOT_URL: \"https://grafana.${domain}\"" >>.env
echo "GF_AUTH_GENERIC_OAUTH_AUTH_URL: \"https://auth.${domain}/application/o/authorize/\"" >>.env
echo "GF_AUTH_GENERIC_OAUTH_TOKEN_URL: \"https://auth.${domain}/application/o/token/\"" >>.env
echo "GF_AUTH_GENERIC_OAUTH_API_URL: \"https://auth.${domain}/application/o/userinfo/\"" >>.env
echo "GF_AUTH_SIGNOUT_REDIRECT_URL: \"https://auth.${domain}/if/session-end/grafana/\"" >>.env
echo "GF_AUTH_JWT_JWK_SET_URL: \"https://auth.${domain}/application/o/bioterm/jwks/\"" >>.env
echo "GF_AUTH_GENERIC_OAUTH_CLIENT_ID: \"\" # insert authentik client ID obtained from provider settings" >>.env
echo "GF_AUTH_GENERIC_OAUTH_CLIENT_SECRET: \"\" # insert authentik client secret obtained from provider settings" >>.env

#echo "### Creating grafana.ini from template..."
#sed "s/\${GRAFANA_PUBLIC_DOMAIN}/grafana.${domain}/g" ./grafana.ini.template >"./grafana.ini"

echo "### Creating docker-compose.yml from template..."
sed "s/\${NGINX_PRIMARY_DOMAIN}/${domain}/g" ./docker-compose.yml.template >"./docker-compose.yml"

echo "### Retrieve oauth2 client id and secret from authentik and complete .env file. Then run \"sudo docker compose up -d\"..."
