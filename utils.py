"""
выполнил Дудин Артем
вспомогательные утилиты для работы с графиками
содержит функции для отображения и форматирования
"""

import matplotlib.pyplot as plt
import os  # ДОБАВЛЯЕМ ИМПОРТ ОС
from datetime import datetime  # ДОБАВЛЯЕМ ЛОЯ ГЕНЕРАЦИИ ИМЕН СОХРАНЯЕМЫХ ФАЙЛОВ



def show_plot(fig, title):
    """
    показывает график пользователю,
    ждет, пока пользователь закроет окно графика
    """
    save_plot(fig, title) # ВЫЗЫВАЕМ НОВУЮ ФУНКЦИЮ

    print(f"✓ График отображен: {title}")
    print("Закройте окно графика, чтобы продолжить...")

    # показываем график и ждем закрытия окна
    plt.show(block=True)

    return None


def format_currency(value):
    """форматирует число как валюту (краткий формат)"""
    if value >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    elif value >= 1_000:
        return f"${value / 1_000:.0f}K"
    else:
        return f"${value:,.0f}"


# НОВАЯ ФУНКЦИЯ
def save_plot(fig, title):
    """сохраняет график в папку plots"""

    # создаем папку plots, если ее нет
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # генерируем имя файла: удаляем недопустимые символы
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()

    # добавляем временную метку для уникальности
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"plots/{timestamp}_{safe_title[:50]}.png"

    # сохраняем график
    fig.savefig(filename, dpi=100, bbox_inches='tight')
    print(f"✓ График сохранен: {filename}")