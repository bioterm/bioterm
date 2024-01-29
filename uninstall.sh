#!/bin/bash

# Check for root privileges
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root or with sudo." 1>&2
    exit 1
fi

# User verification to proceed
read -p "Are you sure you want to stop all Docker containers and remove /srv/docker? [y/N] " response
if [[ ! "$response" =~ ^[Yy]$ ]]; then
    echo "Operation cancelled by user."
    exit 1
fi

# User verification to proceed
read -p "Have you made backups and would still like to proceed? [y/N] " response
if [[ ! "$response" =~ ^[Yy]$ ]]; then
    echo "Operation cancelled by user."
    exit 1
fi

# Stop all running Docker containers
docker stop $(docker ps -aq)
docker remove $(docker ps -aq)

# Remove the /srv/docker directory
rm -rf /srv/docker

# Remove the .env and docker-compose.yml files
rm ./bioterm/server/auth/.env
rm ./bioterm/server/backend/.env
rm ./bioterm/server/backend/docker-compose.yml
rm ./bioterm/server/eln/.env
rm ./bioterm/server/frontend/.env
rm ./bioterm/server/frontend/docker-compose.yml
rm ./bioterm/server/grafana/.env
rm ./bioterm/server/grafana/docker-compose.yml
rm ./bioterm/server/proxy/.env
rm ./bioterm/server/proxy/docker-compose.yml
rm ./bioterm/server/teleport/.env
rm ./bioterm/server/teleport/docker-compose.yml

echo "Operation completed."
