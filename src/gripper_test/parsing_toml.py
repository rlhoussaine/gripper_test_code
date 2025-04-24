import os
import tomllib


def find_project_root(marker='.git'):
    """
    Find the root of the project by looking for a specific marker (default is '.git').

    :param marker: Name of the marker to look for (default is '.git')
    :return: Path to the project root
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != os.path.dirname(current_dir):  # Traverse up to the filesystem root
        if marker in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    raise FileNotFoundError(f"The marker '{marker}' was not found in the parent directories.")

def parse_toml_file(file_name, config_dir='config'):
    """
    Parse a TOML file and return the data as a dictionary.

    :param file_name: Name of the TOML file (without the path)
    :param config_dir: Directory containing the configuration files (default is 'config')
    :return: Dictionary containing the parsed data
    """
    try:
        project_root = find_project_root()
        file_path = os.path.join(project_root, config_dir, file_name)

        with open(file_path, 'rb') as f:
            data = tomllib.load(f)
        return data
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None