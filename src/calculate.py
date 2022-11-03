from steam_pars.database.lootfarm_db import get_loot_inst
from steam_pars.database.tradegg_db import get_trade_gg_inst
from time import perf_counter

loot = get_loot_inst()
trade = get_trade_gg_inst()

loot_items = loot.get_all()
trade_items = trade.get_all()

count = 0

start = perf_counter()
for item in trade_items.items:
    for item_loot in loot_items.items:
        if item.name == item_loot.name:
            count += 1
            continue

print(perf_counter() - start)
print(f'all matches - {count}')