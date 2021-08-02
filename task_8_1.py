"""
Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел
"""
from functools import reduce
from random import randint as rnd
from math import factorial as fact


def fact2(f, n):
    """ Функция - двойной факториал числа """
    return reduce(lambda x, y: x*y, filter(lambda x: x % 2 == n % 2, list(range(1, f(n)+1))))


def main_func():
    """ Test function """
    n = rnd(2, 8)   # Случайное число для первого факториала
    print(f'{n}!  = {fact(n)}')     # Вывод !
    print(f'{n}!! = {fact2(fact,n)}')    # Вывод !!


if __name__ == '__main__':
    main_func()