import itertools


def format_stylish(dct, depth=0, symbol=' ', num_symbols=4):
    indent = (symbol * num_symbols) * depth
    str_lst = []
    for key, val in sorted(dct.items()):
        value = get_value(val)
        status = get_status(val)
        indent_add = f"{indent}  + {key}"
        indent_del = f"{indent}  - {key}"
        indent_unchanged = f"{indent}    {key}"

        if status == 'added':
            string = f"{indent_add}: {edit_value(value, depth + 1)}"
        elif status == 'deleted':
            string = f"{indent_del}: {edit_value(value, depth + 1)}"
        elif status == 'changed':
            str_1 = f"{indent_del}: {edit_value(value['old value'], depth + 1)}"
            str_2 = f"{indent_add}: {edit_value(value['new value'], depth + 1)}"
            string = f"{str_1}\n{str_2}"
        else:
            string = f"{indent_unchanged}: {edit_value(value, depth + 1)}"

        str_lst.append(string)
    result = itertools.chain("{", str_lst, [indent + "}"])
    return '\n'.join(result)


def get_value(data):
    if isinstance(data, dict):
        return data.get('value', data)
    return data


def get_status(data):
    if isinstance(data, dict):
        return data.get('status', None)
    return None


def edit_value(value, depth):
    if isinstance(value, dict):
        return format_stylish(value, depth)
    return edit_string(str(value))


def edit_string(string):
    replacements = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }
    if string in replacements:
        return replacements[string]
    return string
