from main import *
from filter_data import Filter_data
from make_tables import Make_tables

# with open('json_dir/sorted_rez', encoding='utf-8') as file:
#     rez = json.load(file)
# with open('json_dir/gg1.json', encoding='utf-8') as file:
#     gg = json.load(file)
# with open('json_dir/loot.json.json', encoding='utf-8') as file:
#     loot = json.load(file)

loot = get_items_from_lootfarm()
gg = get_data_from_swapGG()
#steam = get_items_from_steam(100)

x = Make_tables(loot=loot, gg=gg)
table = x.make_table_LOOT__GG()

filter_data = Filter_data(table)
filter_data.get_valid_data()

filter_data.filter_from_loot_to_GG()

filter_data.save_rez_to_json()
