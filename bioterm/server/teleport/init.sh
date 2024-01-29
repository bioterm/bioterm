#!/bin/bash
set -e
docker compose version || exit 1

# EXPECTED CONTENT OF .env FILE
# TELEPORT_PUBLIC_DOMAIN="teleport.example.org"

if [ -f ./.env ]; then
    echo "Sourcing .env file..."
    source ./.env
else
    echo "No .env file found, using defaults."
fi

teleport_domain_env="${TELEPORT_PUBLIC_DOMAIN:-"teleport.example.org"}"
echo "Teleport domain: ${TELEPORT_PUBLIC_DOMAIN}"

teleport_path="/srv/docker/teleport"
mkdir -p $certbot_path $teleport_path

echo "### Creating teleport.yaml from template in directory ${teleport_path}..."
sed "s/\${TELEPORT_PUBLIC_DOMAIN}/${teleport_domain_env}/g" \
    ./teleport.yaml.template >"${teleport_path}/teleport.yaml"
echo

if ! [ -f docker-compose.yml ]; then
    echo '### Building docker-compose file with correct docker images based on system architecture...'
    cp docker-compose.yml.template docker-compose.yml
    arch="$(uname -m)"
    if [[ "$arch" == "x86_64" ]]; then
        echo "### Detected x86_64 architecture..."
        sed -i 's/image: public.ecr.aws\/gravitational\/teleport:13.*$/image: public.ecr.aws\/gravitational\/teleport:13/g' docker-compose.yml
    elif [[ $(echo -e "$arch" | grep -e "arm" -e "aarch") ]]; then
        if [[ $(echo -e "$arch" | grep -e "armv8" -e "aarch64") ]]; then
            echo "### Detected arm64v8 architecture..."
            sed -i 's/image: public.ecr.aws\/gravitational\/teleport:13.*$/image: public.ecr.aws\/gravitational\/teleport:13-arm64/g' docker-compose.yml
        else
            echo "### Detected arm32 architecture..."
            sed -i 's/image: public.ecr.aws\/gravitational\/teleport:13.*$/image: public.ecr.aws\/gravitational\/teleport:13-arm/g' docker-compose.yml
        fi
    fi
fi

read -p "Do you want to continue here (and are not just testing)? (y/N) " decision
if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
    exit
fi

echo "### Starting docker container"
docker compose up -d
