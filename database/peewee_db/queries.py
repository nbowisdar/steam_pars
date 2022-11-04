from steam_pars.database.peewee_db.tables import LootFarm, TradeGG
from steam_pars.database.peewee_db.config import db


def insert_all_loot(data: list[dict]):
    with db.atomic():
        LootFarm.delete().execute()
        LootFarm.insert_many(data).execute()


def insert_all_trade_gg(data: list[dict]):
    with db.atomic():
        LootFarm.delete().execute()
        TradeGG.insert_many(data).execute()


def loot_trade_table():
    with db.atomic():
        return LootFarm.select().join(TradeGG, on=LootFarm.name == TradeGG.name)


s = loot_trade_table()

for i in s[:10]:
    print(i.name, i.price)