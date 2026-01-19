"""
выполнила Черник Полина
анализ клиентской базы
топ клиентов по сумме покупок с детальной статистикой
"""

import matplotlib.pyplot as plt
import pandas as pd
from config import PLOT_CONFIG, TOP_N
from utils import show_plot, format_currency


def plot_top_customers(df):
    """анализ лучших клиентов - топ-5 по общей сумме покупок"""

    # группируем данные по имени клиента, агрегируем метрики
    customer_stats = df.groupby('CustomerName').agg({
        'Amount': 'sum',  # общая сумма покупок
        'Order ID': 'nunique',  # количество заказов
        'Profit': 'sum'  # общая прибыль
    }).reset_index()

    # переименовываем столбцы
    customer_stats.columns = ['Customer', 'Total Amount', 'Orders Count', 'Total Profit']

    # выбираем топ-5 клиентов по общей сумме
    top_5_customers = customer_stats.nlargest(TOP_N, 'Total Amount')

    # создаем график
    fig, ax = plt.subplots(figsize=(12, 6))

    # столбчатая диаграмма
    bars = ax.bar(range(TOP_N), top_5_customers['Total Amount'],
                  color='#9b59b6', alpha=0.7)

    ax.set_title('Топ-5 клиентов по сумме заказов', fontsize=14, fontweight='bold')
    ax.set_xlabel('Клиент')
    ax.set_ylabel('Общая сумма ($)')

    # настраиваем метки на оси X (имена клиентов)
    ax.set_xticks(range(TOP_N))
    ax.set_xticklabels(top_5_customers['Customer'],
                       rotation=45,
                       ha='right')
    ax.grid(True, alpha=0.3, axis='y')

    # добавляем значения поверх столбцов
    for bar, amount in zip(bars, top_5_customers['Total Amount']):
        ax.text(bar.get_x() + bar.get_width() / 2., amount,
                format_currency(amount),
                ha='center', va='bottom', fontsize=9)

    plt.tight_layout()

    # показываем график
    show_plot(fig, 'Анализ топ-клиентов')

