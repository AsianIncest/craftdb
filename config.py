#урл главной страницы
MCTOP_MAIN_URL = 'https://mctop.su/'
#user agent чтобы сайт особо не палил
AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
#вывод кучи инфы во время работы
DEBUG = True
#файлик со списком всех страниц в рейтинге (примерно 9)
MCTOP_PAGES_LINKS_FILE = 'mctop_pages_links.txt'
#файлик со ссылками на все странички серверов в рейтинге (было 256)
MCTOP_PROJECTS_PAGES_FILE = 'mctop_projects_pages_links.txt'
#кеш страниц рейтинга
MCTOP_PAGES_CACHE = "mctop_pages_cache"
#время в секундах жизни кеша
#ЗЫ - чтобы постоянно во время отладки не перекачивать
MCTOP_PAGES_CACHE_TIMEOUT = 999
#аналогично для страниц проектов
MCTOP_PROJECTS_CACHE = "mctop_projects_cache"
MCTOP_PROJECTS_CACHE_TIMEOUT = 999