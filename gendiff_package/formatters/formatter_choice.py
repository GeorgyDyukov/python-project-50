from gendiff_package.formatters.stylish import format_stylish


def choose_formatter(data, formatter='stylish'):
    if formatter == 'stylish':
        return format_stylish(data)
    else:
        raise ValueError('Unsupported formatter.')
