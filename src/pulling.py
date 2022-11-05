import asyncio
from loguru import logger

from steam_pars.src.get_items.lootfarm import get_items_from_lootfarm
from steam_pars.src.get_items.tradeGG import get_items_from_tradegg


async def run_tasks():
    loot_task = asyncio.create_task(get_items_from_tradegg())
    trade_task = asyncio.create_task(get_items_from_lootfarm())

    await loot_task
    await trade_task


async def pulling(sec: int):
    while True:
        await run_tasks()
        await asyncio.sleep(sec)


def start_pulling(sec: int):
    logger.info("Start pulling!")
    asyncio.run(pulling(sec))
