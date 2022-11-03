from steam_pars.database.lootfarm_db import get_loot_inst
from steam_pars.database.peewee_db.queries import build_loot
from steam_pars.database.tradegg_db import get_trade_gg_inst
from time import perf_counter

loot = get_loot_inst()
trade = get_trade_gg_inst()

loot_items = loot.get_all()


start = perf_counter()

build_loot(loot_items)

print(perf_counter() - start)




