from flask import Flask, url_for, request
import requests

server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
geocode = 'Красная площадь 1'
# Готовим запрос.
geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&format=json'

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа, он находится по следующему пути:
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Полный адрес топонима:
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
app = Flask(__name__)


@app.route('/<name>')
def return_sample_page(name):
    print(toponym_address)
    if name == 'вася':
        name = 'Машу'
    else:
        name = 'Васю'
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>я хороший</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Пожалуйста, возьмите меня и {name} в IT класс</h1>
                    <img src="{url_for('static', filename='gerb.webp')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-danger" role="alert">
                            Мы очень умные
                    </div>
                    <div class="alert alert-warning" role="alert">
                            И способные
                    </div>
                    <div class="alert alert-success" role="alert">
                        А главное:
                    </div>
                     <div class="alert alert-info" role="alert">
                        Любим информатику!
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run()