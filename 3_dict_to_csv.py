import csv

# Домашнее задание №2
# Работа csv
# 1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
#    В списке нужно создать не менее 4-х словарей
# 2. Запишите содержимое списка словарей в файл в формате csv


def main():
    # создаем список словарей
    persons = [
        {"name": "John", "age": 25, "job": "developer"},
        {"name": "Jane", "age": 30, "job": "designer"},
        {"name": "Dave", "age": 40, "job": "manager"},
        {"name": "Mike", "age": 35, "job": "programmer"},
    ]

    # определяем имена полей таблицы
    fields = ["name", "age", "job"]

    # записываем словари в файл в формате CSV
    with open("persons.csv", "w", newline="\n") as csv_file:
        writer = csv.DictWriter(csv_file, fields)
        writer.writeheader()  # записываем заголовок таблицы
        for person in persons:
            writer.writerow(person)


if __name__ == "__main__":
    main()
