from steam_pars.database.mongo_db.lootfarm_db import get_loot_inst
from steam_pars.database.peewee_db.queries import insert_all_loot, insert_all_trade_gg, loot_trade_table
from steam_pars.database.mongo_db.tradegg_db import get_trade_gg_inst
from time import perf_counter
from math import fabs

def find_percentage(a, b) -> int:
    return fabs(a - b) / a


loot = get_loot_inst()
trade = get_trade_gg_inst()

# loot_items = loot.get_all()
# tradegg_items = trade.get_all()

start = perf_counter()

#insert_all_loot(loot_items)
#insert_all_trade_gg(tradegg_items)
items = loot_trade_table()


sorted_list = sorted(items, key=lambda item: find_percentage(item.loot_price, item.trade_price), reverse=True)

for i in sorted_list:
    print(i)


print(perf_counter() - start)




