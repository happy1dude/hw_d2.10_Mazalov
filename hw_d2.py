#Импортируем sentry и bottle
import sentry_sdk
import os
from bottle import Bottle, request, route, run, response
from sentry_sdk.integrations.bottle import BottleIntegration

#Инициализируем sentry с нашими данными
sentry_sdk.init(
    dsn="https://957ad00809604c76afc011d7b8b34f31@o485517.ingest.sentry.io/5540996",
    integrations=[BottleIntegration()]
)

app = Bottle()

#Создаём нужные маршруты
#Основная страница с выбором маршрута
@app.route('/')
def index():
    htmlCode = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>D2.10_HW Mazalov.N.A </title>
    </head>
    <body>
        <h1>Ниже выберете нужный вариант</h1>
        <h2><a href='http://localhost:8080/success'>Соединение установлено</a></h2>
        <h2><a href='http://localhost:8080/fail'>Ошибка сервера</a></h2>
    </body>
</html>
    """
    return htmlCode
#Страница со статусом 200ОК
@app.route('/success')
def successMes():
    return 'HTTP статус - {status}'.format(status=response.status)

#Страница с ошибкой
@app.route('/fail')
def failMess():
    raise RuntimeError("There is an error! Vol.2")
    return 


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)