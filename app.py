from flask import Flask, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
from plotter import parse_csv_to_array
from flask_cors import CORS

import matplotlib
matplotlib.use('Agg')
app = Flask(__name__)
CORS(app)

@app.route('/plot', methods=['POST'])
def plot():
    """
    Функция представление построения графика
    :return: JSON типа {"message": "График сохранен", "file": Путь к графику}
    """
    try:
        # Получаем данные из запроса
        path = request.json['path']

        # Преобразуем в массив
        data = parse_csv_to_array(path)

        # Преобразуем данные в DataFrame
        df = pd.DataFrame(data)

        # Разделяем данные по времени
        prediction_window = df[df['t'] <= 0.4]
        forecast_window = df[df['t'] > 0.4]

        # Генерируем график
        plt.figure(figsize=(10, 5))
        plt.plot(prediction_window['t'], prediction_window['delta'], linewidth=3,
                 color='royalblue', label='Окно наблюдения')

        plt.plot(forecast_window['t'], forecast_window['delta'], linewidth=3,
                 color='sandybrown', label='Окно прогноза')

        plt.xlabel('Время, с')
        plt.ylabel('Угол, град')
        plt.grid()
        plt.legend()  # Добавляем легенду

        # Сохраняем график
        filepath = 'C:\\Users\\Umaro\\PycharmProjects\\NeRO\\nero_app\\static\\plots\\plot.png'
        plt.savefig(filepath)
        plt.close()

        return jsonify(message="График сохранен", file=filepath), 200

    except Exception as e:
        return jsonify(error=str(e)), 400


if __name__ == '__main__':
    app.run(port=7123)