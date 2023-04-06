"""В этом файле описаны все функции взаимодействия с таблицами БД"""

from sqlalchemy import (
    and_,
    or_,
    desc,
    select,
)
from .models import *

import func

# Для добавления в базу 20 котят
def insert_data():
    with engine.begin() as connection:
        ins_1 = cats.insert().values(
            age = 5,
            breed = 'British',
            description = 'Evil cat',
            name = "Sima",
            picture = "Sima.png"
        )

        ins_2 = cats.insert().values(
            age = 2,
            breed = 'British',
            description = 'Good cat',
            name = "Barsik",
            picture = "Barsik.png"
        )

        ins_3 = cats.insert().values(
            age = 3,
            breed = 'Sphinx',
            description = 'Bald cat',
            name = "Kuzja",
            picture = "Kuzja.png"
        )

        ins_4 = cats.insert().values(
            age = 7,
            breed = 'Pers',
            description = 'Soft cat',
            name = "Mila",
            picture = "Mila.png"
        )

        ins_5 = cats.insert().values(
            age = 4,
            breed = 'Sphinx',
            description = 'afraid cat',
            name = "Sky",
            picture = "Sky.png"
        )

        ins_6 = cats.insert().values(
            age = 1,
            breed = 'Sphinx',
            description = 'Bad cat',
            name = "Thomas",
            picture = "Thomas.png"
        )

        ins_7 = cats.insert().values(
        age = 7,
        breed = 'British',
        description = 'brave cat',
        name = "Simon",
        picture = "Simon.png"
        )

        ins_8 = cats.insert().values(
        age = 2,
        breed = 'Australian Mist',
        description = 'clever cat',
        name = "Ryan",
        picture = "Ryan.png"
        )

        ins_9 = cats.insert().values(
        age = 3,
        breed = 'British',
        description = 'curious cat',
        name = "Oscar",
        picture = "Oscar.png"
        )

        ins_10 = cats.insert().values(
        age = 5,
        breed = 'Australian Mist',
        description = 'difficult cat',
        name = "Martin",
        picture = "Martin.png"
        )

        ins_11 = cats.insert().values(
        age = 4,
        breed = 'Asian cat',
        description = 'fast cat',
        name = "Leo",
        picture = "Leo.png"
        )

        ins_12 = cats.insert().values(
        age = 7,
        breed = 'Bengal cat',
        description = 'funny cat',
        name = "Logan",
        picture = "Logan.png"
        )

        ins_13 = cats.insert().values(
        age = 7,
        breed = 'British',
        description = 'huge cat',
        name = "Kester",
        picture = "Kester.png"
        )

        ins_14 = cats.insert().values(
        age = 9,
        breed = 'Asian cat',
        description = 'little cat',
        name = "Alvin",
        picture = "Alvin.png"
        )
        
        ins_15 = cats.insert().values(
        age = 2,
        breed = 'British',
        description = 'nice cat',
        name = "Lily",
        picture = "Lily.png"
        )

        ins_16 = cats.insert().values(
        age = 1,
        breed = 'Bengal cat',
        description = 'quiet cat',
        name = "Latesha",
        picture = "Latesha.png"
        )

        ins_17 = cats.insert().values(
        age = 1,
        breed = 'British',
        description = 'small cat',
        name = "Leona",
        picture = "Leona.png"
        )

        ins_18 = cats.insert().values(
        age = 8,
        breed = 'Burmilla',
        description = 'wicked cat',
        name = "Bella",
        picture = "Bella.png"
        )

        ins_19 = cats.insert().values(
        age = 4,
        breed = 'British',
        description = 'Evil cat',
        name = "Aurora",
        picture = "Aurora.png"
        )

        ins_20 = cats.insert().values(
        age = 7,
        breed = 'Burmilla',
        description = 'bright cat',
        name = "Ada",
        picture = "Ada.png"
        )

        connection.execute(ins_1)
        connection.execute(ins_2)
        connection.execute(ins_3)
        connection.execute(ins_4)
        connection.execute(ins_5)
        connection.execute(ins_6)
        connection.execute(ins_7)
        connection.execute(ins_8)
        connection.execute(ins_9)
        connection.execute(ins_10)
        connection.execute(ins_11)
        connection.execute(ins_12)
        connection.execute(ins_13)
        connection.execute(ins_14)
        connection.execute(ins_15)
        connection.execute(ins_16)
        connection.execute(ins_17)
        connection.execute(ins_18)
        connection.execute(ins_19)
        connection.execute(ins_20)

    return 'completed'


# Функция для поиска определенного котенка по имени
def select_cat(name: str) -> dict:

    sel = cats.select().where(cats.c.name == name)
    conn = engine.connect()
    result = conn.execute(sel).fetchone()
    conn.close()
    if result == None:
        return 'there is no such cat'
    return dict(result)

# Функция по выдаче лимитированного запроса в 5 котиков
def select_all_cat(num_page: str) -> list:

    sel = cats.select().limit(5).offset((int(num_page) * 5) - 5)
    conn = engine.connect()
    data = conn.execute(sel).fetchall()
    conn.close()
    if data == []:
        return 'cats ran out'
    result = []
    for dat in data:
        result.append(dict(dat))

    return result


# Функция для поиска, выдает данные по всей базе и выдает словарь
# где ключи это id котов а значения это словарь со всей информацией по коту
def select_all_cat_search() -> dict:
    
    sel = cats.select()
    conn = engine.connect()
    data = conn.execute(sel).fetchall()
    conn.close()
    dict_cat = {}
    for dat in data:
        dat = dict(dat)
        dict_cat[dat['id']] = dat
    return dict_cat


# Функция по обработке поискового запроса, в зависимости от type(которая отвечает за фильтрацию),
#  в функцию приходит tuple где первое значение это id кота а второе значение то как часто он встречается 
#  отсортированно заранее, поэтому в список просто загоняются словари с данными котов 
def select_search(data: list, type: str) -> dict:
    with engine.begin() as connection:
        result = []
        if type == '0':
            for dat in data:
                sel = cats.select().where(cats.c.id == dat[0])
                sel_dict = dict(connection.execute(sel).fetchone())
                result.append(sel_dict)
        elif type == '1':
            res = {}
            for dat in data:
                sel = cats.select().where(cats.c.id == dat[0])
                sel_dict = dict(connection.execute(sel).fetchone())
                res[sel_dict['id']] = sel_dict['breed']
            sort = func.sort_dictionary(res, type)
            for dat in sort:
                sel = cats.select().where(cats.c.id == dat[0])
                sel_dict = dict(connection.execute(sel).fetchone())
                result.append(sel_dict)
        elif type == '2':
            res = {}
            for dat in data:
                sel = cats.select().where(cats.c.id == dat[0])
                sel_dict = dict(connection.execute(sel).fetchone())
                res[sel_dict['id']] = sel_dict['age']
            sort = func.sort_dictionary(res, type)
            for dat in sort:
                sel = cats.select().where(cats.c.id == dat[0])
                sel_dict = dict(connection.execute(sel).fetchone())
                result.append(sel_dict)

    return result