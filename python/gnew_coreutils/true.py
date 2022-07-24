from typing import NoReturn


def true() -> NoReturn:
    """Exit with a status code indicating success."""
    exit(0)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description=true.__doc__
    )
    parser.add_argument('string', type=str, nargs="...")
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    true()
