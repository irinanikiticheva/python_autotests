import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '80833f69e9396f3a57b925ced70efaac'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
trainer_id = 6952

def test_status_code():
    response = requests.get(url=f'{URL}trainers', params={'trainer_id': trainer_id})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}trainers', params={'trainer_id': trainer_id})
    assert response_get.json()["data"][0]["trainer_name"] == 'Хоттабыч'
