# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowels_count = sum([1 for letter in word.lower() if letter in vowels])
print(vowels_count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(len(words))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
avg_word_length = sum([len(word) for word in words]) / len(words)
print(avg_word_length)
