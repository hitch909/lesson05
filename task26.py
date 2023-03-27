# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

import random

a = random.randint(1, 9)
print(f'число a= {a}')
b = random.randint(1, 9)
print(f"степень числа{a}= {b}")


def degree(a, b):
    if b == 0:
        return 1

    return a * degree(a, b - 1)


print(f"{a} в степени {b} это {degree(a, b)}")
