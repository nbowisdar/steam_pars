from fake_useragent import UserAgent
import json
import aiohttp


async def get_items_from_lootfarm(save=False) -> list:
    print('Getting data from lootfarm')
    agent = UserAgent().random
    headers = {
        'User-Agent': agent
    }
    link = 'https://loot.farm/fullprice.json' #
    async with aiohttp.ClientSession() as session:
        async with session.get(link, headers=headers) as response:
            rez = list()
            resp_json = await response.json()
            for i in resp_json:
                item = list()
                item.append(i['name']), item.append(i['price']/100), item.append(i['have']), item.append(i['max'])
                rez.append(item)
    if save:
        with open('lootfarm_items.json', 'w', encoding='utf-8') as file:
            json.dump(rez, file, indent=4)
    print('Data from lootfarm was gotten')
    return rez



# def get_data_from_swapGG():
#     response = requests.get('https://api.swap.gg/prices/730', headers)
#     print(response)
#     rez = response.json()['result']
#     new_data = []
#
#     for item in rez:
#
#         bot = Correct_price(item['price']['sides']['bot'])
#         user = Correct_price(item['price']['sides']['user'])
#         value = {
#             'name':item['marketName'].replace('\'', ''),
#             'bot_price': bot.price,
#             'user_price': user.price,
#             'have':item['stock']['have'],
#             'max_have':item['stock']['max']
#         }
#         new_data.append(value)
#     with open('json_dir/gg1.json', 'w', encoding='utf-8') as file:
#         json.dump(new_data, file, indent=4, ensure_ascii=False)
#     return new_data

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



