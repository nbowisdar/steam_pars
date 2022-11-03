from peewee import *

from steam_pars.database.peewee_db.config import BaseModel, db


class Item(BaseModel):
    name = CharField(unique=True)


class LootFarm(BaseModel):
    item = ForeignKeyField(Item, backref='lootfarm', on_delete='CASCADE', on_update='CASCADE')
    price = IntegerField()
    have = IntegerField()
    max = IntegerField()


class TradeGG(BaseModel):
    item = ForeignKeyField(Item, backref='tradegg', on_delete='CASCADE', on_update='CASCADE')
    price = IntegerField()
    have = IntegerField()


if __name__ == '__main__':
    db.create_tables([Item, LootFarm, TradeGG])
