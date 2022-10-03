import requests
from fake_useragent import UserAgent
import json
import aiohttp


def build_url(offset: int, limit: int, min: int = 1, max: int = 100) -> str:
    base = 'https://tradeit.gg/api/v2/inventory/data?gameId=730&'
    return base + f'offset={offset}&limit={limit}&searchValue=&minPrice={min}&maxPrice={max}' \
          '&minFloat=0&maxFloat=1&showTradeLock=true&colors=&fresh=true'

#max limit 1500
async def get_items_from_tradegg(limit = 1500, offset = 0, min = 0, max = 500, save = False) -> list:
    print('Getting data from tradeGG')
    agent = UserAgent().random
    headers = {
        'User-Agent': agent
    }
    all_date = list()
    while True:
        url = build_url(offset, limit)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                resp_json = await response.json()
                if resp_json['items']:
                    all_date.extend(resp_json['items'])
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
    print(f'Got {len(good_date)} items from {len(all_date)}')
    if save:
        with open(f'tradeit_items.json', 'w', encoding='utf-8') as file:
            json.dump(good_date, file, indent=3)
    return good_date




