from steam_pars.database.peewee_db.tables import LootFarm, TradeGG
from steam_pars.database.peewee_db.connect import db
from steam_pars.schemas.common_schemas import ItemSchema


def insert_all_loot(data: list[dict]):
    with db.atomic():
        LootFarm.delete().execute()
        LootFarm.insert_many(data).execute()


def insert_all_trade_gg(data: list[dict]):
    with db.atomic():
        LootFarm.delete().execute()
        TradeGG.insert_many(data).execute()


def loot_trade_table() -> list[ItemSchema]:
    with db.atomic():
        cursor = db.execute_sql('''
        SELECT lf.name, lf.price as loot_price, lf.have, lf.max, trade.price, trade.have
        FROM lootfarm as lf
        JOIN tradegg as trade
        ON trade.name = lf.name
        ''')
        rez = []
        for row in cursor.fetchall():
            rez.append(ItemSchema(
                name=row[0],
                loot_price=row[1],
                loot_have=row[2],
                loot_max=row[3],
                trade_price=row[4],
                trade_have=row[5]
            ))
        return rez


if __name__ == '__main__':
    loot_trade_table()