#  Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('file.txt', 'r', encoding='UTF-8')  as data:      
    polynomial1 = data.read()

with open('file2.txt', 'r', encoding='UTF-8')  as data:      
    polynomial2 = data.read()

print(f'Первый многочлен {polynomial1}')
print(f'Второй многочлен {polynomial2}')

polynomial1 = polynomial1.replace('+', '').replace('- ', ' -').replace('=', '').split(' ')
polynomial2 = polynomial2.replace('+', '').replace('- ', ' -').replace('=', '').split(' ')

pol1 = []
pol2 = []
for i in range(len(polynomial1)):
    if polynomial1[i] != '' and polynomial1[i] != '0':  
        pol1.append(polynomial1[i])
    if polynomial2[i] != '' and polynomial2[i] != '0': 
        pol2.append(polynomial2[i])

# print(pol1)
# print(pol2)

sum1 = []

for i in range(len(pol1)):
    if pol1[i].endswith('**'+str(len(pol1)-i-1)) == True:
        for j in range(len(pol2)):
            if pol2[j].endswith('**'+str(len(pol1)-i-1)) == True:
                temp ='**'+ str(len(pol1)-i-1)
                sum = int(pol1[i].replace('*x**'+str(len(pol1)-i-1), '')) + int(pol2[j].replace('*x**'+str(len(pol1)-i-1), ''))
                sum1.append(str(sum)+'*x**'+str(len(pol1)-i-1))
    elif pol1[i].endswith('*x') == True:
        for j in range(len(pol2)):
            if pol2[j].endswith('*x') == True:
                sum = int(pol1[i].replace('*x', '')) + int(pol2[j].replace('*x', ''))
                sum1.append(str(sum)+'*x')
    else:
        for j in range(len(pol2)):
            if '*' in pol2[j]:
                k=2
            else:
                sum = int(pol1[i]) + int(pol2[j])
                sum1.append(str(sum))

final = ' + '.join(sum1)

final = final.replace('+ -', '-').replace('0*x', 'x').replace(' + 0', '').replace(' - 0', '')
print(f'Сумма многочленов {final}')