# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
class NewEx(Exception):
    pass


while True:
    try:
        n = int(input("Введите число N=  "))
        m = int(input("введите число M=  "))
        if n < 0:
            raise NewEx()
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова.")
    except NewEx:
        print("число N должно быть положительным!")

print(f'число N= {n}, число M= {m}')


def summ_numm(n, m):
    if n == 0:
        return m
    return summ_numm(n - 1, m + 1)


print(f'сумма чисел = {summ_numm(n, m)}')
