from peewee import CharField, IntegerField

from steam_pars.database.peewee_db.config import BaseModel, db


class LootFarm(BaseModel):
    name = CharField(unique=True)
    price_loot = IntegerField()
    have_loot = IntegerField()
    max_loot = IntegerField()


class TradeGG(BaseModel):
    name_trade = CharField(unique=True)
    price_trade = IntegerField()
    have_trade = IntegerField()


if __name__ == '__main__':
    db.create_tables([LootFarm, TradeGG])
