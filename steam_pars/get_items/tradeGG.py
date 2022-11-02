import asyncio
from fake_useragent import UserAgent
import aiohttp
from steam_pars.database.tradegg_db import get_trade_gg_inst

limit: int = 1500
min_price: int = 5
max_price: int = 25
trade_gg = get_trade_gg_inst()

def build_url(offset=0) -> str:
    base = 'https://tradeit.gg/api/v2/inventory/data?gameId=730&'
    return base + f'offset={offset}&limit={limit}&searchValue=&minPrice={min_price}&maxPrice={max_price}' \
                  '&minFloat=0&maxFloat=1&showTradeLock=true&colors=&fresh=true'


async def get_items_from_tradegg(local_offset=0):
    # clean previous data
    trade_gg.prune_collection()
    agent = UserAgent().random
    headers = {
        'User-Agent': agent
    }
    while True:
        url = build_url(local_offset)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                resp_json = await response.json()
                items = resp_json['items']
                if items:
                    trade_gg.insert_many(items)
                    local_offset += limit
                    continue
        return
    # good_date = list()
    # for i in all_date:
    #     try:
    #         rez = list()
    #         rez.append(i['name'])
    #         rez.append(i['price'] / 100)
    #         rez.append(len(i['botIndexes']))
    #         rez.append(0)
    #         good_date.append(rez)
    #     except Exception as err:
    #         print(f'[Error]: {err}')
    # print(f'Got {len(good_date)} items from {len(all_date)}')
    # if save:
    #     with open(f'tradeit_items.json', 'w', encoding='utf-8') as file:
    #         json.dump(good_date, file, indent=3)
    # return good_date


asyncio.run(get_items_from_tradegg())