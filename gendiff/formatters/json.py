import json


def format_json(data):
    """
    The function takes input data and formats it into a JSON string.

    Args:
        data: Data to be formatted.

    Returns:
        str: JSON-formatted string representing the provided data.
    """
    return json.dumps(data, indent=4)
