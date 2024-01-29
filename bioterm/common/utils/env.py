import os


def check_existing_env_files(locations: dict):
    """Check for existing .env files in the specified locations."""
    for location_name, location_path in locations.items():
        env_path = os.path.join(location_path, ".env")
        if os.path.isfile(env_path):
            return True, location_name
    return False, None


def write_env_file(file_path: str, env_vars: dict, vars_to_quote: set):
    """
    Write an .env file to the specified location with quotes around specified variables.

    Parameters:
    file_path (str): Path to the .env file to be written.
    env_vars (dict): Dictionary containing the environment variables.
    vars_to_quote (set): Set of variable names that should be enclosed in quotes.
    """
    try:
        with open(file_path, "w") as file:
            for key, value in env_vars.items():
                # Check if the variable should be quoted
                if key in vars_to_quote:
                    file.write(f'{key}="{value}"\n')
                else:
                    file.write(f"{key}={value}\n")
        print(f".env file written successfully to {file_path}")
    except IOError as e:
        print(f"Error writing .env file: {e}")
