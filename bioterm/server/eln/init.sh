#!/bin/bash

set -e
docker compose version || exit 1

if [[ -f .env ]]; then
    echo "The .env file already exists. Exiting the script. Make a backup of the .env file before continuing"
    exit 1
fi

read -p "Please enter the domain name of the elabftw instance (without https://): " domain

/bin/bash ../../common/utils/domaincheck.sh $domain

elabftw_path="/srv/docker/elabftw"
mkdir -p $elabftw_path

# generate database passwords and secret_key and store in .env file
dbpw="$(pwgen -s 31 1)"
echo "DB_PASSWORD=$dbpw" >>.env
echo "MYSQL_PASSWORD=$dbpw" >>.env
#echo "SECRET_KEY=$(pwgen -s 136 1)" >>.env
{
    echo -n "SECRET_KEY="
    curl -s "https://get.elabftw.net/?key"
    echo ""
} >>.env
echo "MYSQL_ROOT_PASSWORD=$(pwgen -s 31 1)" >>.env
echo "SITE_URL=https://$domain" >>.env
echo "SERVER_NAME=$domain" >>.env

docker compose up -d
