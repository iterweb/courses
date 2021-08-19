import sqlite3


class DataWriter:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS advert(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price TEXT,
            published TEXT);
            """
        )
        self.conn.commit()

    def get_data(self):
        list_titles = []
        self.cur.execute("SELECT title FROM advert;")
        db_titles = self.cur.fetchall()

        for i in db_titles:
            list_titles.append(''.join(i))

        print(list_titles)
        return list_titles

    def save_data(self, title, price, published):
        self.cur.execute(f"""INSERT INTO advert(title, price, published)
                           VALUES('{title}', '{price}', '{published}');""")
        self.conn.commit()