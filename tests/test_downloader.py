#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from osd.downloader import _ZoomDownloader


class TestZoomDownloader:
    def test_download(self, tmp_path):
        load_dotenv()

        file_path = tmp_path / "a.mp4"
        zd = _ZoomDownloader()
        url = os.getenv("ZOOM_CLOUD_TEST_URL")
        assert url
        zd.download(url, file_path)
        assert file_path.is_file()
