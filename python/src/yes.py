#!/usr/bin/env python3
from argparse import ArgumentParser

parser = ArgumentParser(description="Repeatedly output a line with all specified STRING(s), or 'y'.")
parser.add_argument('string', type=str, nargs="...")
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

message = ' '.join(args.string) or "y"
while True:
    print(message)
