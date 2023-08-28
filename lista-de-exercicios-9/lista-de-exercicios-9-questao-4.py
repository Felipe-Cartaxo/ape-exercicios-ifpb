#Problema
'''Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.'''

#Declaração de variáveis
num = 10
vetorA = [None] * num

#Leitura dos números do vetor
print('-'*50)
for (count) in range (num):
    vetorA[count] = int(input(f'Número [{count}]: '))

#Exibição dos números que estão nos índices pares:
print('-'*50)
print('Números que estão nos índices pares: ')
print('-'*50)
for (count) in range (num):
    if (count % 2 == 0):
        print(vetorA[count])

#Exibição dos números que estão nos índices ímpares:
print('-'*50)
print('Números que estão nos índices ímpares: ')
print('-'*50)
for (count) in range (num):
    if (count % 2 == 1):
        print(vetorA[count])
print('-'*50)