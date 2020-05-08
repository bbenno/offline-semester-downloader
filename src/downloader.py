#!/usr/bin/python3

""" """

import getpass
import re as regex
import os.path
import logging
from argparse import ArgumentParser
import requests
from tqdm import tqdm
from . import pattern

__author__ = "Benno Bielmeier"
__status__ = "instable"
__date__ = "2020-05-03"
__version__ = "0.1"


class GripsDownloader:
    '''
    Downloder instace that is capable of finding the video destination urls
    of a given course.
    '''

    _DOMAIN = 'elearning.uni-regensburg.de'
    _URL = f"https://{_DOMAIN}"
    _COURSE_URL = 'https://elearning.uni-regensburg.de/mod/url/view.php?id={}'

    def __init__(self):
        self.login_failed_pattern = regex.compile(r'Sie sich anmelden')
        self.session = requests.Session()
        self._login()
        self._test()

    def __del__(self):
        self._logout()

    def _logout(self):
        '''Logout and end session.'''
        logging.info("Logout")
        response = self.session.post(self._URL + '/login/logout.php')
        assert response.status_code == requests.codes.ok
        # TODO: remove cookie

    def _login(self, user: str = None, password: str = None) -> bool:
        if not user:
            user = input('User: ')
        assert Validator.validate_user(user)

        if not password:
            password = getpass.getpass()

        logging.info("Login as %s", user)

        response = self.session.post(
            self._URL,
            data=dict(realm='hs', username=user, password=password, anchor=''))

        assert response.status_code == requests.codes.ok
        assert self.session.cookies.get_dict(domain=self._DOMAIN)

        is_success = str(response.content).find('id="loginerrormessage"') == -1
        assert is_success
        return is_success

    def _test(self, text: str = None):
        if not text:
            text = self.session.get(self._URL).text
        if self.login_failed_pattern.search(text):
            raise Exception("nicht eingeloggt")

    def find_vimp_link(self, url: str):
        """Searching the lectures' video url, referenced by the course site in
        GRIPS.

        :param url: The URL of the course website in GRIPS
        :type url: str

        :raises Exception: Current Session not logged in

        :return: List of all video urls
        :rtype: list
        """
        response = self.session.get(url)
        self._test(response.text)

        matches = regex.findall(
            pattern.SRC_URL_VIMP, str(response.text), regex.I)
        return matches[0]

    def find_vimp_link_by_id(self, course_id: int) -> str:
        assert course_id >= 0
        self.find_vimp_link(self._COURSE_URL.format(course_id))


class VimpDownloader:

    def __init__(self):
        pass

    def download(self, url: str, path: str):
        pass


class ZoomDownloader:

    _HEADER = {'Referer': 'https://oth-regensburg.zoom.us'}

    def __init__(self):
        self.cookie = None
        self._chunk_size = 8192

    def _find_mp4_url(self, url: str) -> str:
        assert Validator.validate_url(url)

        response = requests.get(url)
        response.raise_for_status()

        if not self.cookie:
            logging.debug("Set required cookie")
            cookie_values = response.cookies.get_dict()
            assert cookie_values
            self.cookie = dict(_zm_ssid=cookie_values['_zm_ssid'])

        logging.info("Searching video source url")
        match = regex.search(pattern.SRC_URL_ZOOM, response.text)

        if not match:
            logging.error("No video url found")
            return None

        src_url = match[0]
        logging.debug("Found video source url: %s", src_url)
        return src_url

    def _download_file(self, url: str, path: str):
        with requests.get(
                url, cookies=self.cookie, headers=self._HEADER, stream=True
                ) as response:
            if response.status_code == requests.codes.ok:
                total_size = int(response.headers.get('content-length', 0))
                progress_bar = tqdm(
                    total=total_size, unit='iB', unit_scale=True)

                response.raise_for_status()
                with open(path, 'wb') as video_file:
                    for chunk in response.iter_content(
                            chunk_size=self._chunk_size):
                        progress_bar.update(len(chunk))
                        video_file.write(chunk)
                logging.debug("Successfully safed to %s", path)
            else:
                logging.error("Received HTTP Status %d", response.status_code)

    def download(self, url: str, path: str):
        assert Validator.validate_url(url)
        # validate path

        video_url = self._find_mp4_url(url)
        self._download_file(video_url, path)


class Validator:
    ''''Provides methods to verify certain string formats.'''

    _url = regex.compile(pattern.URL_BASIC)
    _user = regex.compile(pattern.GRIPS_USER)

    @classmethod
    def validate_url(cls, url: str) -> bool:
        '''Validates validity of given url.

        :param url: given url
        :type url: str
        :return: `True` if URL is valid; otherwise `False`
        :rtype: bool
        '''
        return cls._url.match(url)

    @classmethod
    def validate_user(cls, user: str) -> bool:
        '''Validates validity of given GRIPS username.

        :param user: the username
        :types user: str
        :return: `True` if URL is valid; otherwise `False`
        :rtype: bool
        '''
        return cls._user.match(user)

    @classmethod
    def validate_video_path(cls, path: str) -> bool:
        assert os.path.basename(path).endswith('.mp4')
        assert os.path.isdir(os.path.dirname(path))
        if os.path.isfile(path):
            logging.warning("file '%s' already existent.", path)


def download(url: str, path: str):
    '''Downloads the video lecture of a given page.

    :param url: The url of the page in which the video is embedded.
    :type url: str
    :param path: The destination path to safe the video.
    :type path: str
    '''
    if _zoom_matcher.match(url):
        zoom_d = ZoomDownloader()
        zoom_d.download(url, path)
    elif _vimp_matcher.match(url):
        pass
    elif _grips_matcher.match(url):
        grips_d = GripsDownloader()
        vimp = grips_d.find_vimp_link(url)
    else:
        logging.critical("Can not parse url '%s'", url)


_zoom_matcher = regex.compile(pattern.DOMAIN_ZOOM)
_grips_matcher = regex.compile(pattern.DOMAIN_GRIPS)
_vimp_matcher = regex.compile(pattern.DOMAIN_VIMP)


def main():
    '''Main function'''
    parser = ArgumentParser(description="Offline Semester Downloader.")
    parser.add_argument('-v', '--version', action='version',
                        version='{author}\'s %(prog)s v{version}'.format(
                            author=__author__, version=__version__))
    parser.add_argument("url", help="url of vimp or zoom cloud", type=str)
    parser.add_argument('path', help="destination path", type=str)
    args = parser.parse_args()

    logging.basicConfig(
        format='[%(levelname).1s] %(message)s', level=logging.DEBUG)

    download(args.url, args.path)


if __name__ == '__main__':
    main()
