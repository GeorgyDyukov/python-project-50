#!/usr/bin/env python3
from gendiff import parse_arguments
from gendiff import generate_diff


def main():
    """
    Main function for generating a difference between two files.

    The function parses command-line arguments, generates a difference
    between the content of two specified files, and prints the result.

    Arguments:
        None

    Returns:
        None
    """
    args = parse_arguments()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()
