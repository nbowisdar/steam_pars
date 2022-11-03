from peewee import PostgresqlDatabase, Model

db = PostgresqlDatabase('test_db', user='root', password='root', host='192.168.0.107', port=5432)

class BaseModel(Model):
    class Meta:
        database = db
