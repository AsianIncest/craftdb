from config import *
import os
import logging
from bs4 import BeautifulSoup


def get_files():
    html_file_path = []
    with os.scandir(MCTOP_PAGES_CACHE) as dir:
        for f in dir:
            # печать всех записей, являющихся файлами
            if f.is_file():
                file = os.path.join(MCTOP_PAGES_CACHE, f.name)
                html_file_path.append(file)
    return html_file_path

def get_projects_links(filename):
    html = open(filename).read()
    soup = BeautifulSoup(html, 'lxml')
    main_table = soup.find('section', {
        "class": "server-rt-cards"})
    servers_rows = main_table.find_all('article', {
        "class": "user-pr-card"})
    res = []
    for row in servers_rows:
        rate_number = row.find("div", {
            "class": "user-pr-card__num"
        })
        rate_number = rate_number.text

        link = row.find("div", {
            "class": "user-pr-card__h"
        }).find("a").attrs['href']

        link = MCTOP_MAIN_URL + link[1:]
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #тут может быть отвал, если rate_number не преобразуется в int
        res.append((int(rate_number), link))
    return res



if DEBUG:
    # выставляем уровень логирования
    logging.basicConfig(level=logging.DEBUG)
    logging.info(f"[{__file__}]")

result = []
for f in get_files():
    result = result + get_projects_links(f)
#хитровыебанная сортировка по 0 столбцу
#понятия не имею, но работает
result = sorted(result, key=lambda r: r[0])

with open(MCTOP_PROJECTS_PAGES_FILE, 'w') as f:
    txt = ""
    for i in result:
        logging.debug(f"#{i[0]}={i[1]}")
        txt = txt + f"{i[0]}:{i[1]}\n"
    #тут срез чтобы не вставлять последний перевод строки)
    f.write(txt[:-len("\n")])
logging.info(f"file saved {MCTOP_PROJECTS_PAGES_FILE}")