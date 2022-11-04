from steam_pars.database.mongo_db.base import MongoQueriesBase, db


# calculate numer of items by bots that have this item
def get_amount(bots: list | None):
    if bots:
        return len(bots)
    return 0


class TradeGGQueries(MongoQueriesBase):
    def __init__(self, collection):
        super().__init__(collection)

        #self.collection = collection

    def get_all(self) -> list[dict]:
        # I don't need all the fields
        query = self.collection.find(
            {}, {'_id': 0, 'name': 1, 'price': 1, 'botIndexes': 1}
        )
        rez = []
        for item in query:
            # botIndexes represents list with bots that has an item - I want to get an amount
            if 'botIndexes' in item:
                # if any of bots has this item we drop this field and take amount of items
                have = get_amount(item.pop('botIndexes'))
            else:
                have = 0
            item.update({'have': have})
            rez.append(item)
        return rez


def get_trade_gg_inst() -> TradeGGQueries:
    trade_gg = db.tradegg
    return TradeGGQueries(trade_gg)


# if __name__ == '__main__':
#     gg = get_trade_gg_inst()
#     all1 = gg.get_all()
