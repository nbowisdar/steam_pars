from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client.steam


class LootFarmCS:
    def __init__(self, loot):
        self.__loot = loot

    def prune_collection(self):
        self.__loot.drop()

    def insert_many(self, data: list):
        self.__loot.insert_many(data)

    def get_all(self) -> list:
        # bellow I can change retrieved data, by passing argument
        # example: find( {}, {name: 1, age: 1}... )
        query = self.__loot.find()
        return [item for item in query]


def get_loot_inst() -> LootFarmCS:
    lf_cs = db.lootfarmCs
    return LootFarmCS(lf_cs)


# if __name__ == '__main__':
#     # test
#     loot = LootFarmCS(lf_cs)
#     data = [{'name': 'aka-47', 'price': 20},
#             {'name': 'test', 'price': 0}]
#     #loot.insert_many(data)
#     loot.prune_collection()
#     s = loot.get_all()
#     print(s)
