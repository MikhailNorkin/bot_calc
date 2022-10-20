import sys
import operations as op
from colorama import init, Fore, Back
init()


def check_number_type(input_string: str) -> int:
    '''
    Функция проверяет корректность ввода типа числа.
    '''
    flag = False
    print(Fore.BLUE + Back.WHITE)
    number_type = input(input_string)
    while flag == False:
        try:
            int(number_type)
            number_type = int(number_type)
            if number_type == 1 or number_type == 2:
                flag = True
                return number_type
            else:
                print(Fore.GREEN + Back.RED + '\nНеверный ввод данных!!!')
                print(Fore.BLUE + Back.WHITE)
                number_type = input(input_string)
        except ValueError:
            print(Fore.GREEN + Back.RED + '\nНеверный ввод данных!!!')
            print(Fore.BLUE + Back.WHITE)
            number_type = input(input_string)


def check_ratio_number(input_string: str) -> float:
    '''
    Функция проверки на рациональное число.
    '''
    flag = False
    print(Fore.BLUE + Back.WHITE)
    num = input(input_string)
    while flag == False:
        try:
            float(num)
            print(Fore.BLUE + Back.WHITE)
            num = float(num)
            flag = True
            return num
        except ValueError:
            print(Fore.GREEN + Back.RED + '\nНекорректный ввод!!! \nВ случае дробного числа целая часть отделяется от дробной точкой, никак иначе.\nТакже допустимо вводить только числа (знаки после цифр и буквы недопустимы)')
            num = input(input_string)
            continue


def check_complex_number(input_string: str) -> complex:
    '''
    Функция проверки на комплексное число.
    '''
    flag = False
    print(Fore.BLUE + Back.WHITE)
    num = input(input_string)
    while flag == False:
        try:
            len(list(num.split(','))) == 2
            num1, num2 = map(float, list(num.split(',')))
            while num1 == 0 and num2 == 0:
                print(Fore.GREEN + Back.RED +
                      '\nБессмысленно вводить комплексное число 0 + 0j. Повторите ввод числа!')
                print(Fore.BLUE + Back.WHITE)
                num = input(input_string)
                num1, num2 = map(float, list(num.split(',')))
            num = complex(num1, num2)
            flag = True
            return num
        except ValueError:
            print(Fore.GREEN + Back.RED +
                  '\nНекорректный ввод!!! \nДолжны быть указаны 2 числа через запятую!')
            print(Fore.BLUE + Back.WHITE)
            num = input(input_string)


def check_number_operation(input_string):
    '''
    Функция проверки на целое число от 1 до 5.
    '''
    while type:
        print(Fore.BLUE + Back.WHITE)
        number_oper = input(input_string)
        try:
            number_oper = int(number_oper)
            if 0 < number_oper < 6:
                return number_oper
            else:
                print(Fore.GREEN + Back.RED +
                      '\nНеверный ввод данных! Должно быть целое число от 1 до 5 включительно!')
                print(Fore.BLUE + Back.WHITE)
                number_oper = input(input_string)
                continue
        except ValueError:
            print(Fore.GREEN + Back.RED +
                  '\nНеверный ввод данных! Должно быть целое число от 1 до 5 включительно!')


def check_exceptions_div(a, b):
    '''
    Функция отлавливает исключения при делении.
    '''
    try:
        op.div_numbers(a, b)
    except ZeroDivisionError:
        print(Fore.GREEN + Back.RED +
              'Вы ввели комбинацию, при которой происходит деление на ноль. Программа завершается!')
        sys.exit()


def check_exceptions_exp(a, b):
    '''
    Функция отлавливает исключения при возведении в степень.
    '''
    try:
        op.exp_numbers(a, b)
    except ZeroDivisionError:
        if a == 0 and isinstance(b, complex):
            print(Fore.GREEN + Back.RED +
                  'Вы ввели комбинацию, при которой происходит возведение ноля в степень - комплексное число, что вызывает ошибку. Программа завершается!')
            sys.exit()
        if a == 0 and (isinstance(b, int) or isinstance(b, float)) and b < 0:
            print(Fore.GREEN + Back.RED +
                  'Вы ввели комбинацию, при которой происходит возведение ноля в отрицательную рациональную степень, что вызывает ошибку. Программа завершается!')
            sys.exit()
