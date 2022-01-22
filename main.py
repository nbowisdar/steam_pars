import requests
from fake_useragent import UserAgent
from filter_data import Filter_data, Correct_price
import json
import time
agent = UserAgent().random
l1 = 'http://www.xhaus.com/headers'
headers = {
    'User-Agent':agent
}


def get_items_from_lootfarm():
    link = 'https://loot.farm/fullprice.json'
    return requests.get(link, headers = headers).json()

def get_data_from_swapGG():
    rez = requests.get('https://api.swap.gg/prices/730', headers).json()['result']
    new_data = []

    for item in rez:

        bot = Correct_price(item['price']['sides']['bot'])
        user = Correct_price(item['price']['sides']['user'])
        value = {
            'name':item['marketName'].replace('\'', ''),
            'bot_price': bot.price,
            'user_price': user.price,
            'have':item['stock']['have'],
            'max_have':item['stock']['max']
        }
        new_data.append(value)
    return new_data

def get_items_from_csmoney():
    #count need to be multiple of 60
    min_price = 3000
    max_price = 5000
    batch_size = 0
    offset = 60
    while True:
        for item in range(0, offset + batch_size, offset):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?limit=60&maxPrice={max_price}&minPrice={min_price}&offset={offset}&withStack=true'
            response = requests.get(
                url, headers=headers
            )
            data = response.json()
            items = data.get('items')
            rez = []
            for item in items:
                d = {
                    'price':item['price'],
                    'name':item['fullName']
                }
                print(f'Rez {d}')
                rez.append(d)
            batch_size += offset
            print(f'Обработка страницы номер {batch_size}')
        if len(items) < 60:
            break
    return rez



    #return requests.get(link, headers=headers).json()['items']

def get_items_from_steam(quantity=100):
    BASE = 'https://steamcommunity.com/market/search/render/?query=&'
    rez = []
    start, count = 1, 100
    cycle = round(quantity/100)
#'https://steamcommunity.com/market/search/render/?query=&start=1&count=100&norender=1%2Fnorender%3D1&appid=730'
    for i in range(cycle):
        print(headers)
        link = f'start={start}&count={quantity}&norender=1%2Fnorender%3D1&appid=730'
        response = requests.get(BASE+link, headers= headers).json()['results']
        #print(response)
        rez += response

        start = count
        count += 100
    return rez


def make_table_STEAM_vs_LOOTFARM(steam, loot):
    match = []
    for item in steam:
        for i_loot in loot:
            if item['name'] == i_loot['name'].replace('\'', ''):
                loot_price = i_loot['price']
                price = Correct_price(loot_price)
                bot_price, user_price = price.correct_price_for_loot()

                steam_sell = round(item['sell_price'] / 100, 2)
                steam_sale = float(item['sale_price_text'][1:])

                match.append(
                    {'name':item['name'],
                     'steam':
                         {'max_price_steam':steam_sell,
                     'min_price_steam':steam_sale,},
                     'loot_info':
                         {'loot_price_sell':bot_price,
                     'loot_price_buy':user_price,
                     'loot_have':i_loot['have'],
                     'loot_max':i_loot['max'],
                     'loot_res':i_loot['res'],
                     'loot_tr':i_loot['tr']}
                     }
                )
                break
    return match

def make_table_LOOT__GG(loot, gg):
    # list_loot = {item['name']:loot.index(item) for item in loot}
    list_gg = {item['name']: gg.index(item) for item in gg}

    new_data = []
    for item in loot:
        if item['name'] in list_gg:
            item['gg_info'] = gg[list_gg[item['name']]]
    return loot
