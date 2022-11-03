import datetime
import logging
import requests
from config import *
import os

if DEBUG:
    # выставляем уровень логирования
    logging.basicConfig(level=logging.DEBUG)


headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': AGENT,
    }
)


def get_html(url):
    return requests.get(url, headers=headers)

def down_and_save(url, path):
    html = requests.get(url, headers=headers).text
    with open(path, 'w') as f:
        f.write(html)
    return html

def cache(url, folder, file, timeout=DEFAULT_TIMEOUT, html=""):
    '''файловый кеш'''
    dir_exists = os.path.exists(folder)
    path = os.path.join(folder, file)
    file_exists = os.path.exists(path)
    if dir_exists and file_exists:
        last_update = os.path.getmtime(path)
        last_update = datetime.datetime.fromtimestamp(last_update)
        # вычисляем сколько прошло секунд
        delta = datetime.datetime.now() - last_update
        delta = delta.seconds
        if delta >= timeout:
            logging.info(f"[{__file__}] down&save {url} -> {path}")
            return down_and_save(url, path)
        else:
            logging.info(f"[{__file__}] cached -> {path}]")
            return open(path).read()
    elif dir_exists and not file_exists:
        logging.info(f"[{__file__}] down&save {url} -> {path}")
        return down_and_save(url, path)
    else:
        os.mkdir(folder)
        logging.info(f"[{__file__}] down&save {url} -> {path}")
        return down_and_save(url, path)

def url_to_id(url):
    ''' in >> https://mctop.su/servers/4888/
        out >> 4888
    '''
    url = 'https://mctop.su/servers/4888/'
    spl = url.split('/')
    return spl[4]

