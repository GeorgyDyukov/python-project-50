def format_plain(dct, path=''):
    """
    The function takes input data and formats it into a plain text format.

    Args:
        dct (dict): The dictionary containing data to be formatted.
        path (str): Optional. The path to the current item
            in the data structure.

    Returns:
        str: A string containing the formatted data in plain text.
    """
    str_lst = []
    for key, val in sorted(dct.items()):
        value = get_value(val)
        status = get_status(val)
        current_path = f"{path}{key}"
        message = create_status_message(status, current_path, value)
        if message:
            str_lst.append(message)
    return '\n'.join(str_lst)


def get_value(data):
    return data['value']


def get_status(data):
    return data['status']


def create_status_message(status, path, value):
    """
    The function creates a status message based on the provided status,
    path, and value.

    Args:
        status (str): The status of the property ('added', 'deleted',
            'unchanged', 'changed', 'changed, nested').
        path (str): The path to the current property in the data structure.
        value: The value of the property.

    Returns:
        str or None: The status message if applicable, otherwise None.
    """
    if status == 'added':
        message = f"Property '{path}' was added with value: {edit_value(value)}"
    elif status == 'deleted':
        message = f"Property '{path}' was removed"
    elif status == 'unchanged':
        message = None
    elif status == 'changed, nested':
        message = format_plain(value, f"{path}.")
    elif status == 'changed':
        message = (
            f"Property '{path}' was updated. "
            f"From {edit_value(value['old value'])} to "
            f"{edit_value(value['new value'])}"
        )
    return message


def edit_value(value):
    """
    The function edits the provided value for better representation.

    Args:
        value: The value to be edited.

    Returns:
        str: The edited value.
    """
    replacements = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }
    if isinstance(value, dict):
        return '[complex value]'
    elif str(value) in replacements:
        return replacements[str(value)]
    elif isinstance(value, int):
        return value
    return f"'{value}'"
