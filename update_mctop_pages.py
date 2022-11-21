#2
import os
import datetime
import shutil
import logging
import utils


from config import *


def how_many_seconds(file):
    # получаем дату изменения файла
    last_update = os.path.getmtime(file)
    last_update = datetime.datetime.fromtimestamp(last_update)

    # вычисляем сколько прошло секунд
    delta = datetime.datetime.now() - last_update
    return delta.seconds

def update():
    pages_links = None
    if not os.path.exists(MCTOP_PAGES_LINKS_FILE):
        logging.error(f"No file ({MCTOP_PAGES_LINKS_FILE}), please run update_mctop_pages.py")

    with open(MCTOP_PAGES_LINKS_FILE) as f:
        pages_links = f.read().split("\n")
    pn = 1 #page number
    for url in pages_links:
        utils.cache(url, MCTOP_PAGES_CACHE, f"page_{pn}.html")
        pn += 1

if DEBUG:
    # выставляем уровень логирования
    logging.basicConfig(level=logging.DEBUG)
    logging.info("[{__file__}]")

update()

