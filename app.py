from flask import Flask, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)


@app.route('/plot', methods=['POST'])
def plot():
    try:
        # Получаем данные из запроса
        data = request.get_json()

        # Преобразуем данные в DataFrame
        df = pd.DataFrame(data)

        # Генерируем график
        plt.figure(figsize=(10, 5))
        plt.plot(df['t'], df['delta'], marker='o')
        plt.xlabel('Время, мс')
        plt.ylabel('Угол, град')
        plt.grid()

        # Сохраняем график
        filepath = 'plot.png'
        plt.savefig(filepath)
        plt.close()

        return jsonify(message="График сохранен", file=filepath), 200

    except Exception as e:
        return jsonify(error=str(e)), 400


if __name__ == '__main__':
    app.run(port=8080)