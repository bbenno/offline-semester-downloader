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
import os.path
from . import downloader


_expected_ext = "mp4"

def setup_logging():
    """Configure logging."""
    logging.basicConfig(
        format="[%(levelname).1s] %(message)s", level=logging.DEBUG
    )


def run(urls: str, path: str, verbose_mode: bool = False):
    """Main function

    - set up logging
    """
    assert urls and path
    ext = os.path.splitext(path)[1].strip()
    if ext and ext != _expected_ext:
        logging.warn("Expected the file extension to be '%s'", _expected_ext)

    setup_logging()

    generator = _filename_generator(path)

    for url in urls:
        filename = next(generator)
        logging.debug("Download to '%s' from '%s'", filename, url)
        if not verbose_mode:
            downloader.download(url, filename)

def _filename_generator(path: str) -> str:
    """Generate valid, unique filenames with consistent file extension.

    :param path: The directory or file path where giving the pattern for
    generated filepaths
    :type path: str

    :return: valid, unique filename
    :rtype: str
    """
    count = 0
    filepath, ext = os.path.splitext(path)
    dirname, filename = os.path.split(path)
    if not filename.strip():
        filepath = os.path.join(filepath, "out_")
        ext = "mp4"
    while True:
        yield (filepath +  f"{count}" + ext)
        count += 1


def debug():
    pass
