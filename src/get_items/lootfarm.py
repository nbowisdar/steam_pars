from fake_useragent import UserAgent
import aiohttp
from loguru import logger
from steam_pars.database.mongo_db.lootfarm_db import get_loot_inst

loot = get_loot_inst()


async def get_items_from_lootfarm() -> None:
    logger.info('Getting data from lootfarm')
    agent = UserAgent().random
    headers = {
        'User-Agent': agent
    }
    link = 'https://loot.farm/fullprice.json'
    async with aiohttp.ClientSession() as session:
        async with session.get(link, headers=headers) as response:
            resp_json = await response.json()

            # before insert date clear the table
            loot.prune_collection()
            loot.insert_many(resp_json)









