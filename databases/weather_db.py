"""
Создание БД, подключение ОРМ, определение модели

"""
import datetime
from typing import List
from peewee import *

db = SqliteDatabase('/home/artyom/python_basic_diploma/databases/weathercityhistory.db')


class User(Model):
    """
    Класс для взаимодействия в БД
    """
    class Meta:
        database = db

    tg_id = IntegerField()
    first_name = CharField(default='Hello')
    data = TextField()
    date = DateTimeField(null=False, default=datetime.datetime.now())

    @classmethod
    def add_data(cls, name: str, tg_id: int, data: str) -> None:
        """
        Добавляет информацию о пользователе и его запросах
        :param name: str
        :param tg_id: int
        :param data: str
        :return: None
        """
        User.create(first_name=name, tg_id=tg_id, data=data)

    @classmethod
    def find_user(cls, user_id: int) -> List:
        """
        Определяет, есть ли пользователь в БД
        :param user_id: int
        :return:
        """
        with db:
            users = User.select().where(User.tg_id == user_id).order_by(User.date.desc()).limit(10)

            if len(users) == 0:
                return ['У вас ещё не было запросов']
            else:
                data_list = []
                for user in users:
                    data_list.append(user.data)
                return data_list





