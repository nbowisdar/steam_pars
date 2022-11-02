from sqlalchemy import create_engine, Integer, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("postgresql+psycopg2://root:root@192.168.0.107:5432/test_db")


class Base(DeclarativeBase):
    pass


class LFcsItem(Base):
    __tablename__ = 'LootFarmCSItem'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    have: Mapped[int]
    max: Mapped[int]
    rate: Mapped[int]
    tr: Mapped[int]
    res: Mapped[int]

    def __str__(self):
        return str(self.id)

#Base.metadata.create_all(engine)


if __name__ == '__main__':
    session = Session(engine)
    stmt = select(LFcsItem)

    items = session.scalars(stmt)
    for item in items:
        print(item)