# Задание 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


while True:
    try:
        n = int(input("Введите количество элементов N=  "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова.")


def foo(n):
    if n == 1:
        return 1
    sum_el = 1 / ((-2) ** (n - 1))
    print(sum_el)
    return sum_el + foo(n - 1)


foo(n)
print(1)
