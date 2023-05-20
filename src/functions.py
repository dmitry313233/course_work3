import json
import os
from datetime import date, datetime

PROJECT_PATH = os.path.abspath('..')
PATH_TO_JSON = os.path.join(PROJECT_PATH, 'src', 'operations.json')

def from_json_data():
    with open(PATH_TO_JSON, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def get_iso_date(operation):
    splitted_date, splitted_time = operation['date'].split('T')
    iso_date = date.fromisoformat(splitted_date)
    return iso_date


def format_data(operation: dict) -> str:
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
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')

#print(reformed_date("2019-07-13T18:51:29.313309"))
def get_blure_number(card: str):
    card, number = card.rsplit(" ", 1)
    if len(number) == 16:
        number = list(number)
        number[6:12] = ['*'] * 6
        for i in range(1, len(number) + 1):
            if i % 4 == 0:
                number[i - 1] += " "
        return card + ' ' + ''.join(number)
    elif len(number) == 20:
        number = '**' + number[-4:]
        return card + " " + number

#print(get_blure_number('Счет 44812258784861134719'))

#def show(operation_info) -> str:
    # получение отформатированой даты(метод strftime())  1 функция
    # отличить счет от карты и создать ***, отформатировать  2 функция
    # получение стоимости с учетом курса  3 функция




# def get_masked_card_number(card_number: str) -> str:
#     return f"{card_number[:6]} {'*' * 8} {card_number[-4:]}"
#
#
# def get_masked_account_number(account_number: str) -> str:
#     return f"**{account_number[-4:]}"
#
#
# def format_operation_date(date_str: str) -> str:
#     date = datetime.strftime(date_str, '%Y-%m-%d %H:%S.%f')
#     return date.strftime('%d,%m.%Y')
#
#
# def format_operation(operation: dict) -> str:
#     date = format_operation_date(operation['date'])
#     description = operation['description']
#     from_ = operation.get('from', '')
#     to = operation['to']
#     amount = operation['operationAmount']['amount']
#     currency = operation['operationAmount']['currency']
#
#     formatted_from = get_masked_card_number(from_) if from_ else ''
#     formatted_to = get_masked_account_number(to)
#
#     return f"{date} {description}\n{formatted_from} -> {formatted_to}\n{amount} {currency}"