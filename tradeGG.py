import requests
from fake_useragent import UserAgent
import json
from pprint import pprint

#max limit 1500
def get_tradeit_prices(limit = 100, offset = 0, sortType = 'Popularity', min = 0, max = 500, save = False) -> dict:
    agent = UserAgent().random
    headers = {
        'User-Agent': agent
    }
    base = 'https://tradeit.gg/api/v2/inventory/data?gameId=730&'
    url = base + f'offset={offset}&limit={limit}&sortType={sortType}&searchValue=&minPrice={min}&maxPrice={max}' \
          '&minFloat=0&maxFloat=1&showTradeLock=true&colors=&fresh=true'
    #print(url)
    data = requests.get(url, headers=headers).json()
    good_date = list()
    for i in data['items']:
        rez = list()
        rez.append(i['name'])
        rez.append(i['price'] / 100)
        rez.append(len(i['botIndexes']))
        rez.append(0)
        good_date.append(rez)
    if save:
        with open(f'tradeit_items.json', 'w', encoding='utf-8') as file:
            json.dump(good_date, file, indent=3)
    return data['items']


data = get_tradeit_prices(limit=100, min=1, max=100, save=True)




