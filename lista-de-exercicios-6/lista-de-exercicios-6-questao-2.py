#Problema
'''Faça um programa que leia um número N, inteiro, e some todos os números de 1 até N, mostrando o resultado.'''

#Declaração de variáveis
soma = 0

#Variáveis de entrada
print('------------------------------')
num = int(input('Digite um número inteiro: '))
print('------------------------------')

#Processamento de dados e saída do programa
for (count) in range (1, num + 1, 1):
    print(f'{count} + {soma}', end='')
    soma = soma + count
    print(f' = {soma}')
print('------------------------------')