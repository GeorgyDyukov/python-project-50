from gendiff_package.formatters.stylish import format_stylish
from gendiff_package.formatters.plain import format_plain
from gendiff_package.formatters.json import format_json


def choose_formatter(data, formatter='stylish'):
    if formatter == 'stylish':
        return format_stylish(data)
    elif formatter == 'plain':
        return format_plain(data)
    elif formatter == 'json':
        return format_json(data)
    else:
        raise ValueError('Unsupported formatter.')
