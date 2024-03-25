from gendiff_package.formatters.stylish import format_stylish
from gendiff_package.formatters.plain import format_plain
from gendiff_package.formatters.json import format_json


def choose_formatter(data, formatter='stylish'):
    """
    This function selects the appropriate formatter based on the
    specified 'formatter' parameter and transforms the provided data
    into the corresponding format.

    Args:
        data: The data to be formatted.
        formatter (str): Optional. Specifies the formatter to use.
            Available options: 'stylish' (default), 'plain', 'json'.

    Returns:
        The formatted data according to the chosen formatter.

    If the 'formatter' parameter is not supported, the function raises
    a ValueError.
    """
    formatters = {
        'stylish': format_stylish,
        'plain': format_plain,
        'json': format_json,
    }
    if formatter not in formatters:
        raise ValueError('Unsupported formatter.')
    return formatters[formatter](data)
