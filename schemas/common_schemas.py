from pydantic import BaseModel
from steam_pars.schemas.lootfarm_schemas import LFcsItemSchema
from steam_pars.schemas.trade_gg_schemas import TradeGGItem


class Item:
    name: str
    lootfarm: list[LFcsItemSchema]
    tradge_gg: list[TradeGGItem]