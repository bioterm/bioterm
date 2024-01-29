#!/bin/bash
# this script is based of https://github.com/wmnnd/nginx-certbot and several of related pull-requests
set -e
docker compose version || exit 1

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
    echo "### Sourcing .env file..."
    source ./.env
else
    echo "No .env file found, run init.sh or create .env file manually. Exiting..."
    exit 1
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

rsa_key_size=4096

certbot_path="/srv/docker/certbot"
nginx_path="/srv/docker/nginx"
mkdir -p $certbot_path $nginx_path

email=${LETSENCRYPT_EMAIL:-""}    # Adding a valid address is strongly recommended
staging=${LETSENCRYPT_STAGING:-0} # Set to 1 if you're testing your setup to avoid hitting request limits
proxy_pass=${NGINX_PROXY_PASS:-"http://example.org"}
escaped_proxy_pass=$(printf '%s\n' "$proxy_pass" | sed -e 's/[\/&]/\\&/g')

# read -p "Do you want to continue here (and are not just testing)? (y/N) " decision
# if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
#     exit
# fi

# if [ -d "$certbot_path" ]; then
#     read -p "Existing data found for $domains. Continue and replace existing certificate? (y/N) " decision
#     if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
#         exit
#     fi
# fi

if [ ! -e "$certbot_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$certbot_path/conf/ssl-dhparams.pem" ]; then
    echo "### Downloading recommended TLS parameters ..."
    mkdir -p "$certbot_path/conf"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf >"$certbot_path/conf/options-ssl-nginx.conf"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem >"$certbot_path/conf/ssl-dhparams.pem"
    echo
fi

echo "### Creating dummy certificate for $domains ..."
path="/etc/letsencrypt/live/$domains"
mkdir -p "$certbot_path/conf/live/$domains"
docker compose run --rm --entrypoint "\
  openssl req -x509 -nodes -newkey rsa:$rsa_key_size -days 1\
    -keyout '$path/privkey.pem' \
    -out '$path/fullchain.pem' \
    -subj '/CN=localhost'" certbot
echo

echo "### Starting nginx ..."
docker compose up --force-recreate -d nginx
echo

echo "### Deleting dummy certificate for $domains ..."
docker compose run --rm --entrypoint "\
  rm -Rf /etc/letsencrypt/live/$domains && \
  rm -Rf /etc/letsencrypt/archive/$domains && \
  rm -Rf /etc/letsencrypt/renewal/$domains.conf" certbot
echo

echo "### Requesting Let's Encrypt certificate for $domains ..."
#Join $domains to -d args
domain_args=""
for domain in "${domains[@]}"; do
    domain_args="$domain_args -d $domain"
done

# Select appropriate email arg
case "$email" in
"") email_arg="--register-unsafely-without-email" ;;
*) email_arg="--email $email" ;;
esac

# Enable staging mode if needed
if [ $staging != "0" ]; then staging_arg="--staging"; fi

docker compose run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    $email_arg \
    $domain_args \
    --rsa-key-size $rsa_key_size \
    --agree-tos \
    --force-renewal" certbot
echo

echo "### Reloading nginx ..."
docker compose exec nginx nginx -s reload
