import json
import yaml


def parser_file(file_path):
    """
    The function parses a file located at the specified file path
    and returns its contents as a dictionary.
    It supports files in JSON (.json) and YAML (.yaml or .yml) formats.

    Args:
        file_path (str): The path to the file to be parsed.

    Returns:
        dict: The contents of the file as a dictionary.

    Raises:
        ValueError: If the file format is not supported.
    """
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise ValueError('Unsupported file format.')
