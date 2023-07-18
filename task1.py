'''Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.'''

def degree(a,b):
    if b == 0:
        return 1
    return a * degree(a, b-1)

first_number = int(input('Введите число: '))
second_number = int(input('Введите степень: '))
print(degree(first_number,second_number))
    
