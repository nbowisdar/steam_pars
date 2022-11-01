from pydantic import BaseModel


class LFcsItemSchema(BaseModel):
    name: str
    price: int
    have: int
    max: int
    tr: int
    res: int

    class Config:
        orm_mode = True


class LFcsItemsSchema(BaseModel):
    items: list[LFcsItemSchema]
