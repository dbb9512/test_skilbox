from flask import Flask, request, jsonify, abort
from sql_app import crud
import func

app = Flask(__name__)


@app.route("/api/v1/createDB", methods=['GET'])
def create_DB():
    """Эндпоинт для создания базы
        params:
            num_page: str
    """

    result = crud.insert_data()

    return jsonify(result)

''
@app.route("/api/v1/getCatsInfo/<num_page>", methods=['GET'])
def get_cats_info(num_page):
    """Эндпоинт по выдаче всех котиков лимитированно по 5 котиков на страницу
        params:
            num_page: str
    """

    result = crud.select_all_cat(num_page)

    return jsonify(result)


@app.route("/api/v1/getCatInfo/<name>", methods=['GET'])
def get_cat_info(name):
    """Эндпоинт для получения информации по каждому коту, реализует требование по переходу на
        вторую страницу, на фронте к каждому коту было подцеплено имя м они переходили бы по имени
        отдает всю имеющуюся информацию по определенному коту
        params:
            name: str
    """

    result = crud.select_cat(name)

    return jsonify(result)


@app.route("/api/v1/getSearchInfo/<search>/<type>", methods=['GET'])
def get_search_info(search, type):
    """Эндпоинт для поисковой строки, в search отправляется запрос через пробелы 
    type отвечате за фильтрацию поиска
    type = 0 фильтрация по релевантности(по умолчанию)
    type = 1 фильтрация по породе(все одинаковые породы ставит вместе и по алфавиту)
    type = 2 филтрация по возрасту(от меньшего возраста к большему)
        params:
            search: str
            type: str
    """
    search = search.split(' ')
    data_dict = crud.select_all_cat_search()
    count_coinc = func.count_coincidences(data_dict, search)
    result = crud.select_search(count_coinc, type)
    return jsonify(result)
''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

