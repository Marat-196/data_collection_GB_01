import requests
import json

val = input("Введите категорию поиска: ")


url = "https://api.foursquare.com/v3/places/search"

params = {
    "query": val
}

headers = {
    "accept": "application/json",
    "Authorization": "fsq3YW7XKLfdoXm3kTdb5Oh9VmCfBfZtHbi86d4D2G/Gy/4="}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Подключение API успешно!")
    print('-' * 35)
    j_data = response.json()
    for name in j_data.get("results"):
        print("Наименование: ", name.get("name"))
        print("Адрес: ", name.get("location").get("region"),
              name.get("location").get("locality"),
              name.get("location").get("address"))
        print('-' * 35)
else:
    print("Подключение не выполнено с кодом", response.status_code)

