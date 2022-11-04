from peewee import PostgresqlDatabase, Model
from steam_pars.src.config import config as conf

db = PostgresqlDatabase(conf.DB_NAME,
                        user=conf.DB_USER,
                        password=conf.DB_PASSWORD,
                        host=conf.DB_HOST,
                        port=conf.DB_PORT)


class BaseModel(Model):
    class Meta:
        database = db
