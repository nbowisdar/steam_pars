from engine import engine
from tables import Item, Loot, TradeGG
from sqlalchemy.orm import Session
from sqlalchemy import select
from steam_pars.database.lootfarm_db import get_loot_inst

loot_mongo = get_loot_inst()

data = loot_mongo.get_all()

# with Session(engine) as session:
#     #item = Item(**data.items[0].dict())
#     items = [Item(name='test1'), Item(name='test2')]
#     session.add_all(items)
#     session.commit()

# with Session(engine) as session:
#     item_one = Item(name='m4a4',
#                     loot=Loot(price=20, have=1, max=3,),
#                     trade_gg=TradeGG(price=18, have=3))
#     session.add(item_one)
#     session.commit()


with Session(engine) as session:
    smtp = select(Item).where(Item.name == 'aka-47')

    for i in session.scalars(smtp):
        i.name = 'new_name'
    session.commit()