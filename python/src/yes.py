#!/usr/bin/env python3
from argparse import ArgumentParser

parser = ArgumentParser(description="Repeatedly output a line with all specified STRING(s), or 'y'.")
parser.add_argument('string', type=str, nargs="...")

args = parser.parse_args()

message = ' '.join(args.string) or "y"
while True:
    print(message)
