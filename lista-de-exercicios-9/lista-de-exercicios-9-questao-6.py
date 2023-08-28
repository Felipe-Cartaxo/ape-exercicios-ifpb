#Problema
'''Escreva um programa que leia um vetor de N números inteiros (N será lido), inverta a ordem dos elementos do vetor e exiba o vetor invertido.
Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em ordem inversa!'''

import random
#Leitura do tamanho do vetor
print('-'*50)
numTamanho = int(input('Digite o tamanho do vetor: '))
print('-'*50)

#Inicialização do vetor
vetorA = [None] * numTamanho

#Leitura dos elementos do vetor
for (count) in range (numTamanho):
    vetorA[count] = random.randint(1, 20)

#Exibição do vetor antes da inversão
print(f'Antes da inversão: {vetorA}')

#Inversão da ordem dos elementos do vetor
count2 = numTamanho - 1

for (count) in range (numTamanho//2):
    numAux = vetorA[count]
    vetorA[count] = vetorA[count2]
    vetorA[count2] = numAux
    count2 = count2 - 1

#Saída do programa
print('-'*50)
print('Depois da inversão: ', vetorA)
print('-'*50)