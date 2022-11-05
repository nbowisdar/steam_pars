from steam_pars.database.mongo_db.lootfarm_db import get_loot_inst
from steam_pars.database.peewee_db.queries import insert_all_loot, insert_all_trade_gg, loot_trade_table
from steam_pars.database.mongo_db.tradegg_db import get_trade_gg_inst
from time import perf_counter
from math import fabs

from steam_pars.src.pulling import start_pulling


def find_percentage(a, b) -> int:
    return fabs(a - b) / a


def main():
    loot = get_loot_inst()
    trade = get_trade_gg_inst()

    # TODO line below I must put in different process
    start_pulling(one_time=True)
    #


    insert_all_loot(loot.get_all())
    insert_all_trade_gg(trade.get_all())
    items = loot_trade_table()


    sorted_list = sorted(items, key=lambda item: find_percentage(item.loot_price, item.trade_price), reverse=True)

# TODO filter date, and get only profitable pair


if __name__ == '__main__':
    main()



