'''
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
'''

my_num = int(input("введите число N=  "))
next_num = 0


def rev_my_num(my_num):
    global next_num
    if my_num > 0:
        temp = my_num % 10
        next_num = (next_num * 10) + temp
        rev_my_num(my_num // 10)
    return next_num


print(rev_my_num(my_num))