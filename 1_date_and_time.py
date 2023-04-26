from datetime import datetime, timedelta

# Домашнее задание №2
# Дата и время
# 1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
# 2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime


def print_days():
    # сегодняшняя дата это текущая дата
    today = datetime.now().date()
    # вчера это сегодняшняя дата минус один день
    yesterday = today - timedelta(days=1)
    # 30 дней назад это текущая дата минус 30 дней
    thirty_days_ago = today - timedelta(days=30)

    print(f"Сегодня: {today}")
    print(f"Вчера: {yesterday}")
    print(f"30 дней назад: {thirty_days_ago}")


def str_2_datetime(date_string):

    fmt_str = '%d/%m/%y %H:%M:%S.%f'
    dt = datetime.strptime(date_string, fmt_str)
    return dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
