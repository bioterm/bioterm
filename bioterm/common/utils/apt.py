import subprocess


def is_package_installed(package_name):
    """Check if a specific package is installed."""
    status = subprocess.run(
        ["dpkg", "-s", package_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return status.returncode == 0


def install_package(package_name):
    """Install an apt package using apt-get."""
    subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)
