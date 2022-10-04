from get_items.lootfarm import get_items_from_lootfarm
from get_items.tradeGG import get_items_from_tradegg
from work_with_db import Cursor
import asyncio


async def main(time: int):
    while True:
        cursor = Cursor()
        lootfarm_task = asyncio.create_task(get_items_from_lootfarm())
        tradegg_task = asyncio.create_task(get_items_from_tradegg())
        lootfarm = await lootfarm_task
        tradegg = await tradegg_task
        # print('Len - loot -', len(lootfarm))
        # print('Len - trade -', len(tradegg))
        cursor.save_to_db('lootfarm', lootfarm)
        cursor.save_to_db('tradegg', tradegg)
        asyncio.sleep(time)

if __name__ == '__main__':
    asyncio.run(main(100))



