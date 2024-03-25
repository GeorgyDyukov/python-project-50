from gendiff_package.parser import parser_file
from gendiff_package.comparer import compare_data
from gendiff_package.formatters.formatter_choice import choose_formatter


def generate_diff(file_path_1, file_path_2, formatter='stylish'):
    """
    The function reads the content of two configuration files,
    compares their content, and generates a difference representation.
    The comparison result is then formatted using the specified formatter.

    Args:
        file_path_1 (str): The path to the first configuration file.
        file_path_2 (str): The path to the second configuration file.
        formatter (str): Optional. Specifies the format of the output.
            Available options: 'stylish' (default), 'plain', 'json'.

    Returns:
        str: The generated difference between two configuration files.
    """
    data1 = parser_file(file_path_1)
    data2 = parser_file(file_path_2)
    comparison = compare_data(data1, data2)
    result = choose_formatter(comparison, formatter)
    return result
