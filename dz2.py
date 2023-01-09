with open('file.txt', 'r', encoding='UTF-8')  as data:      
    polynomial1 = data.read()

with open('file2.txt', 'r', encoding='UTF-8')  as data:      
    polynomial2 = data.read()

print(polynomial1)
print(polynomial2)

polynomial1 = polynomial1.replace('+', '').replace('- ', ' -').replace('=', '').split(' ')
polynomial2 = polynomial2.replace('+', '').replace('- ', ' -').replace('=', '').split(' ')

pol1 = []
pol2 = []
for i in range(len(polynomial1)):
    if polynomial1[i] != '' and polynomial1[i] != '0':  
        pol1.append(polynomial1[i])
    if polynomial2[i] != '' and polynomial2[i] != '0': 
        pol2.append(polynomial2[i])

print(pol2)
print(pol1)