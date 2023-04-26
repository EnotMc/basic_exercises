import urllib.request

# Домашнее задание №2
# Работа с файлами
# 1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
# 2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
# 3. Подсчитайте количество слов в тексте
# 4. Замените точки в тексте на восклицательные знаки
# 5. Сохраните результат в файл referat2.txt


def main():
# скачиваем файл по ссылке и сохраняем его под локальным именем "referat.txt"
    url = "https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=1"
    urllib.request.urlretrieve(url, "referat.txt")


# читаем содержимое файла в переменную
with open("referat.txt", "r", encoding="utf-8") as file:
    content = file.read()

# подсчитываем количество символов и слов
chars = len(content)
words = len(content.split())

# заменяем точки на восклицательные знаки
new_content = content.replace(".", "!")

# сохраняем новый текст в файл referat2.txt
with open("referat2.txt", "w", encoding="utf-8") as file:
    file.write(new_content)

print(f"Количество символов: {chars}")
print(f"Количество слов: {words}")

if __name__ == "main":
    main()
