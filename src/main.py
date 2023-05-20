from functions import from_json_data, get_iso_date, format_data

"""Импортируем все функции и присваиваем переменной значение функции"""
list_of_operations = from_json_data()
"""Перебираем каждый список и если он соответсвует требованиям, добавляем его в list_exexuted """
list_executed = [operation for operation in list_of_operations if operation and operation['state'] == 'EXECUTED']

sorted_executed_list = sorted(list_executed, key=get_iso_date, reverse=True)
"""Сортируем наш список"""
for operation in sorted_executed_list[:5]:
    """И выводим пять новых операций по картам"""
    print(format_data(operation))
    print()