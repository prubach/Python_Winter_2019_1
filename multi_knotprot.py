import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)

types = {'image/png'}

SEARCH_STRING='https://knotprot.cent.uw.edu.pl/browse/?raw=1&set=False&bridgeType=probab%2Ccov_ion&knotTypes=%2B31'
'https://knotprot.cent.uw.edu.pl/static/knot_data/1j85/A/1j85_A.png'


def get_links(search_string):
    req = Request(search_string, method='GET')


    with urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    return [item['link'] for item in data['data'] if 'type' in item and item['type'] in types]


def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir