import json
class Filter_data:
    def get_valid_data(self, bad_data):
        data = []
        for item in bad_data:
            if item['loot_price_buy'] > 1:
                data.append(item)
        self.data = data

    def get_procent_from_a(self, big, small):
        return round(100 - big/small*100, 2)

    def __init__(self, data):
        self.cod = 'without_filter'
        self.data = data

    def filter_from_loot_to_steam(self):
        self.cod = 'LOOT_STEAM'
        for item in self.data:
            item['profit'] = self.get_procent_from_a(item['min_price_steam'], item['loot_price_buy'])
        self.data = sorted(self.data, key=lambda x: x['profit'])
        return self.data
    def save_rez_to_json(self):
        with open(f'json_dir/rez-{self.cod}.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def filter_from_loot_to_GG(self):
        self.cod ='LOOT_GG'
        for item in self.data:
            item['profit'] = self.get_procent_from_a(item['gg_info']['user_price'], item['loot_info']['loot_price_buy'])
        self.data = sorted(self.data, key=lambda x: x['profit'])
        return self.data

class Correct_price:
    def __init__(self, price):
        if type(price) == int:
            self.price = round(price/100, 2)
        else:
            self.price = 'Not Found price'


    def correct_price_for_loot(self, price, cof=0.95):
        bot_price = price/ 100
        user_price = round(bot_price * cof, 2)
        return (bot_price,user_price)