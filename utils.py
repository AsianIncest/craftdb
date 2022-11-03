import datetime

import requests
from config import *
import os

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': AGENT,
    }
)


def get_html(url):
    return requests.get(url, headers=headers)

def down_and_save(url, path):
    pass
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
        if delta >= timeout:
            return down_and_save(url, path)
        else:
            return open(path).read()
    elif dir_exists and not file_exists:
        return down_and_save(url, path)
    else:
        os.mkdir(folder)
        return down_and_save(url, path)
