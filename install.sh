#!/bin/bash

# Check for Python 3 and get its version
PYTHON_VERSION=$(python3 --version)
if [[ $PYTHON_VERSION == '' ]]; then
    echo "Python 3 is not installed. Please install it first."
    exit 1
fi

echo "Using system's Python version: $PYTHON_VERSION"

# Install pip if it is not already installed
PIP_VERSION=$(pip --version)
if [[ $PIP_VERSION == '' ]]; then
    echo "Installing pip..."
    sudo apt update
    sudo apt install -y python3-pip
fi

# Install virtualenv
echo "Installing virtualenv..."
sudo pip install virtualenv

# Create a virtual environment named '.biotermInstallVenv' in the current directory
echo "Creating virtual environment..."
virtualenv -p python3 .biotermInstallVenv

# Activate the virtual environment
source .biotermInstallVenv/bin/activate

# Check if requirements_install.txt exists
if [ ! -f requirements_install.txt ]; then
    echo "requirements_install.txt not found, exiting."
    exit 1
fi

# Install packages within the virtual environment from requirements.txt
echo "Installing packages from requirements_install.txt in the virtual environment..."
pip install -r requirements_install.txt

# Deactivate the virtual environment
deactivate

# Full path to the Python interpreter in the virtual environment
VENV_PYTHON=".biotermInstallVenv/bin/python"

# Call the install script with sudo and the virtual environment's Python
sudo $VENV_PYTHON install.py

# Make install log readable
if [ -f server_installation.log ]; then
    chmod 440 server_installation.log
fi

# Cleanup
rm -rf .biotermInstallVenv
