# 29.	Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел

A = int(input('Введите число А = '))
B = int(input('Введите число В = '))

def Efclid(a, b):
    while a != 0 and b !=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

print((A * B) / Efclid(A, B))