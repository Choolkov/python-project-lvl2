"""Script for gendiff."""
import argparse
import pathlib

from gendiff.gendiff import generate_diff

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.',
)
parser.add_argument('first_file', type=pathlib.Path)
parser.add_argument('second_file', type=pathlib.Path)
parser.add_argument(
    '-f',
    '--format',
    metavar='FORMAT',
    help='set format of output',
    choices=['stylish', 'plain'],
    default='stylish'
)
args = parser.parse_args()


def main():
    """Print the difference between two flat json files."""
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
