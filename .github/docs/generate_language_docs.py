#!/usr/bin/env python3
from functools import lru_cache
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
langs = ["go", "python", "rust"]
utils = [
    "b2sum", "base32", "base64", "basename", "basenc", "cat", "chcon", "chgrp", "chmod", "chroot", "cksum", "comm", "cp", "csplit", "cut", "date", "dd",
    "df", "dir", "dircolors", "dirname", "dirname", "du", "echo", "env", "expand", "expr", "factor", "false", "fmt", "fold", "head", "hostid", "id",
    "install", "join", "link", "ln", "logname", "ls", "md5sum", "mkdir", "mkfifo", "mknod", "mktemp", "mv", "nice", "nl", "nohup", "nproc", "numfmt", "od",
    "paste", "pathchk", "pinky", "pr", "printenv", "printf", "ptx", "pwd", "readlink", "realpath", "rm", "rmdir", "runcon", "seq", "sha1sum", "sha224sum",
    "sha256sum", "sha384sum", "sha512sum", "shred", "shuf", "sleep", "sort", "split", "stat", "stdbuf", "stty", "sum", "sync", "tac", "tail", "tee",
    "test", "timeout", "touch", "tr", "true", "truncate", "tsort", "tty", "uname", "unexpand", "uniq", "unlink", "users", "vdir", "wc", "who", "whoami", "yes"
]


def get_webpage(cmd: str) -> str:
    """Using archlinux man pages"""
    return f"https://man.archlinux.org/man/core/coreutils/{cmd}.1.en"


@lru_cache
def get_status(language: str, util: str) -> bool:
    """We are assuming all the languages have been built,
    so we can just check their `{lang}/build` has a file of that name."""
    return (PROJECT_ROOT / language / "build" / util).exists()


def create_rst(language: str) -> None:
    """Broken into 2 tables due to size"""

    with open(f"./langs/{language}.rst", "w") as f:

        implemented_count = sum(get_status(language, u) for u in utils)
        f.write(f"Implemented: {implemented_count}/{len(utils)}\n\n")

        def _generate_table(cmds: list[str]) -> None:
            f.write(".. list-table::\n\n")
            f.write(f"  * - Command\n")
            for c in cmds:
                f.write(f"    - `{c} <{get_webpage(c)}>`_\n")
            f.write("\n")

            f.write(f"  * - Implemented\n")
            for c in cmds:
                f.write(f"    - {'✅' if get_status(language, c) else '❌'}\n")
            f.write("\n")

        _generate_table(utils[:50])
        _generate_table(utils[50:])


if __name__ == "__main__":
    for lang in langs:
        create_rst(lang)
