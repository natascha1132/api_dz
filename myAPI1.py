import requests

name = input()
url = f"https://api.genderize.io/?name={name}"

response = requests.get(url)
data = response.json()

if data['gender']:
    print(f"имя {name} принадлежит {data['gender']} с вероятностью {data['probability']}")
else:
    print(f"Я не знаю, что это за имя- {name}")