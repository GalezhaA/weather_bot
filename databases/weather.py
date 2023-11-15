import sqlite3


class BotDB:
    def __init__(self):
        self.db = sqlite3.connect('/home/artyom/pets/PetBotTG/databases/weather.db')
        self.cursor = self.db.cursor()

    def start_db(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS weather_search_history("
                           "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                           "user_id INTEGER,"
                           "city TEXT,"
                            "date TEXT default)"
                            )
        self.db.commit()

    def add_user(self, user_id: int):
        user = self.cursor.execute(f"SELECT * FROM main_balance WHERE user_id == {user_id}").fetchone()
        if not user:
            self.cursor.execute(
                f"INSERT INTO main_balance(user_id, balance) VALUES ({user_id}, 0)"
            )
            self.db.commit()

    def plus_balance(self, user_id: int, money: int):
        self.cursor.execute(f"UPDATE main_balance SET balance = balance + {money} WHERE user_id = {user_id}")
        self.db.commit()

    def minus_balance(self, user_id: int, money: int):
        self.cursor.execute(f"UPDATE main_balance SET balance = balance - {money} WHERE user_id = {user_id}")
        self.db.commit()

    def get_balance(self, user_id: int):
        balance = self.cursor.execute(f"SELECT balance FROM main_balance WHERE user_id == {user_id}").fetchone()
        return balance


tg = BotDB()
tg.plus_balance(2, 1000)