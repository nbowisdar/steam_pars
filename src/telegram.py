import telebot

from steam_pars.schemas.common_schemas import ItemSchema
from steam_pars.src.config.config import TOKEN_BOT, CHAT_ID

bot = telebot.TeleBot(TOKEN_BOT)


def send_items_telegram(items: list[ItemSchema]):
    for item in items:
        message = f'''
                    {item.name},
                    Lootfarm: {item.loot_price/100}, {item.loot_have}, {item.loot_max}
                    TradeGG: {item.trade_price}, {item.trade_have},
                    Percentage: {item.percent}
        '''
        bot.send_message(CHAT_ID, str(item))