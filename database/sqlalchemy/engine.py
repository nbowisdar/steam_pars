from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://root:root@192.168.0.107:5432/test_db")
