import math

#Variáveis de entrada
print('---------------------------------------')
a = float(input('Informe o valor de "a": '))
b = float(input('Informe o valor de "b": '))
c = float(input('Informe o valor de "c": '))
print('---------------------------------------')

#Processamento de dados
delta = (b ** 2) - (4 * a * c)

#Saída do programa

if (delta < 0):
    raizes = print('A equação não possui raízes.')
    print('---------------------------------------')
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    print(f'Delta = {delta:.2f}')
    print(f'As raízes são: x1 = {x1:.2f} e x2 = {x2:.2f}')
    print('---------------------------------------')