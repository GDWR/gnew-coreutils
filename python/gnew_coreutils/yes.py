#!/usr/bin/env python3
import sys
from typing import NoReturn


def yes(string: str = "y", stdout=sys.stdout) -> NoReturn:
    """Repeatedly output a line with all specified STRING(s), or 'y'."""
    while True:
        print(string, file=stdout)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description=yes.__doc__
    )
    parser.add_argument('string', type=str, nargs="...")
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    yes(' '.join(args.string) or "y")
