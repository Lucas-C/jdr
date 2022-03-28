#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re, requests
from random import randrange


RESULTS_PER_PAGE = 10  # smaller => less HTML to parse


def get_model_count():
    resp = requests.get('https://ws.q3df.org/models/')
    resp.raise_for_status()
    match = re.search(r" (\d+) results", resp.text)
    return int(match.group(1))

def get_model_href(model_index):
    page_id = model_index // RESULTS_PER_PAGE
    url = f'https://ws.q3df.org/models/?model=&page={page_id}&show={RESULTS_PER_PAGE}'
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    items = soup.find_all(class_='models_modelitem')
    assert len(items) <= RESULTS_PER_PAGE
    item = items[model_index % RESULTS_PER_PAGE]
    assert item, (model_index, url)
    return item.find('a')['href']

def get_img_urls(model_href):
    url = 'https://ws.q3df.org' + model_href
    resp = requests.get(url)
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
    model_href = get_model_href(model_index)
    print(get_img_urls(model_href))
