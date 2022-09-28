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
    if save:
        with open(f'tradeit_items.json', 'w', encoding='utf-8') as file:
            json.dump(data['items'], file, indent=3)
    return data['items']


#data = get_tradeit_prices(limit=2000, min=1, max=100, save=True)

with open('tradeit_items.json') as file:
    date = json.load(file)

def get_items_from_lootfarm():
    agent = UserAgent().random
    headers = {
        'User-Agent': agent
    }
    link = 'https://loot.farm/fullprice.json'
    response = requests.get(link, headers=headers)
    print(response)

    # with open('json_dir/loot.json.json', 'w', encoding='utf-8') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    return response.json()

x = get_items_from_lootfarm() #TODO: add database here.

print(x[0])