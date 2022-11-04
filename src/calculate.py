from steam_pars.database.lootfarm_db import get_loot_inst
from steam_pars.database.peewee_db.queries import insert_all_loot, insert_all_trade_gg
from steam_pars.database.tradegg_db import get_trade_gg_inst
from time import perf_counter

loot = get_loot_inst()
trade = get_trade_gg_inst()

loot_items = loot.get_all()
tradegg_items = trade.get_all()

start = perf_counter()

insert_all_loot(loot_items)
#insert_all_trade_gg(tradegg_items)

print(perf_counter() - start)




