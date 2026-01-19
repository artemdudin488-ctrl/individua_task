"""
ИНДИВИДУАЛЬНЫЕ ПРАВКИ, ДУДИН АРТЕМ
анализ платежных методов
круговая диаграмма распределения способов оплаты
"""

import matplotlib.pyplot as plt
import pandas as pd
from config import PLOT_CONFIG
from utils import show_plot


def plot_payment_methods(df):
    """круговая диаграмма распределения платежных методов"""

    # считаем количество транзакций по каждому методу оплаты
    payment_counts = df['PaymentMode'].value_counts()

    # создаем квадратный график для круговой диаграммы
    fig, ax = plt.subplots(figsize=(8, 8))

    # цвета для секторов
    colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']

    # рисуем круговую диаграмму
    wedges, texts, autotexts = ax.pie(payment_counts.values,
                                      labels=payment_counts.index,
                                      autopct='%1.1f%%',
                                      colors=colors,
                                      startangle=90)

    ax.set_title('Распределение способов оплаты',
                 fontsize=14, fontweight='bold')

    # настраиваем отображение процентов
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')

    # добавляем легенду
    ax.legend(wedges, payment_counts.index,
              title="Способы оплаты",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.tight_layout()
    show_plot(fig, 'Распределение способов оплаты')