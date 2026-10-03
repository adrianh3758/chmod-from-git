"""Chmod from Git — Show files in a git repo whose executable bit disagrees with the index."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='chmod_from_git',
        description='Show files in a git repo whose executable bit disagrees with the index.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Chmod from Git')
    print('Catch +x drift on Windows checkouts.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
