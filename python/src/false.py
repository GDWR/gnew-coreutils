from argparse import ArgumentParser

parser = ArgumentParser(description="Exit with a status code indicating failure.")
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

exit(1)
