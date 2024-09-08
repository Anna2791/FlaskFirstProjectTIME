# Задание 1
# Создайте новое приложение Flask, которое будет отображать текущие дату и время на главной странице.

# from flask import Flask
# from datetime import datetime
#
# app = Flask(__name__)
# @app.route('/')
# def show_time():
#     # Получаем текущие дату и время
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     # Возвращаем их в виде строки
#     return f"Текущие дата и время: {current_time}"
#
# if __name__ == '__main__':
#     app.run(debug=True)