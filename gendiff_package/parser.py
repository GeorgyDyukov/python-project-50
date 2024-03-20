import json
import yaml


def parser_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    else:
        raise ValueError('Unsupported file format.')
