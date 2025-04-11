from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/<name>')
def return_sample_page(name):
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
                    <h2>А это жизненно<h2>
                    <p>Встречаются два программиста:</p>
                    <p>— Представляешь, вчера работал над проектом, и комп завис.</p>
                    <p>— Что сделал?</p>
                    <p>— Конечно, перезагрузил! Теперь жду, пока реальность тоже перезагрузится, а то что-то не работает.</p>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)