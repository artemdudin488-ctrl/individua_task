"""
ИНДИВИДУАЛЬНЫЕ ПРАВКИ, АРТЕМ ДУДИН

анализ прибыльности товаров
топ наиболее и наименее прибыльных товаров
"""

import matplotlib.pyplot as plt
import pandas as pd
from config import PLOT_CONFIG, TOP_N
from utils import show_plot, format_currency


def plot_profit_top(df, mode='top'):
    """
    столбчатая диаграмма топ-5 по прибыльности

    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame с данными
    mode : str
        'top' - наиболее прибыльные
        'bottom' - наименее прибыльные
    """

    # группируем по подкатегориям, суммируем прибыль
    profit_by_subcategory = df.groupby('Sub-Category')['Profit'].sum()

    # выбираем топ или bottom в зависимости от режима
    if mode == 'top':
        data = profit_by_subcategory.nlargest(TOP_N).sort_values(ascending=True)
        title = f'Топ-{TOP_N} наиболее прибыльных подкатегорий'
        color = '#2ecc71'  # зеленый
    else:  # mode == 'bottom'
        data = profit_by_subcategory.nsmallest(TOP_N).sort_values(ascending=True)
        title = f'Топ-{TOP_N} наименее прибыльных подкатегорий'
        color = '#e74c3c'  # красный

    # создаем график
    fig, ax = plt.subplots(figsize=PLOT_CONFIG['figsize'])

    # рисуем горизонтальные столбцы
    bars = ax.barh(data.index.astype(str), data.values,
                   color=color, alpha=0.7)

    # добавляем значения на столбцы
    for bar in bars:
        width = bar.get_width()

        # определяем позицию текста (слева для положительных, справа для отрицательных)
        if width >= 0:
            ha = 'left'
            x_pos = width
        else:
            ha = 'right'
            x_pos = width

        ax.text(x_pos, bar.get_y() + bar.get_height() / 2,
                format_currency(width),
                ha=ha, va='center', fontsize=10)

    # добавляем вертикальную линию на ноль для bottom графика
    if mode == 'bottom' and any(data.values < 0):
        ax.axvline(x=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)

    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Прибыль ($)')
    ax.grid(True, alpha=0.3, axis='x')

    plt.tight_layout()
    show_plot(fig, title)


def show_profit_menu(df):
    """показывает подменю для анализа прибыльности"""

    while True:
        print("\nАНАЛИЗ ПРИБЫЛЬНОСТИ")
        print("=" * 35)
        print("1. Топ-5 наиболее прибыльных подкатегорий")
        print("2. Топ-5 наименее прибыльных подкатегорий")
        print("0. Назад в главное меню")

        choice = input("\nВыберите опцию: ").strip()

        if choice == "1":
            plot_profit_top(df, mode='top')
            return

        elif choice == "2":
            plot_profit_top(df, mode='bottom')
            return

        elif choice == "0":
            return

        else:
            print("Неверный выбор. Попробуйте еще раз.")
            input("Нажмите Enter чтобы продолжить...")