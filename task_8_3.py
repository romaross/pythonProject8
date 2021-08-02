"""
Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)
"""


def main_func():
    """ Test function """
    str1 = input('Enter three words (separated by space):').strip().lower()  # Ввод строки с пробелами нижн. регистр
    x = filter(lambda a: a == a[::-1], [word_i for word_i in str1.split(' ')])  # Определение палиндромов
    print(list(x), ' is palindromes')   # Вывод


if __name__ == '__main__':
    main_func()