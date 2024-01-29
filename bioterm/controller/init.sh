#!/bin/bash
set -e

# Check for root privileges
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root or with sudo." 1>&2
    exit 1
fi

# Set the directory path
directory="/srv/docker/redis"

# Create the directory if it does not exist
mkdir -p "$directory"

# Navigate to the directory
cd "$directory"

# Create CA Key and Certificate
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt -subj "/C=DE/ST=Lower Saxony/L=Hanover/O=bioterm/OU=IT/CN=bioterm-controller-ca"

# Create Server Key and CSR (Certificate Signing Request)
openssl genrsa -out redis.key 2048
openssl req -new -key redis.key -out redis.csr -subj "/C=DE/ST=Lower Saxony/L=Hanover/O=bioterm/OU=IT/CN=localhost"

# Create Server Certificate signed with CA Certificate
openssl x509 -req -days 365 -in redis.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out redis.crt

# Clean up CSR file
rm redis.csr

# Check if OpenSSL command was successful
if [ $? -ne 0 ]; then
    echo "Failed to generate SSL certificate and key"
    exit 1
fi

# Check if Base64 encoding was successful
if [ $? -ne 0 ]; then
    echo "Failed to encode the certificate to Base64"
    exit 1
fi

echo "Certificate, key, and Base64 encoded certificate created in $directory"
