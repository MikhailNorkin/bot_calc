# Рациональные числа — это целые и дробные числа (обыкновенные дроби,
# конечные десятичные дроби и бесконечные периодические дроби).
# Рациональное число — это число, которое можно представить
# в виде положительной или отрицательной обыкновенной дроби
# или числа ноль.
# Если число можно получить делением двух целых чисел,
# то это число рациональное.
# Любое комплексное число z задается его действительной частью a,
# мнимой частью b и в нем всегда присутствует символ j,
# обозначающий мнимую единицу. z = a + bj

from typing import Union


def sum_numbers(x: Union[int, float, complex], y: Union[int, float, complex]) -> Union[int, float]:
    '''
    Функция вычисляет сумму двух чисел.
    '''
    return x + y


def diff_numbers(x: Union[int, float, complex], y: Union[int, float, complex]) -> Union[int, float, complex]:
    '''
    Функция вычисляет разность между первым и вторым числом.
    '''
    return x - y


def mult_numbers(x: Union[int, float, complex], y: Union[int, float, complex]) -> Union[int, float, complex]:
    '''
    Функция вычисляет произведение двух чисел.
    '''
    return x * y


def div_numbers(x: Union[int, float, complex], y: Union[int, float, complex]) -> Union[int, float, complex]:
    '''
    Функция вычисляет частное от деления первого числа на второе.
    '''
    return x / y


def exp_numbers(x: Union[int, float, complex], y: Union[int, float, complex]) -> Union[int, float, complex]:
    '''
    Возведение первого числа в степень второго числа.
    '''
    return x ** y
