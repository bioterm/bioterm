#!/bin/bash
# this script is based of https://github.com/wmnnd/nginx-certbot and several of related pull-requests
set -e
docker compose version || exit 1

# Check if a command line argument is provided and use it as the user input
if [ $# -eq 1 ]; then
  user_input="$1"
else
  # If no argument is provided, prompt the user for a choice
  read -p "Do you want to use certbot (only recommended for production)? (yes/no): " user_input
fi

# Convert the input to lowercase to ensure the script works even if the user inputs "Yes", "YES", etc.
user_input=$(echo "$user_input" | tr '[:upper:]' '[:lower:]')

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

if [ -f ./.env ]; then
  echo "Sourcing .env file..."
  source ./.env
else
  echo "No .env file found, using defaults."
fi

eln_domain_env="${ELN_PUBLIC_DOMAIN:-"eln.example.org www.eln.example.org"}"
grafana_domain_env="${GRAFANA_PUBLIC_DOMAIN:-"grafana.example.org www.grafana.example.org"}"
auth_domain_env="${AUTH_PUBLIC_DOMAIN:-"auth.example.org www.auth.example.org"}"
api_domain_env="${API_PUBLIC_DOMAIN:-"api.example.org www.api.example.org"}"
app_domain_env="${APP_PUBLIC_DOMAIN:-"app.example.org www.app.example.org"}"
teleport_domain_env="${TELEPORT_PUBLIC_DOMAIN:-"teleport.example.org www.teleport.example.org"}"
echo "Primary domain: ${NGINX_PRIMARY_DOMAIN}"

domain_array=("${NGINX_PRIMARY_DOMAIN:-"example.org www.example.org"}" ${eln_domain_env} ${grafana_domain_env} ${auth_domain_env} ${api_domain_env} ${app_domain_env} ${teleport_domain_env})
domains_env="${domain_array[*]}"
echo $domains_env
IFS=' ' read -r -a domains <<<"$domains_env"
primary_domain=${domains[0]:-$NGINX_PRIMARY_DOMAIN}

certbot_path="/srv/docker/certbot"
nginx_path="/srv/docker/nginx"
mkdir -p $certbot_path $nginx_path

email=${LETSENCRYPT_EMAIL:-""}    # Adding a valid address is strongly recommended
staging=${LETSENCRYPT_STAGING:-0} # Set to 1 if you're testing your setup to avoid hitting request limits
proxy_pass=${NGINX_PROXY_PASS:-"http://example.org"}
escaped_proxy_pass=$(printf '%s\n' "$proxy_pass" | sed -e 's/[\/&]/\\&/g')

echo "### Creating nginx.conf from template in directory ${nginx_path}..."
sed "s/\${NGINX_PRIMARY_DOMAIN}/${primary_domain}/g; \
  s/\${NGINX_PROXY_PASS}/${escaped_proxy_pass}/g; \
  s/\${ELN_PUBLIC_DOMAIN}/${eln_domain_env}/g; \
  s/\${AUTH_PUBLIC_DOMAIN}/${auth_domain_env}/g; \
  s/\${APP_PUBLIC_DOMAIN}/${app_domain_env}/g; \
  s/\${API_PUBLIC_DOMAIN}/${api_domain_env}/g; \
  s/\${GRAFANA_PUBLIC_DOMAIN}/${grafana_domain_env}/g; \
  s/\${TELEPORT_PUBLIC_DOMAIN}/${teleport_domain_env}/g" \
  ./nginx.conf.template >"${nginx_path}/nginx.conf"
echo

if ! [ -f docker-compose.yml ]; then
  echo '### Building docker-compose file with correct docker images based on system architecture...'
  cp docker-compose.yml.template docker-compose.yml

  arch="$(uname -m)"
  if [[ "$arch" == "x86_64" ]]; then
    echo "### Detected x86_64 architecture..."
    sed -i 's/image: certbot\/certbot.*$/image: certbot\/certbot:latest #certbot/g' docker-compose.yml
  elif [[ $(echo -e "$arch" | grep -e "arm" -e "aarch") ]]; then
    if [[ $(echo -e "$arch" | grep -e "armv8" -e "aarch64") ]]; then
      echo "### Detected arm64v8 architecture..."
      sed -i 's/image: certbot\/certbot.*$/image: certbot\/certbot:arm64v8-latest #certbot/g' docker-compose.yml
    else
      echo "### Detected arm32 architecture..."
      sed -i 's/image: certbot\/certbot.*$/image: certbot\/certbot:arm32v6-latest #certbot/g' docker-compose.yml
    fi
  fi

  if [ "$user_input" == "no" ]; then
    echo '### Disabling certbot container...'
    sed -i "/#certbot/ s/^/#/" docker-compose.yml
    echo '### Copying ssl files to /srv/docker/certbot/conf...'
    mkdir -p "$certbot_path/conf"
    cp options-ssl-nginx.conf "$certbot_path/conf"
    echo "### Follow documentation to create self-signed certificates for primary domain ${primary_domain}"
    echo "### Store self-signed certificates in /srv/docker/certbot/conf/live/${primary_domain}/"
    echo "### Then start nginx container manually using docker-compose..."
    exit 1
  else
    echo "### Continuing by running certbot.sh..."
    /bin/bash ./certbot.sh
    exit 0
  fi

else
  echo "### Found existing docker-compose.yml file. Exiting..."
  exit 1
fi
