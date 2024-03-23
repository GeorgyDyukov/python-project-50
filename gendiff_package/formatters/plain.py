def format_plain(dct, path=''):
    str_lst = []
    for key, val in sorted(dct.items()):
        value = get_value(val)
        status = get_status(val)
        current_path = path + key
        message = create_status_message(status, current_path, value)
        if message is not None:
            str_lst.append(message)
    return '\n'.join(str_lst)


def get_value(data):
    return data['value']


def get_status(data):
    return data['status']


def create_status_message(status, path, value):
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
            f"From {edit_value(value['old'])} to {edit_value(value['new'])}"
        )
    return message


def edit_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    return edit_string(str(value))


def edit_string(string):
    if string in ('True', 'False', 'None'):
        string = string.replace('True', 'true')
        string = string.replace('False', 'false')
        string = string.replace('None', 'null')
        return string
    return f"'{string}'"
