from main import *

loot = get_items_from_lootfarm()
steam = get_items_from_steam(1500)
rez = make_table_STEAM_vs_LOOTFARM(steam, loot)

with open('rez.json', 'w', encoding='utf-8') as file:
    json.dump(rez ,file, indent=4, ensure_ascii=False)

x = Filter_data(rez)
x.filter_from_loot_to_steam()
x.save_rez_to_json()
