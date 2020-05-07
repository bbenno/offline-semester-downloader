#!/usr/bin/python3

'''Regular expression patterns used by downloader'''

# ToDo: add ending "
SRC_URL_VIMP = (r'(?<=src=")(https?:\/\/)?vimp\.(oth-regensburg|othr)\.de'
                r'(/\w*)*)')
SRC_URL_ZOOM = (r'(?<=src=")https?:\/\/(?P<domain>[\da-z\.-]+\.)?zoom\.'
                r'(?P=domain)?([a-z\.]{2,6})[\/\w \.-]+\.mp4.*?(?=")')
URL_BASIC = r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?'
GRIPS_USER = r'^([a-z]){3}\d{5}$'
DOMAIN_ZOOM = r'(https?:\/\/)?oth-regensburg\.zoom\.(us|de)'
DOMAIN_VIMP = r'(https?:\/\/)?vimp\.(oth-regensburg|othr|hs-regensburg)\.de'
DOMAIN_GRIPS = r'(https?:\/\/)?elearning\.(uni-regensburg|ur)\.de'
