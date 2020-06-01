#!/usr/bin/env python3

from argparse import ArgumentParser
from . import __version__, __author__, __title__, __description__, app


def main():
    parser = ArgumentParser(description=__description__)
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="{author}'s {prog}  v{version}".format(
            author=__author__, prog=__title__, version=__version__
        ),
    )
    parser.add_argument(
        "-u",
        "--urls",
        required=True,
        metavar="url",
        help="video source urls",
        nargs="+",
        type=str
    )
    parser.add_argument(
        "-l", "--log", help="log level", action="count", default=0
    )
    parser.add_argument("path", help="destination path", type=str)
    args = parser.parse_args()
    app.run(args.urls, args.path)


if __name__ == "__main__":
    main()
