import requests
from fake_useragent import UserAgent
import json

agent = UserAgent().random
headers = {
    'User-Agent':agent
}
link = 'https://api.swap.gg/prices/730'
def get_data_from_swapGG():
    rez = requests.get('https://api.swap.gg/prices/730', headers).json()['result']
    new_data = []
    for item in rez:
        value = {
            'name':item['marketName'],
            'bot_price': item['price']['sides']['bot'],
            'user_price': item['price']['sides']['user'],
            'have':item['stock']['have'],
            'max_have':item['stock']['max']
        }
        new_data.append(value)
    return new_data
# with open('json_dir/gg1.json', 'w', encoding='utf-8') as file:
#     json.dump(new_data, file, indent=4, ensure_ascii=False)
