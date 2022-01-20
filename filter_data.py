import json
class Filter_data:
    def get_valid_data(self, bad_data):
        data = []
        for item in bad_data:
            if item['loot_price_buy'] > 1:
                data.append(item)
        return data

    def get_procent_from_a(self, big, small):
        return round(100 - big/small*100, 2)

    def __init__(self, data):

        self.data = self.get_valid_data(data)
    def filter_from_loot_to_steam(self):
        for item in self.data:
            item['profit'] = self.get_procent_from_a(item['min_price_steam'], item['loot_price_buy'])
        self.data = sorted(self.data, key=lambda x: x['profit'])
        return self.data
    def save_rez_to_json(self):
        with open('json_dir/sorted_rez', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)




#x.save_rez_to_json()