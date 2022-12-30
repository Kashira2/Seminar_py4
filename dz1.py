import random

num1 = int(input('Введите натуральную степень многочлена: '))

my_list = []

for i in range(1, num1+1):
    kof = int(random.uniform(0, 4))
    if kof > 1:
        my_list.append(str(kof))
    elif kof == 1:
        my_list.append('c') 
    else:
        my_list.append('z')   
print(' '.join(my_list))

my_string = ' '.join(my_list)

my_string = my_string.split(' ') 

print(my_string)

new_string = ''
for i in range(num1):
    step = str(num1 - i)
    my_string[i] = my_string[i] + ' '
    if my_string[i] == 'z ':
        new_string = new_string + ''
    elif my_string[i] == 'c ':
        new_string = new_string + my_string[i].replace('c', 'x**k').replace('k', step) + ' '
    else:
        new_string = new_string + my_string[i].replace(' ', '*x**k').replace('k', step) + ' '

print(new_string.replace(' ', ' '))
