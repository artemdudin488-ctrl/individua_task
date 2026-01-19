"""
выполнил Насенников Максим
главный интерфейс программы
управляет меню и навигацией между модулями анализа
"""

import pandas as pd
import matplotlib.pyplot as plt

# импортируем модули анализа из папки modules
from modules import (
    revenue_time,  # анализ по времени
    category_analysis,  # анализ категорий товаров
    geo_analysis,  # анализ по географии
    customer_analysis, # анализ клиентов
    payment_analysis, # НОВЫЙ МОДУЛЬ анализ методов платежей
    profit_top # НОВЫЙ МОДУЛЬ анализ прибыльности подкатегорий
    )


def clear_screen():
    """очищает экран консоли"""
    import os
    # для windows команда 'cls', для linux/mac - 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')


def show_revenue_menu(df):
    """показывает подменю для анализа выручки по времени"""

    while True:
        clear_screen()
        print(
            f"\nАНАЛИЗ ВЫРУЧКИ ПО ВРЕМЕНИ (доступны данные о периоде: {df['Order Date'].min().date()} - {df['Order Date'].max().date()})")
        print("1. Выручка по дням")
        print("2. Выручка по неделям")
        print("3. Выручка по месяцам")
        print("0. Назад в главное меню")

        sub_choice = input("\nВыберите опцию: ").strip()

        if sub_choice == "1":
            revenue_time.plot_daily_revenue(df)
            continue

        elif sub_choice == "2":
            revenue_time.plot_weekly_revenue(df)
            continue

        elif sub_choice == "3":
            revenue_time.plot_monthly_revenue(df)
            continue

        elif sub_choice == "0":
            return  # возвращаемся в главное меню

        else:
            print("Неверный выбор. Попробуйте еще раз.")
            input("Нажмите Enter чтобы продолжить...")


def show_category_menu(df):
    """показывает подменю для анализа категорий товаров"""

    while True:
        clear_screen()
        print("\nАНАЛИЗ КАТЕГОРИЙ И ПОДКАТЕГОРИЙ")
        print("1. Выручка по категориям (круговая диаграмма)")
        print("2. Топ-5 подкатегорий по выручке")
        print("3. Топ-5 подкатегорий по прибыли")
        print("0. Назад в главное меню")

        sub_choice = input("\nВыберите опцию: ").strip()

        if sub_choice == "1":
            category_analysis.plot_category_revenue(df)
            continue

        elif sub_choice == "2":
            category_analysis.plot_top_subcategories(df, metric='Amount')
            continue

        elif sub_choice == "3":
            category_analysis.plot_top_subcategories(df, metric='Profit')
            continue

        elif sub_choice == "0":
            return

        else:
            print("Неверный выбор. Попробуйте еще раз.")
            input("Нажмите Enter чтобы продолжить...")


def show_geo_menu(df):
    """показывает подменю для географического анализа"""

    while True:
        clear_screen()
        print("\nГЕОГРАФИЧЕСКИЙ АНАЛИЗ")
        print("1. Выручка по штатам (топ-5)")
        print("2. Выручка по городам (топ-5)")
        print("0. Назад в главное меню")

        sub_choice = input("\nВыберите опцию: ").strip()

        if sub_choice == "1":
            geo_analysis.plot_state_revenue(df)
            continue

        elif sub_choice == "2":
            geo_analysis.plot_city_revenue(df)
            continue

        elif sub_choice == "0":
            return

        else:
            print("Неверный выбор. Попробуйте еще раз.")
            input("Нажмите Enter чтобы продолжить...")


def get_user_choice(df):
    """главная функция интерфейса - показывает основное меню"""

    while True:
        clear_screen()
        print("=" * 49)
        print("ГЛАВНОЕ МЕНЮ:")
        print("-" * 40)
        print("1. Анализ выручки по времени")
        print("2. Анализ категорий и подкатегорий")
        print("3. Географический анализ")
        print("4. Анализ клиентов")
        print("5. Анализ платежных методов")  # НОВЫЙ
        print("6. Анализ прибыльности подкатегорий")       # НОВЫЙ
        print("0. Выход из программы")

        choice = input("\nВыберите опцию (цифра): ").strip()

        if choice == "0":
            print("\nСпасибо за использование программы!")
            break  # завершаем программу

        elif choice == "1":
            show_revenue_menu(df)

        elif choice == "2":
            show_category_menu(df)

        elif choice == "3":
            show_geo_menu(df)

        elif choice == "4":
            customer_analysis.plot_top_customers(df)

        elif choice == "5":  # НОВЫЙ МОДУЛЬ PAYMENT_ANALYSIS
            payment_analysis.plot_payment_methods(df)

        elif choice == "6":  # НОВЫЙ МОДУЛЬ PROFIT_TOP
            profit_top.show_profit_menu(df)

        else:
            print("Неверный выбор. Попробуйте еще раз.")
            input("Нажмите Enter чтобы продолжить...")