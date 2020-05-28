#!/usr/bin/env python3

"""OSD - Offline-Semester-Downloader - the solution for asynchronous education.

Copyright (c) 2020 Benno Bielmeier.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import logging
from . import downloader


def setup_logging():
    """Configure logging."""
    logging.basicConfig(
        format="[%(levelname).1s] %(message)s", level=logging.DEBUG
    )


def run(url: str, path: str):
    """Main function

    - set up logging
    """
    setup_logging()
    downloader.download(url, path)


def debug():
    pass
