import os
import subprocess


def is_docker_source_added():
    # Paths to check
    sources_list = "/etc/apt/sources.list"
    sources_list_d = "/etc/apt/sources.list.d/"

    # Search for Docker CE source in sources.list
    if os.path.exists(sources_list):
        with open(sources_list, "r") as file:
            if any("docker" in line for line in file):
                return True

    # Search for Docker CE source in files inside sources.list.d
    if os.path.isdir(sources_list_d):
        for filename in os.listdir(sources_list_d):
            file_path = os.path.join(sources_list_d, filename)
            with open(file_path, "r") as file:
                if any("docker" in line for line in file):
                    return True

    return False


def install_docker_sources():
    try:
        # Update apt and install required packages
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(
            ["sudo", "apt", "install", "ca-certificates", "curl", "gnupg"], check=True
        )

        # Create keyrings directory
        subprocess.run(
            ["sudo", "install", "-m", "0755", "-d", "/etc/apt/keyrings"], check=True
        )

        # Add Docker's official GPG key
        subprocess.run(
            (
                "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | "
                "sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg"
            ),
            shell=True,
            check=True,
        )
        subprocess.run(
            ["sudo", "chmod", "a+r", "/etc/apt/keyrings/docker.gpg"], check=True
        )

        # Add the Docker repository to Apt sources
        architecture = (
            subprocess.check_output(["dpkg", "--print-architecture"]).decode().strip()
        )
        version_codename = (
            subprocess.check_output(
                '. /etc/os-release && echo "$VERSION_CODENAME"', shell=True
            )
            .decode()
            .strip()
        )
        docker_list_content = (
            f"deb [arch={architecture} "
            f"signed-by=/etc/apt/keyrings/docker.gpg] "
            f"https://download.docker.com/linux/ubuntu "
            f"{version_codename} stable"
        )
        with open("/etc/apt/sources.list.d/docker.list", "w") as f:
            f.write(docker_list_content)
        subprocess.run(
            ["sudo", "tee", "/etc/apt/sources.list.d/docker.list"],
            input=docker_list_content.encode(),
            check=True,
        )

        # Update apt again
        subprocess.run(["sudo", "apt", "update"], check=True)

        print("Docker sources installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def does_docker_network_exist(network_name):
    try:
        # List all Docker networks
        result = subprocess.check_output(["sudo", "docker", "network", "ls"]).decode()
        # Check if the specified network is in the list
        return network_name in result
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while checking Docker networks: {e}")
        return False


def create_docker_network(network_name):
    try:
        # Create the Docker network
        subprocess.run(
            ["sudo", "docker", "network", "create", "-d", "bridge", network_name],
            check=True,
        )
        print(f"Docker network '{network_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the Docker network: {e}")
