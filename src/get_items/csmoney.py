# def get_items_from_csmoney():
#     #count need to be multiple of 60
#     min_price = 3000
#     max_price = 5000
#     batch_size = 0
#     offset = 60
#     while True:
#         for item in range(0, offset + batch_size, offset):
#             url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?limit=60&maxPrice={max_price}&minPrice={min_price}&offset={offset}&withStack=true'
#             response = requests.get(
#                 url, headers=headers
#             )
#             data = response.json()
#             items = data.get('items')
#             rez = []
#             for item in items:
#                 d = {
#                     'price':item['price'],
#                     'name':item['fullName']
#                 }
#                 logger.info(f'Rez {d}')
#                 rez.append(d)
#             batch_size += offset
#             logger.info(f'Обработка страницы номер {batch_size}')
#         if len(items) < 60:
#             break
#     return rez



    #return requests.get(link, headers=headers).json()['items']

# def get_items_from_steam(quantity=100):
#     BASE = 'https://steamcommunity.com/market/search/render/?query=&'
#     rez = []
#     start, count = 1, 100
#     cycle = round(quantity/100)
# #'https://steamcommunity.com/market/search/render/?query=&start=1&count=100&norender=1%2Fnorender%3D1&appid=730'
#     for i in range(cycle):
#         logger.info(headers)
#         link = f'start={start}&count={quantity}&norender=1%2Fnorender%3D1&appid=730'
#         response = requests.get(BASE+link, headers= headers).json()['results']
#         #logger.info(response)
#         rez += response
#
#         start = count
#         count += 100
#     return rez