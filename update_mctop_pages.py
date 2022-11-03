import os
import datetime
import shutil
import logging
import utils


from config import *


def how_many_seconds(file):
    # получпем дату изменения файла
    last_update = os.path.getmtime(file)
    last_update = datetime.datetime.fromtimestamp(last_update)

    # вычисляем сколько прошло секунд
    delta = datetime.datetime.now() - last_update
    return delta.seconds

def update():
    if os.path.exists(MCTOP_PAGES_CACHE):
        shutil.rmtree(MCTOP_PAGES_CACHE)
        os.mkdir(MCTOP_PAGES_CACHE)
    else:
        os.mkdir(MCTOP_PAGES_CACHE)
    pages_links = None
    with open(MCTOP_PAGES_LINKS_FILE) as f:
        pages_links = f.read().split("\n")
    pn = 1 #page number
    for url in pages_links:
        html = utils.get_html(url).text
        if DEBUG:
            html = f"{url}\n" + html
        file_path = os.path.join(MCTOP_PAGES_CACHE, f"page_{pn}.html")
        file = open(file_path, "w")
        file.write(html)
        file.close()
        pn += 1

if DEBUG:
    # выставляем уровень логирования
    logging.basicConfig(level=logging.DEBUG)
    logging.info("[{__file__}]")

NEED_UPDATE = False
WORK_DIR_EXISTS = os.path.exists(MCTOP_PAGES_CACHE)
if not WORK_DIR_EXISTS:
    logging.info(f"[{__file__}] create dir {MCTOP_PAGES_CACHE}")
    NEED_UPDATE = True

# смотрим даты файлов, если устарели ставим флаг
if WORK_DIR_EXISTS:
    with os.scandir(MCTOP_PAGES_CACHE) as dir:
        for f in dir:
            # печать всех записей, являющихся файлами
            if f.is_file():
                file = os.path.join(MCTOP_PAGES_CACHE, f.name)
                lu = how_many_seconds(file)
                if lu > MCTOP_PAGES_CACHE_TIMEOUT:
                    logging.info(f"[{__file__}] {file} is expired.. need update")
                    NEED_UPDATE = True
                    break

if NEED_UPDATE:
    update()
    logging.info(f"[{__file__}] updates complete")
else:
    logging.info(f"[{__file__}] updates not need")

