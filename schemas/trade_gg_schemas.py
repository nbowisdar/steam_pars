from pydantic import BaseModel


class TradeGGItem(BaseModel):
    name: str
    price: int
    have: int


class TradeGGItems(BaseModel):
    items: list[TradeGGItem]