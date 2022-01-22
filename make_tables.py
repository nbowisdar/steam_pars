from filter_data import Correct_price
import json

class Make_tables:
    def __init__(self, steam=None,loot=None,gg=None):
        self.steam = steam
        self.loot = loot
        self.gg = gg
        print('START making tables')


    def make_table_LOOT__GG(self):
        # list_loot = {item['name']:loot.index(item) for item in loot}
        list_gg = {item['name']: self.gg.index(item) for item in self.gg}


        new_data = []
        for item in self.loot:
            if item['name'] in list_gg:
                new_data.append({
                    'loot_info':item,
                    'gg_info':self.gg[list_gg[item['name']]]
                })
                #item['gg_info'] = gg[list_gg[item['name']]]
        with open('json_dir/loot-gg.json', 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)
        return new_data


    def make_table_STEAM_vs_LOOTFARM(self, steam, loot):
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
                        {'name': item['name'],
                         'steam':
                             {'max_price_steam': steam_sell,
                              'min_price_steam': steam_sale, },
                         'loot_info':
                             {'loot_price_sell': bot_price,
                              'loot_price_buy': user_price,
                              'loot_have': i_loot['have'],
                              'loot_max': i_loot['max'],
                              'loot_res': i_loot['res'],
                              'loot_tr': i_loot['tr']}
                         }
                    )
                    break
        return match
