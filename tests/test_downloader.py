#!/usr/bin/env python3

from src.downloader import ZoomDownloader


class TestZoomDownloader:
    def test_download(self, tmp_path):
        file_path = tmp_path / "a.mp4"
        zd = ZoomDownloader()
        url = os.getenv('ZOOM_CLOUD_TEST_URL')
        assert url
        zd.download(url, file_path)
        assert file_path.is_file()
