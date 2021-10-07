#! /usr/bin/env python3

import re
from subprocess import run
from sys import argv, exit


def branches_list():
    return run(
        ["git", "--no-pager", "branch", "--list"], capture_output=True, text=True
    ).stdout


def next_branch(branch_name):
    p = f"{branch_name}(?:-(\\w))?"
    matches = re.findall(p, branches_list())
    if len(matches) == 0:
        return branch_name
    if len(matches) == 1 and matches[0] == "":
        return f"{branch_name}-b"
    return f"{branch_name}-{chr(ord(matches[-1]) + 1)}"


def main():
    if len(argv) != 2:
        print("Please supply a branch name")
        exit(1)
    branch_name = argv[1]
    run(["git", "switch", "develop"])
    run(["git", "pull", "origin", "develop"])
    run(["git", "switch", "-c", next_branch(branch_name)])
    exit(0)


if __name__ == "__main__":
    main()
