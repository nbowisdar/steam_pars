import json
class Filter_data:
    def __init__(self, data):
        self.data = data

    def get_valid_data(self):
        new_data = []
        for item in self.data:

            price = Correct_price(item['loot_info']['price'])
            bot_price, user_price = price.correct_price_for_loot()
            item['loot_info']['bot_price'] = bot_price
            item['loot_info']['user_price'] = user_price

            del item['loot_info']['price']
            if item['loot_info']['bot_price'] > 1 and item['loot_info']['have'] > 0:

                new_data.append(item)
        self.data = new_data

    def get_procent_from_a(self, big, small):
        return round(100 - big/small*100, 2)


    def filter_from_loot_to_steam(self, a,b):
        for item in self.data:
            item['profit'] = self.get_procent_from_a(a, b)
        self.data = sorted(self.data, key=lambda x: x['profit'])
        return self.data
    def save_rez_to_json(self):
        with open('json_dir/rez.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def filter_from_loot_to_GG(self):
        for item in self.data:

            item['profit'] = self.get_procent_from_a(item['gg_info']['bot_price'], item['loot_info']['bot_price'])
        self.data = sorted(self.data, key=lambda x: x['profit'])
        return self.data

class Correct_price:
    def __init__(self, price):
        if type(price) == int:
            self.price = round(price/100, 2)
        else:
            self.price = 0

    def correct_price_for_loot(self,  cof=0.95):
        user_price = round(self.price * cof, 2)
        return (self.price,user_price)
