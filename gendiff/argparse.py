import argparse


def parse_arguments():
    """
    The function uses Python's argparse module to define and parse command-line
    arguments for comparing two configuration files. It allows users to specify
    two configuration files to compare and optionally specify the format of the
    output.

    Command-line Arguments:
        first_file (str): The path to the first configuration file to compare.
        second_file (str): The path to the second configuration file to compare.
        -f, --format (str): Optional. Specifies the format of the output.
            Available choices are 'stylish', 'plain', and 'json'.
            Default is 'stylish'.

    Returns:
        An object containing the parsed arguments, including:
            - first_file: The path to the first configuration file.
            - second_file: The path to the second configuration file.
            - format: The specified format for the output.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        "-f", "--format",
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help="set format of output",
    )
    args = parser.parse_args()
    return args
