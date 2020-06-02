#!/usr/bin/env python3

import os
import os.path
import pytest
import osd.app


def test_generator_creation(tmpdir):
    filename = tmpdir.join("a.file")
    generator = osd.app._filename_generator(filename)
    assert generator


@pytest.fixture(params=["a.file", "file", ""])
def filenames(tmpdir, request):
    count = 5
    filename = tmpdir.join(request.param)
    generator = osd.app._filename_generator(filename)
    return [next(generator) for i in range(count)]


def test_file_unique_name(filenames: list):
    # expect each filename to be unique
    assert len(set(filenames)) == len(filenames)


def test_file_same_ext(filenames: list):
    # expect each filename to have same extension
    assert len({os.path.splitext(path)[1] for path in filenames}) == 1


def test_generated_files_valid(filenames):
    # expect each generated filename to be valid
    assert all(
        [
            os.path.exists(f) or os.access(os.path.dirname(f), os.W_OK)
            for f in filenames
        ]
    )
