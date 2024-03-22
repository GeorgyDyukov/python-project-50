import itertools


def format_stylish(dct, depth=0, symbol=' ', num_symbols=4):
    indent = (symbol * num_symbols) * depth
    str_lst = []
    for key, val in sorted(dct.items()):
        if isinstance(val, dict):
            value = val.get('value', val)
            status = val.get('status', None)
        else:
            value = val
            status = None

        if status == 'added':
            string = f"{indent}  + {key}: {edit_value(value, depth + 1)}"
        elif status == 'deleted':
            string = f"{indent}  - {key}: {edit_value(value, depth + 1)}"
        elif status == 'changed':
            str_1 = f"{indent}  - {key}: {edit_value(value['old'], depth + 1)}"
            str_2 = f"{indent}  + {key}: {edit_value(value['new'], depth + 1)}"
            string = f"{str_1}\n{str_2}"
        else:
            string = f"{indent}    {key}: {edit_value(value, depth + 1)}"

        str_lst.append(string)
    result = itertools.chain("{", str_lst, [indent + "}"])
    return '\n'.join(result)


def edit_value(value, depth):
    if isinstance(value, dict):
        string = format_stylish(value, depth)
    else:
        string = edit_string(str(value))
    return string


def edit_string(string):
    new_string = string.replace('True', 'true')
    new_string = new_string.replace('False', 'false')
    new_string = new_string.replace('None', 'null')
    return new_string
