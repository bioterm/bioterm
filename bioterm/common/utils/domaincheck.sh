#!/bin/bash

if [[ -z "$1" ]]; then
    echo "Domain name cannot be empty."
    exit 1
fi

if [[ "$1" == http://* || "$1" == https://* ]]; then
    echo "Domain name should not start with http:// or https://."
    exit 1
fi

if [[ "$1" != *"."* ]]; then
    echo "Domain name should contain a dot (.)."
    exit 1
fi

if [[ "$1" == *" "* ]]; then
    echo "Domain name should not contain spaces."
    exit 1
fi

if [[ ! "$1" =~ ^([a-zA-Z0-9][a-zA-Z0-9\-]{1,61}[a-zA-Z0-9]\.)+[a-zA-Z]{2,}$ ]]; then
    echo "This does not seem to be a plausible domain name."
    exit 1
fi
