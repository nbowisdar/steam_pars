from main import *
from filter_data import Filter_data
from make_tables import Make_tables

# with open('json_dir/sorted_rez', encoding='utf-8') as file:
#     rez = json.load(file)
with open('json_dir/gg1.json', encoding='utf-8') as file:
    gg = json.load(file)
with open('json_dir/loot.json.json', encoding='utf-8') as file:
    loot = json.load(file)

# loot = get_items_from_lootfarm()
# gg = get_data_from_swapGG()
#steam = get_items_from_steam(100)
# x = make_table_LOOT__GG(loot, gg)
# for i in x:
#     print(i)

x = Make_tables(loot=loot, gg=gg)
x.make_table_LOOT__GG()
print(x)
#x = Filter_data(rez)
#x.filter_from_loot_to_steam()
#x.filter_from_loot_to_GG()
#x.save_rez_to_json()
