#!/usr/bin/env python3
from functools import lru_cache
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
assert PROJECT_ROOT.name == "gnew-coreutils", "incorrect project root"

# key=lang name
# value=(ext, source_path_from_langroot)
langs = {
    "go": (".go", "cmd"),
    "python": (".py", "gnew_coreutils"),
    "rust": (".rs", "src/bin"),
}

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


def src_url(language: str, cmd: str) -> str:
    """Always links to main"""
    ext, path = langs[language]
    if language == "go":
        return f"https://github.com/GDWR/gnew-coreutils/blob/main/{language}/{path}/{cmd}/main.go"
    else:
        return f"https://github.com/GDWR/gnew-coreutils/blob/main/{language}/{path}/{cmd}{ext}"

@lru_cache
def get_status(language: str, util: str) -> bool:
    """We are assuming all the languages have been built,
    so we can just check their `{lang}/build` has a file of that name."""
    ext, path = langs[lang]

    if language == "go":
        return (PROJECT_ROOT / language / path / util).exists()
    else:
        return (PROJECT_ROOT / language / path / f"{util}{ext}").exists()

def create_rst(language: str) -> None:
    with open(f"./source/{language}/implemented.rst", "w") as f:
        implemented_count = sum(get_status(language, u) for u in utils)
        f.write(f"Implemented: {implemented_count}/{len(utils)}\n\n")

        f.write(
            ".. list-table::\n\n"
            "  * - Command\n"
            "    - Implemented\n\n"
        )

        for u in utils:
            f.write(f"  * - `{u} <{get_webpage(u)}>`_\n")

            if get_status(language, u):
                f.write(f"    - ✅ `src <{src_url(language, u)}>`_\n\n")
            else:
                f.write("    - ❌\n\n")


if __name__ == "__main__":
    for lang in langs:
        create_rst(lang)
