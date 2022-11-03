import os
from utils import *

def get_files_list():
    l = []
    with os.scandir(MCTOP_PROJECTS_CACHE) as dir:
        for f in dir:
            # печать всех записей, являющихся файлами
            if f.is_file():
                file = os.path.join(MCTOP_PROJECTS_CACHE, f.name)
                l.append(file)
    return sorted(l)
print(get_files_list())