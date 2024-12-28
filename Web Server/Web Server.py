from flask import Flask, render_template
import requests

app = Flask(__name__)

# Генерация случайного профиля через API
def generate_profile():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        data = response.json()['results'][0]
        profile = {
            "name": f"{data['name']['first']} {data['name']['last']}",
            "date_of_birth": data['dob']['date'].split('T')[0],
            "address": f"{data['location']['street']['name']}, {data['location']['street']['number']}, {data['location']['city']}",
            "phone": data['phone'],
            "color": "LightYellow",  # Замените, если нужен рандом
            "login": data['login']['username'],
            "password": data['login']['password'],
            "photo_url": data['picture']['large']
        }
        return profile
    else:
        # На случай, если API недоступен
        return {
            "name": "Ошибка генерации",
            "date_of_birth": "Неизвестно",
            "address": "Неизвестно",
            "phone": "Неизвестно",
            "color": "Неизвестно",
            "login": "error",
            "password": "error",
            "photo_url": "https://via.placeholder.com/150"
        }

# Главная страница с генерацией профиля
@app.route('/')
def home():
    profile = generate_profile()
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
