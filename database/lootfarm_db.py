from steam_pars.database.mongo_db import MongoQueriesBase, db


class LootFarmQueries(MongoQueriesBase):
    def __init__(self, collection):
        super().__init__(collection)

    def get_all(self) -> list[dict]:
        return self.collection.find({}, {'_id': 0, 'name': 1, 'price': 1, 'have': 1, 'max': 1})


def get_loot_inst() -> LootFarmQueries:
    lf_cs = db.lootfarmCs
    return LootFarmQueries(lf_cs)


# if __name__ == '__main__':
#     loot = get_loot_inst()
#     s = loot.get_all_new()
#     for i in s[:10]:
#         print(i)
#         print(type(i))
