from collect_date import get_items_from_lootfarm
from work_with_db import Cursor
import json
from time import perf_counter

#rez = get_items_from_lootfarm(save=True)
# with open('tradeit_items.json') as file:
#     rez = json.load(file)
with open('lootfarm_items.json') as file:
    rez = json.load(file)
    #print(rez)
    #print(len(rez))

data = list()
for i in rez:
    item = list()
    item.append(i['name']), item.append(i['price']/100), item.append(i['have']), item.append(i['max'])
    data.append(item)

start = perf_counter()
cursor = Cursor()
cursor.save_to_db('lootfarm', data)
print(perf_counter() - start)
data = cursor.show_date('lootfarm')
#print(data)
print(len(data))
# for i in data:
#     print(i)

