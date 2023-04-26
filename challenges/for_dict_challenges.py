from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

# Вариант 1
name_count = {}

for student in students:
    name = student['first_name']
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

for name, count in name_count.items():
    print(f"{name}: {count}")

# Вариант 2
names = []

for student in students:
    names.append(student['first_name'])
print(names)

for key, name in Counter(names).items():
    print(f'{key}: {name}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

# Вариант 1
name_count = {}

for student in students:
    name = student['first_name']
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

most_common_name = max(name_count, key=name_count.get)
print(f"Самое частое имя среди учеников: {most_common_name}")

# Вариант 2
name_list = []

for student in students:
    name_list.append(student['first_name'])

name_count = {}

for name in name_list:
    name_count.update({name: name_list.count(name)})

for key, names in name_count.items():
    if names == max(name_count.values()):

        print(f'Самое частое имя среди учеников: {key}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

school_class = 1
for student in school_students:
    names = [name_student['first_name'] for name_student in student]
    c = Counter(names)
    print(f'Самое частои имя в классе {school_class}: {c.most_common()[0][0]}')
    school_class += 1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for school_class in school:
    class_name = school_class['class']
    students = school_class['students']
    boys_count = 0
    girls_count = 0
    for student in students:
        name = student['first_name']
        if is_male[name]:
            boys_count += 1
        else:
            girls_count += 1
    print(f"Класс {class_name}: девочки {girls_count}, мальчики {boys_count}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

male_counts = {}
female_counts = {}

for cls in school:
    class_name = cls['class']
    male_counts[class_name] = 0
    female_counts[class_name] = 0

for student in cls['students']:
    name = student['first_name']
    if is_male[name]:
        male_counts[class_name] += 1
    else:
        female_counts[class_name] += 1

max_male_class = max(male_counts, key=male_counts.get)
max_female_class = max(female_counts, key=female_counts.get)

print(f'Больше всего мальчиков в классе {max_male_class}')
print(f'Больше всего девочек в классе {max_female_class}')
