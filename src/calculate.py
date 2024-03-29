from time import sleep
from steam_pars.src.telegram import send_items_telegram
from steam_pars.database.mongo_db.lootfarm_db import get_loot_inst, LootFarmQueries
from steam_pars.database.peewee_db.queries import insert_all_loot, insert_all_trade_gg, loot_trade_table
from steam_pars.database.mongo_db.tradegg_db import get_trade_gg_inst, TradeGGQueries
from math import fabs
from steam_pars.schemas.common_schemas import ItemSchema
from loguru import logger


def find_percentage(a, b) -> int:
    return fabs(a - b) / a * 100


def find_profitable_pair(items: list[ItemSchema]) -> list[ItemSchema]:
    good_pair = []
    for item in items:
        if item.trade_price < item.loot_price + 5:
            item.percent = find_percentage(item.trade_price, item.loot_price)
            good_pair.append(item)
    return good_pair
    #return sorted(good_pair, key=lambda x: x['percent'], reverse=True)


def main(loot_mongo: LootFarmQueries, trade_mongo: TradeGGQueries, sec: int = 30):
    logger.info('start calculating')
    while True:
        insert_all_loot(loot_mongo.get_all())
        insert_all_trade_gg(trade_mongo.get_all())
        items = loot_trade_table()

        # here I got the good date, and I want to send it on my another app
        good_items = find_profitable_pair(items)
        send_items_telegram(good_items)
        logger.info('before sleep')
        sleep(sec)


if __name__ == '__main__':
    loot = get_loot_inst()
    trade = get_trade_gg_inst()
    main(loot, trade)



