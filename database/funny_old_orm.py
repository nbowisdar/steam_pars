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
                    cur.execute(f"""INSERT INTO {table} (name, price, have, max) VALUES ('{name.replace("'", ' ')}', {price}, {have}, {max})
                    ON CONFLICT (name) DO UPDATE SET price={price}, have={have}, max={max}""")
                except Exception as err:
                    #print(item)
                    print(f'[INFO]: Exception: {err}')
                    count_err += 1
            print('[INFO] was ', count_err, 'errors')

    def create_table(self):
        with self.connection.cursor() as cur:
            cur.execute("SELECT lootfarm.name, lootfarm.price, lootfarm.have, lootfarm.max,"
                        "tradegg.price, tradegg.have FROM lootfarm "
                        "JOIN tradegg ON tradegg.name = lootfarm.name")
            data = cur.fetchall()
            rez = list()

            for value in data:
                value_l = list(value)
                value_l.append(round(value[1] / value_l[4] * 100, 2))
                rez.append(value_l)

            return sorted(rez, key=lambda x: x[6])

