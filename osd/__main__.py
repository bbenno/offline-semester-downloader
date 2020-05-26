#!/usr/bin/env python3

from argparse import ArgumentParser
from . import __version__, __author__, __title__, __description__, app
from osd import *


def main():
    parser = ArgumentParser(description="OSD - Offline Semester Downloader")
    parser.add_argument('-v', '--version', action='version',
                        version='{author}\'s %(prog)s v{version}'.format(
                            author=__author__, version=__version__))
    parser.add_argument("url", help="url of vimp or zoom cloud", type=str)
    parser.add_argument('path', help="destination path", type=str)
    args = parser.parse_args()
    app.run(args.url, args.path)


if __name__ == "__main__":
    main()
