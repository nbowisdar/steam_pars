from steam_pars.database.mongo_db import MongoQueriesBase, db
from steam_pars.schemas.trade_gg_schemas import TradeGGItem, TradeGGItems


def get_amount(bots: list | None):
    if bots:
        return len(bots)
    return 0


class TradeGGQueries(MongoQueriesBase):
    def __init__(self, collection):
        super().__init__(collection)

        #self.collection = collection

    def get_all(self) -> TradeGGItems:
        # I don't need all the fields
        query = self.collection.find(
            {}, {'name': 1, 'price': 1, 'botIndexes': 1}
        )
        rez = []
        for item in query:
            # botIndexes represents list with bots that has an item - I want to get an amount
            if 'botIndexes' in item:
                have = get_amount(item.pop('botIndexes'))
            else:
                have = 0
            item.update({'have': have})
            rez.append(TradeGGItem(**item))
        return TradeGGItems(items=rez)


def get_trade_gg_inst() -> TradeGGQueries:
    trade_gg = db.tradegg
    return TradeGGQueries(trade_gg)

#
# if __name__ == '__main__':
#     gg = get_trade_gg_inst()
#     gg.get_all()