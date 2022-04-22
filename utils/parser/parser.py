import os

from data.settings import PARSING_URL
from data.warningLevel import WARNING_LEVEL
from utils.log import log

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip install -U lxml requests beautifulsoup4')
    import requests
    from bs4 import BeautifulSoup

def parse() -> list:
    url = PARSING_URL
    try:
        try:
            response = requests.get(url)
        except Exception:
            log(f'Unable to make request to {url}', WARNING_LEVEL['high'])

        soup = BeautifulSoup(response.text, 'lxml')
        jokes = soup.find_all('div', class_='text')

        parsed_jokes = []

        for joke in jokes:
            if joke.text != '':
                parsed_jokes.append(joke.text)
    except Exception:
        log(f'An error occured while parsing the website {url}', WARNING_LEVEL['high'])

    return parsed_jokes