import asyncio
from fake_useragent import UserAgent
import aiohttp
from steam_pars.database.mongo_db.tradegg_db import get_trade_gg_inst

limit: int = 1500
min_price: int = 1
max_price: int = 200
trade_mongo = get_trade_gg_inst()

def build_url(offset=0) -> str:
    base = 'https://tradeit.gg/api/v2/inventory/data?gameId=730&'
    return base + f'offset={offset}&limit={limit}&searchValue=&minPrice={min_price}&maxPrice={max_price}' \
                  '&minFloat=0&maxFloat=1&showTradeLock=true&colors=&fresh=true'


async def get_items_from_tradegg(local_offset=0):
    # clean previous data
    trade_mongo.prune_collection()
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
                    trade_mongo.insert_many(items)
                    local_offset += limit
                    continue
        return



