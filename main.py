"""
выполнил Дудин Артем
главный файл программы
запускает загрузку данных и интерфейс пользователя
"""

import os
import sys

# добавляем текущую директорию в путь для импорта модулей
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_loader import load_and_prepare_data
from interface import get_user_choice
from config import DATA_PATH


def main():
    """основная функция программы"""
    print("\n" + "=" * 50)
    print("ЗАПУСК ВИЗУАЛИЗАТОРА ПРОДАЖ")
    print("=" * 50)

    try:
        # загружаем данные из файла
        df = load_and_prepare_data(DATA_PATH)

        # запускаем интерфейс пользователя
        get_user_choice(df)

    except FileNotFoundError:
        print(f"Ошибка: Файл данных не найден по пути: {DATA_PATH}")
        print("Пожалуйста, убедитесь, что файл Sales_data.csv находится в папке data/")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()