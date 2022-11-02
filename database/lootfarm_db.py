from steam_pars.database.mongo_db import MongoQueriesBase, db
from steam_pars.schemas.lootfarm_schemas import LFcsItemsSchema, LFcsItemSchema


class LootFarmQueries(MongoQueriesBase):
    def __init__(self, collection):
        super().__init__(collection)

    def get_all(self) -> LFcsItemsSchema:
        # I don't need all the fields
        query = self.collection.find()
        rez = []
        for item in query:
            rez.append(LFcsItemSchema(**item))
        return LFcsItemsSchema(items=rez)


def get_loot_inst() -> LootFarmQueries:
    lf_cs = db.lootfarmCs
    return LootFarmQueries(lf_cs)


if __name__ == '__main__':
    loot = get_loot_inst()
    s = loot.get_all()
    for i in s.items:
        print(i.name, i.price)