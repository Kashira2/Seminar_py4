#  Создайте словать заданный по формуле 3*n+1, где n это ключ, а формула значение

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# my_dict = {}         #создать словарь

# number = int(input('Введите целое число: '))

# for n in range(1, number+1):
#     my_dict[n] = 3*n + 1

# print(my_dict)          # тут берем значение, которое нам нужно
# print(my_dict.get(7, 'Такого ключа нет'))   

##########################################################################################

my_string = 'Питон самый лучший язык в мире'

my_list = ['1', '2', '34', '5', '6', '7', '8']
glue = ''

my_string = my_string.replace('и', '$')               # замена всех букв 'и'
print(my_string)

print(''.join(my_list))                    #склейка
print(glue.join(my_list))                  # можно так

# print(my_string.startswith('пит'))                          # проверка на тру и фолсе начало строки

# print(my_string.lower().startswith('пит'))                    # проверка если написал не заглавными

# print(my_string.upper().startswith('ПИТ'))                        # проверка если написал заглавными

# print(my_string.endswith('ире'))                                    # проверка в конце строки

# print(my_string.strip())                       # если много пробелов и прочего в строке, чтобы вывести без них
#  rstrip   # справа 
#  lstrip    # слева

####################################################################################################

# Найдите корни квадратного уравнения Ax² + Bx + C = 0 
# с помощью математических формул нахождения корней квадратного уравнения

# equation = '-3*x**2 + 5*x - 6 = 0'


# equation = equation.replace('**2', '')
# #equation = equation.replace(' = 0', '')
# equation = equation.replace('*x', '')

# equation = equation.split(' ')


# a = int(equation[0])
# if equation[1] == '+':
#     b = int(equation[2])
# else:
#     b = int(equation[2]) * -1

# if equation[3] == '+':
#     c = int(equation[4])
# else:
#     c = int(equation[4]) * -1

# print(a, b, c)

# discriminant = b**2 - 4*a*c

# def function(discriminant):
#     if discriminant < 0:
#         return ('решений нет')
#     elif discriminant == 0:
#         return -(b/(2*a))
#     else:
#         x1 = round((-b + (discriminant)**0.5)/(2*a), 3)
#         x2 = round((-b - (discriminant)**0.5)/(2*a), 3)
#         return print(f'{x1} {x2}')

# z = function(discriminant)
# print(z)

#####################################################################################
#  решение препода
# import math

# equation = '3*x**2 + 5*x - 6 = 0'

# def create_koef(equation: str):
#     new_equation = equation.replace(' ', '').replace('=0', '')\
#         .replace('+', ' ').replace('-', ' -')
#     new_equation = new_equation.split()
#     new_list = []
#     for item in new_equation:
#         if item.startswith('x'):
#             new_list.append(1)
#         elif item.startswith('-x'):
#             new_list.append(-1)
#         else:
#             new_list.append(item.split('*x')[0])
    
#     return new_list


# def solve_equation(koef):
#     a, b, c = int(koef[0]), int(koef[1]), int(koef[2])
#     disc = b**2 - 4 * a * c
#     if disc > 0:
#         x1 = (-b - math.sqrt(disc) / 2 *a)
#         x2 = (-b + math.sqrt(disc) / 2 *a)
#         return round(x1, 2), round(x2, 2)
#     elif disc == 0:
#         x1 = (-b - math.sqrt(disc) / 2 *a)
#         return round(x, 2)
#     else:
#         return None
    
# print(solve_equation(create_koef(equation)))