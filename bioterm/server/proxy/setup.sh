#!/bin/bash

# EXPECTED CONTENT OF .env FILE
# NGINX_DOMAIN_LIST="example.org app.example.org grafana.example.org eln.example.org auth.example.org api.example.org"
# NGINX_PRIMARY_DOMAIN=example.org
# NGINX_PROXY_PASS="http://example.org"
# LETSENCRYPT_EMAIL=""
# LETSENCRYPT_STAGING="0"
# APP_PUBLIC_DOMAIN="app.example.org"
# ELN_PUBLIC_DOMAIN="eln.example.org"
# AUTH_PUBLIC_DOMAIN="auth.example.org"
# GRAFANA_PUBLIC_DOMAIN="grafana.example.org"
# API_PUBLIC_DOMAIN="api.example.org"
# TELEPORT_PUBLIC_DOMAIN="teleport.example.org"

if [[ -f .env ]]; then
    echo "The .env file already exists. Make a backup of the .env file before removing it. Then run this script again. Exiting..."
    exit 1
fi

read -p "Please enter the domain name of the bioterm instance (without https://, e.g. example.org): " domain

/bin/bash ../../common/utils/domaincheck.sh $domain

# set subdomains
SUBDOMAINS=("api" "app" "auth" "eln" "grafana" "teleport")

touch .env

# write domain and subdomains to .env file
echo "NGINX_PRIMARY_DOMAIN=${domain,,}" >.env
echo "NGINX_PROXY_PASS=\"http://${domain,,}\"" >>.env
echo "LETSENCRYPT_EMAIL=\"\"" >>.env
echo "LETSENCRYPT_STAGING=\"0\"" >>.env

for subdomain in ${SUBDOMAINS[*]}; do
    echo "${subdomain^^}_PUBLIC_DOMAIN=\"$subdomain.${domain,,}\"" >>.env
done

# create an array of domain and subdomains
domain_array=($domain)
for subdomain in ${SUBDOMAINS[*]}; do
    domain_array+=("$subdomain.$domain")
done

# write the array to the .env file
echo "NGINX_DOMAIN_LIST=\"${domain_array[*],,}\"" >>.env
