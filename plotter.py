import csv
from typing import List, Dict, Union


def parse_csv_to_array(file_path: str) -> List[Dict[str, Union[float, int]]]:
    """
    Функция преобразования файла csv в массив словарей с ключами 'delta' и 't'.
    :param file_path: Путь к файлу переходного процесса
    :return: Массив словарей с ключами 'delta' и 't'
    """
    data = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')

            t_value = 0.0
            for row in reader:
                if 'delta' in row:
                    try:
                        value = float(row['delta'].replace(',', '.'))
                        data.append({'delta': value, 't': round(t_value, 2)})
                        t_value += 0.01  # Увеличиваем t на 0.01
                    except ValueError as ve:
                        print(f"Ошибка преобразования значения '{row['delta']}': {ve}")

    except FileNotFoundError:
        print(f"Файла '{file_path}' не существует")

    except Exception as e:
        print(f"Ошибка: {e}")

    return data

if __name__ == '__main__':
    print(parse_csv_to_array("C:\\Users\\Umaro\\OneDrive\\Рабочий стол\\test (3).csv"))