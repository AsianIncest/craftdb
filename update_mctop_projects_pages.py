from utils import *

if DEBUG:
    # выставляем уровень логирования
    logging.basicConfig(level=logging.DEBUG)
    logging.info(f"[{__file__}]")

links = open(MCTOP_PROJECTS_PAGES_FILE).readlines()
links = [l.replace("\n", "").split(';') for l in links]
for link in links:
    n = link[0]
    url = link[1]
    file = f"{n.zfill(3)}_{url_to_id(url)}.html"
    logging.info(f"{url} --> {file}")
    cache(url, MCTOP_PROJECTS_CACHE, file, timeout=MCTOP_PROJECTS_CACHE_TIMEOUT)