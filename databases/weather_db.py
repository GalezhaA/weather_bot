from typing import List

from peewee import *

db = SqliteDatabase('databases/weathercityhistory.db')


class User(Model):
    class Meta:
        database = db

    tg_id = IntegerField()
    first_name = CharField(default='Hello')
    data = TextField()

    @classmethod
    def add_data(cls, name: str, tg_id: int, data: str) -> None:
        User.create(first_name=name, tg_id=tg_id, data=data)

    @classmethod
    def find_user(cls, user_id: int) -> List:
        with db:
            users = User.select().where(User.tg_id == user_id)

            if len(users) == 0:
                return ['У вас ещё не было запросов']
            else:
                data_list = []
                for user in users:
                    data_list.append(user.data)
                return data_list

#
# db.connect()
#
# db.create_tables([User])
#
# a = User()
#
# print(a.find_user(1))

