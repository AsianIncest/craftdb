from config import *
import utils
import logging
from bs4 import BeautifulSoup

if DEBUG:
    # выставляем уровень логирования
    logging.basicConfig(level=logging.DEBUG)
    logging.info(f"[{__file__}]")

html = utils.get_html(MCTOP_MAIN_URL).text
soup = BeautifulSoup(html, 'lxml')

# получаем блок с пагинацией
pagination = soup.find('ul', class_='pagination')
# получаем список
lis = pagination.find_all('li')
# фильтр лишнего
lis = lis[2:-1]
links = []
links.append(MCTOP_MAIN_URL)
for i in lis:
    # если сайт поменяется надо переделать!
    q1 = str(i).find('"') + 1
    q2 = str(i).find('"', q1)
    url = str(i)[q1+1:q2]
    links.append(MCTOP_MAIN_URL + url)
file = open(MCTOP_PAGES_LINKS_FILE, 'w')
file.write("\n".join(links))
file.close()
