from peewee import *
from steam_pars.database.peewee_db.tables import Item, LootFarm
from steam_pars.database.peewee_db.config import db
from steam_pars.schemas.lootfarm_schemas import LFcsItemsSchema


def add_all_items(data: list[dict]):
    with db.atomic():
        Item.delete().execute()
        Item.insert_many(data).execute()


def build_loot(items: LFcsItemsSchema):
    count = 0
    with db.atomic():
        for item in items.items:
            item_db = Item.get(name=item.name)

            LootFarm(item=item_db,
                     price=item.price,
                     have=item.have,
                     max=item.max).save()
            count += 1
            print(count)