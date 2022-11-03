from steam_pars.database.sqlalchemy.engine import engine
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = 'item'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    loot: Mapped['Loot'] = relationship(
        back_populates='item',
    )
    trade_gg: Mapped['TradeGG'] = relationship(
        back_populates='item',
    )


class Loot(Base):
    __tablename__ = 'lootfarm'
    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    item: Mapped['Item'] = relationship(back_populates='loot')
    price: Mapped[int]
    have: Mapped[int]
    max: Mapped[int]
    # tr: Mapped[int]
    # res: Mapped[int]


class TradeGG(Base):
    __tablename__ = 'trade_gg'
    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    item: Mapped['Item'] = relationship(back_populates='trade_gg')
    price: Mapped[int]
    have: Mapped[int]


Base.metadata.create_all(engine)
