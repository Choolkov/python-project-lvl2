"""Script for gendiff."""
import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.',
)
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f', '--format', metavar='FORMAT', help='set format of output',
)
args = parser.parse_args()


def main():
    """Make pass."""


if __name__ == '__main__':
    main()
