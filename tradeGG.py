import requests
from fake_useragent import UserAgent
import json
from pprint import pprint


def build_url(offset: int, limit: int, min: int = 1, max: int = 100) -> str:
    base = 'https://tradeit.gg/api/v2/inventory/data?gameId=730&'
    return base + f'offset={offset}&limit={limit}&searchValue=&minPrice={min}&maxPrice={max}' \
          '&minFloat=0&maxFloat=1&showTradeLock=true&colors=&fresh=true'

#max limit 1500
def get_tradeit_prices(limit = 1500, offset = 0, min = 0, max = 500, save = False) -> dict:
    agent = UserAgent().random
    print(agent)
    headers = {
        'User-Agent': agent
    }
    all_date = list()
    while True:
        url = build_url(offset, limit)
        data = requests.get(url, headers=headers).json()
        if data['items']:
            all_date.extend(data['items'])
            offset += limit
            print('ok')
            continue
        break
    good_date = list()
    for i in all_date:
        try:
            rez = list()
            rez.append(i['name'])
            rez.append(i['price'] / 100)
            rez.append(len(i['botIndexes']))
            rez.append(0)
            good_date.append(rez)
        except Exception as err:
            print(f'[Error]: {err}')
    print(f'Got {len(good_date)} items from {len(data["items"])}')
    if save:
        with open(f'tradeit_items.json', 'w', encoding='utf-8') as file:
            json.dump(good_date, file, indent=3)
    return data['items']


data = get_tradeit_prices(limit=1500, min=1, max=100, save=True)




