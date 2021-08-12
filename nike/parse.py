import requests
from bs4 import BeautifulSoup
import csv
import os

URL = 'https://www.nike.com/ru/w/mens-sale-shoes-3yaepznik1zy7ok'
#URL = 'https://www.adidas.ru/?cm_mmc=AdieSEM_Yandex-_-adidas-Brand-B-Exact-Desktop-Rus-_-adidas-_-adidas-_-dv:eCom-_-cn:adidas-Brand-B-Exact-Desktop-Rus-_-pc:Yandex&cm_mmc1=RU&cm_mmc2=PPC-B-brand-None-Exact-RU-CIS-eCom-Paid_Search&yclid=4571525686535956786'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.3.756 Yowser/2.5 Safari/537.36',
    'accept': '*/*'
}
HOST = 'https://auto.ria.com'
FILE = 'nike.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    #print(r.text)
    print(r.ok)
    return r


def get_content(html):
    #   print(html)
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-card')
    nike = []
    print(items)
    for item in items:
        nike.append({
            'title': item.find('a', class_='product-card__link-overlay').get_text(strip=True),
            'link': item.find('a', class_='product-card__link-overlay').get('href'),
            'rub_price': item.find('div', class_='product-price').get_text().replace('\xa0', ''),
            'rub_price_prev': item.find('div', class_='product-price is--striked-out').get_text().replace('\xa0', '')
        })
    for nik in nike:
        print(nik)
    print(len(nike))
    return None


def parse():
    html = get_html(URL)
    nike = get_content(html.text)


parse()
