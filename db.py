import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS from_where (id INTEGER PRIMARY KEY, from_where text, to_where text, production_rate text, distance text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM from_where")
        rows = self.cur.fetchall()
        return rows

    def insert(self, from_where, to_where, production_rate, distance):
        self.cur.execute("INSERT INTO from_where VALUES (NULL, ?, ?, ?, ?)",
                         (from_where, to_where, production_rate, distance))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM from_where WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, from_where, to_where, production_rate, distance):
        self.cur.execute("UPDATE from_where SET from_where = ?, to_where = ?, production_rate = ?, distance = ? WHERE id = ?",
                         (from_where, to_where, production_rate, distance, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


