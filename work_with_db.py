import psycopg2
username = 'king'
password = '1324'
database = 'steam'
port = 5432

class Cursor:

    def __init__(self):
        connection = psycopg2.connect(
            user=username,
            password=password,
            database=database,
            port=port
        )
        connection.autocommit = True
        self.connection = connection

    def show_date(self, table) -> list:
        with self.connection.cursor() as cur:
            cur.execute(f'SELECT * FROM {table}')
            return cur.fetchall()

    def save_to_db(self, table: str, date: list):
        with self.connection.cursor() as cur:
            count_err = 0
            for item in date:
                try:
                    name, price, have, max = item
                    print(name, price)
                    cur.execute(f"""INSERT INTO {table} (name, price, have, max) VALUES ('{name}', {price}, {have}, {max})
                    ON CONFLICT (name) DO UPDATE SET price={price}, have={have}, max={max}""")
                except Exception as err:
                    #print(item)
                    print(f'[INFO]: Exception: {err}')
                    count_err += 1
            print('[INFO] was ', count_err, 'errors')


# c = Cursor()
# max = 10
# have = 5
# price = 10.2
# name = "test"
# name1 = f'{name}'
# print(name1)
# with c.connection.cursor() as cur:
#     cur.execute(f"""INSERT INTO lootfarm (name, price, have, max) VALUES ('{name}', {price}, {have}, {50})""")