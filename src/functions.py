import json
import os
from datetime import date, datetime

PROJECT_PATH = os.path.abspath('..')
PATH_TO_JSON = os.path.join(PROJECT_PATH, 'src', 'operations.json')

def from_json_data():
    with open(PATH_TO_JSON, 'r', encoding='UTF-8') as file:
        """Создаём переменную для сохранения в неё json файла"""
        data = json.load(file)
    return data


def get_iso_date(operation):
    """В этой функции получаем строку по ключу 'date' в словаре и с помощью функции получаем два значения"""
    splitted_date, splitted_time = operation['date'].split('T')
    """С помощью функции преобразуем строку в особый формат и записываем его в переменую"""
    iso_date = date.fromisoformat(splitted_date)
    return iso_date


def format_data(operation: dict) -> str:
    """В этой функции получаем строки которые нам нужны обращаясь к словарю по ключам"""
    date = operation.get('date')
    description = operation.get('description')
    sender = operation.get('from', '')
    to = operation.get('to')
    amount = operation.get('operationAmount').get('amount')
    currency = operation.get('operationAmount').get('currency').get('name')
    if sender: 
        sender = get_blure_number(sender)[:-1]
    to = get_blure_number(to)[:-1]
    return f"{reformed_date(date)} {description} \n " \
           f"{sender} -> {to} \n " \
           f"{amount} {currency}"


def reformed_date(date):
    """В этой функции преобразуем дату и время в определённый тип даты в той последовательности которой нам нужно"""
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')


def get_blure_number(card):
    """В этой функции мы разделяем карту и счет, преобразуем в список и изменяем значения по индексам"""
    card, number = card.rsplit(" ", 1)
    if len(number) == 16:
        number = list(number)
        number[6:12] = ['*'] * 6
        for i in range(1, len(number) + 1):
            if i % 4 == 0:
                number[i - 1] += " "
                """"Возвращаем строку с помощью метода join"""
        return card + ' ' + ''.join(number)
    elif len(number) == 20:
        number = '**' + number[-4:]
        return card + " " + number