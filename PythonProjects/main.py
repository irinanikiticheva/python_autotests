import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '808333f69e9396f3a57b925ecd70fa4c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "irinanickiticheva@yandex.ru",
    "password": "1404_Margo"
}

body_confirmation = {
"trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "100868",
    "name": "Алешка",
    "photo_id": 2
}

body_pokeboll = {
    "pokemon_id": "66499"
}
responce = requests.post(url = f'{URL}trainers/reg', headers = HEADER, json = body_registration)
print(responce.text)

responce_confirmation = requests.post(url = f'{URL}trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(responce_confirmation.text)

responce_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create)
print(responce_create.status_code)

responce_change = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_change)
print(responce_change.text)

responce_pokeboll = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(responce_pokeboll.text)