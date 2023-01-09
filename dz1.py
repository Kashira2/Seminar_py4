import random

num1 = int(input('Введите натуральную степень многочлена: '))

my_list = []

def creat_list(my_list, num1):
    for i in range(1, num1+2):
        kof = int(random.uniform(-100, 100))
        if kof > 1 or kof < 0:
            my_list.append(str(kof))
        elif kof == 1:
            my_list.append('c')
        elif kof == -1:
            my_list.append('-c') 
        else:
            my_list.append('z') 

    my_string = ' '.join(my_list)

    my_string = my_string.split(' ') 

    return my_string
print(creat_list(my_list, num1))

def string_end(num1, my_string):
    new_string = ''
    for i in range(num1+1):
        step = str(num1 - i)
        my_string[i] = my_string[i] + ' '
        if my_string[i] == 'z ':
            new_string = new_string + ''
        elif my_string[i] == 'c ':
            new_string = new_string + my_string[i].replace('c ', 'x**k').replace('k', step) + ' '
        else:
            new_string = new_string + my_string[i].replace(' ', '*x**k').replace('k', step) + ' '
    return new_string

print(string_end(num1, creat_list(my_list, num1)).replace('*x**0', '').replace('x**0', '1')\
    .rstrip().replace(' ', ' + ').replace('**1', '').replace(' + -', ' - ') + ' = 0')

# f = open('file2.txt', 'w')
# f.write(string_end(num1, creat_list(my_list, num1)).replace('*x**0', '').replace('x**0', '1')\
#     .rstrip().replace(' ', ' + ').replace('**1', '').replace(' + -', ' - ') + ' = 0')
# f.close
