from peewee import CharField, IntegerField

from steam_pars.database.peewee_db.connect import BaseModel, db


class LootFarm(BaseModel):
    name = CharField(unique=True)
    price = IntegerField()
    have = IntegerField()
    max = IntegerField()


class TradeGG(BaseModel):
    name = CharField(unique=True)
    price = IntegerField()
    have = IntegerField()


if __name__ == '__main__':
    db.create_tables([LootFarm, TradeGG])
