from pydantic import BaseModel


class ItemSchema(BaseModel):
    name: str
    loot_price: int
    loot_have: int
    loot_max: int
    trade_price: int
    trade_have: int
