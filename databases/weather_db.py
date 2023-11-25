"""
Создание БД, подключение ОРМ, определение модели

"""
import datetime
from typing import List
from peewee import *

db = SqliteDatabase('/home/artyom/python_basic_diploma/databases/weathercityhistory.db')


class BaseModel(Model):
    class Meta:
        database = db


class HistoryDataModel(BaseModel):
    """
    Класс для взаимодействия с БД
    """
    tg_id = IntegerField()
    data = TextField()
    date = DateTimeField(null=False, default=datetime.datetime.now())

    @classmethod
    def add_data(cls, tg_id: int, data: str) -> None:
        """
        Добавляет информацию о пользователе и его запросах
        :param tg_id: int
        :param data: str
        :return: None
        """
        HistoryDataModel.create(tg_id=tg_id, data=data)

    @classmethod
    def find_user(cls, user_id: int) -> List:
        """
        Определяет, есть ли пользователь в БД
        :param user_id: int
        :return:
        """
        with db:
            users = HistoryDataModel.select(
            ).where(HistoryDataModel.tg_id == user_id
                    ).order_by(HistoryDataModel.date.asc()
                               ).limit(10)

            if len(users) == 0:
                return ['У вас ещё не было запросов']
            else:
                data_list = []
                for user in users:
                    data_list.append(user.data)
                return data_list
