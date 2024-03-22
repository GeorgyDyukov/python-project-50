from gendiff_package.parser import parser_file
from gendiff_package.comparer import compare_dicts
from gendiff_package.formatters.formatter_choice import choose_formatter


def generate_diff(file_path_1, file_path_2, formatter='stylish'):
    data1 = parser_file(file_path_1)
    data2 = parser_file(file_path_2)
    comparison = compare_dicts(data1, data2)
    result = choose_formatter(comparison, formatter)
    return result
