import json

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


def compare_file_contents(data_1, data_2):
    key_set = set(data_1) | set(data_2)
    result = ''
    for key in sorted(key_set):
        if key in data_1 and key not in data_2:
            result += f"  - {key}: {data_1[key]}\n"
        elif key not in data_1 and key in data_2:
            result += f"  + {key}: {data_2[key]}\n"
        else:
            if data_1[key] == data_2[key]:
                result += f"    {key}: {data_1[key]}\n"
            else:
                result += f"  - {key}: {data_1[key]}\n"
                result += f"  + {key}: {data_2[key]}\n"
    return result


def edit_string(string):
    new_string = string.replace('True', 'true')
    new_string = new_string.replace('False', 'false')
    new_string = new_string.replace('None', 'null')
    result = '{\n' + new_string + '}'
    return result


def generate_diff(file_path_1, file_path_2):
    data1 = read_file(file_path_1)
    data2 = read_file(file_path_2)
    comparison = compare_file_contents(data1, data2)
    result = edit_string(comparison)
    return result
