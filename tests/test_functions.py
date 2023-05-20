from src.functions import *
import pytest


@pytest.fixture
def operation_data() -> list:
    return from_json_data()



def test_from_json_data():
    assert type(from_json_data()) == list


def test_get_iso_date(operation_data):
    assert type(get_iso_date(operation_data[0])) == date


def test_format_data(operation_data):
    assert type(format_data(operation_data[0])) == str


def test_reformed_date():
    assert reformed_date("2019-07-13T18:51:29.313309") == '13.07.2019'


def test_get_blure_number():
    assert get_blure_number('Счет 44812258784861134719') == 'Счет **4719'
