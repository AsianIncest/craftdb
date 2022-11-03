import requests
from config import AGENT

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': AGENT,
    }
)


def get_html(url):
    return requests.get(url, headers=headers)

