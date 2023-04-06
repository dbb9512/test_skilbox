
# Функция для проверки количесво вхождений запроса, в цикл помещаются все словари БД
# после проверяется есть ли в значениях словарей совпадение, если есть то подсчитывается количество совпадений,
# после это загоняется в словарь где ключ это id кота где были совпадения, а значение количество совпадений
def count_coincidences(data: dict, search: list) -> list:
    res = {}
    for dic in data:
        amount = 0
        for var in data[dic]:
            for val in search:
                count = str(data[dic][var]).count(str(val))
                if count != 0:
                    amount += 1
        if amount != 0:
            res[str(data[dic]['id'])] = amount

    return sort_dictionary(res, '0')


# Функция для сортировки словаря по значениям, в зависимости от типа, разворачиваем список или нет
def sort_dictionary(dictionary: dict, type: str) -> list:
    if type == '0':

        return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    else:

        return sorted(dictionary.items(), key=lambda item: item[1], reverse=False)