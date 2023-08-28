#Problema
'''Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Faça um programa que leia um número e determine se ele é ou não primo.'''

numPrimoCount = 0

#Variáveis de entrada
print('-------------------------------------')
num = int(input('Digite um número inteiro: '))

#Processamento de dados
for (count) in range (1, num + 1, 1):
    if (num % count) == 0:
        numPrimoCount = numPrimoCount + 1

if (numPrimoCount == 2):
    numPrimo = 'é primo'
else:
    numPrimo = 'não é primo'

#Saída do programa
print('-------------------------------------')
print(f'O número {num} {numPrimo}.')
print('-------------------------------------')