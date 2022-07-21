#!/usr/bin/env python3
import logging, re, requests
from bs4 import BeautifulSoup
from http.client import HTTPConnection
from random import randrange

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
# HTTPConnection.debuglevel = 2

RESULTS_PER_PAGE = 10  # smaller => less HTML to parse

session = requests.session()  # make things a lot faster by re-using the same PHPSESSID cookie


def get_model_count():
    resp = session.get('https://ws.q3df.org/models/')
    resp.raise_for_status()
    match = re.search(r" (\d+) results", resp.text)
    return int(match.group(1))

def get_model_href(model_index):
    page_id = model_index // RESULTS_PER_PAGE
    url = f'https://ws.q3df.org/models/?model=&page={page_id}&show={RESULTS_PER_PAGE}'
    resp = session.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    items = soup.find_all(class_='models_modelitem')
    assert len(items) <= RESULTS_PER_PAGE
    item = items[model_index % RESULTS_PER_PAGE]
    assert item, (model_index, url)
    return item.find('a')['href']

def get_img_urls(model_href):
    url = 'https://ws.q3df.org' + model_href
    resp = session.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    details_container = soup.find(id='modeldetails_container')
    assert details_container, url
    imgs = details_container.find_all('img')
    assert len(imgs) >= 3, (len(imgs), url)
    return {
        'head_face': 'https://ws.q3df.org' + imgs[0]['src'],
        'head_profile': 'https://ws.q3df.org' + imgs[1]['src'],
        'body': 'https://ws.q3df.org' + imgs[2]['src'],
    }

if __name__ == '__main__':
    model_count = get_model_count()
    model_index = randrange(model_count)
    print(f'{model_index=}')
    model_href = get_model_href(model_index)
    img_urls = get_img_urls(model_href)
    for img_url in img_urls.values():
        resp = session.get(img_url, stream=True)
        resp.raise_for_status()
        with open(img_url[27:], 'wb') as img_file:
            img_file.write(resp.raw.read())
