import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)

types = {'image/png'}

SEARCH_STRING = 'https://knotprot.cent.uw.edu.pl/browse/?raw=1&set=False&bridgeType=probab%2Ccov_ion&knotTypes=%2B31'
DOWNLOAD_LINK = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}.png'


def get_proteins(search_string):
    req = Request(search_string, method='GET')
    proteins = []
    with urlopen(req) as resp:
        data = resp.read().decode('utf-8')
        for line in data.splitlines():
            if len(line)>4 and not line.startswith('#'):
                cells = line.strip().split(';')
                proteins.append((cells[0],cells[1]))
    return proteins


def download_link(directory, protein):
    download_path = os.path.join(directory, os.path.basename('{0}_{1}.png'.format(protein[0],protein[1])))
    link = DOWNLOAD_LINK.format(protein[0], protein[1])
    with urlopen(link) as image, open(download_path, 'wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir

dir = setup_download_dir()
proteins = get_proteins(SEARCH_STRING)
for protein in proteins:
    download_link(dir, protein)


