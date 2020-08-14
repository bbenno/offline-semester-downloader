#!/usr/bin/env python3

"""Regular expression patterns used by downloaders."""

SRC_URL_VIMP = (
    r'(?<=src=")(https?:\/\/)?vimp\.(oth-regensburg|othr)\.de'
    r'(/[\w_\-]*)*(?=(\?[^"]*?)?")'
)
"""Pattern describing the HTML-content referencing the video url of a
video stored on vimp.oth-regensburg.de (`str`).
"""

SRC_URL_ZOOM = (
    r'(?<=src=")https?:\/\/(?P<domain>[\da-z\.-]+\.)?zoom\.'
    r'(?P=domain)?([a-z\.]{2,6})[\/\w \.-]+\.mp4.*?(?=")'
)
"""Regex-pattern describing the source adress of a lecture provided from Zoom
cloud that is embedded as video-src in HTML page (`str`).
"""

URL_BASIC = r"(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?"
"""Basic pattern describing an url (`str`).
"""

GRIPS_USER = r"^([a-z]){3}\d{5}$"
"""Pattern of user naming at GRIPS (`str`).
"""

DOMAIN_ZOOM = r"(https?:\/\/)?oth-regensburg\.zoom\.(us|de)"
"""Domain of zoom platform (`str`).
"""

DOMAIN_VIMP = r"(https?:\/\/)?vimp\.(oth-regensburg|othr|hs-regensburg)\.de"
"""Domain of vimp platform (`str`).
"""

DOMAIN_GRIPS = r"(https?:\/\/)?elearning\.(uni-regensburg|ur)\.de"
""" Domain of GRIPS platform (`str`).
"""
