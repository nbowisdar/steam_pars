from main import *
from filter_data import Filter_data


loot = get_items_from_lootfarm()
gg = get_data_from_swapGG()
#steam = get_items_from_steam(1500)
#rez = make_table_STEAM_vs_LOOTFARM(steam, loot)
rez = make_table_LOOT__GG(loot, gg)

x = Filter_data(rez)
#x.filter_from_loot_to_steam()
x.filter_from_loot_to_GG()
x.save_rez_to_json()
