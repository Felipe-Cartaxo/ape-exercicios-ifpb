#Problema
'''Escreva um programa que receba um vetor V de N números inteiros (N será lido), determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices.
Obs: suponha a inexistência de valores repetidos.'''

import random

#Leitura do tamanho do vetor
print('-'*50)
n = int(input('Digite o tamanho do vetor A: '))
print('-'*50)

#Inicialização do vetor
vetorA = [None] * n

#Declaração de variáveis
maiorIndice = 0
menorIndice = 0

#Leitura dos elementos do vetor
for (count) in range (n):
    vetorA[count] = random.randint(1, 20)

    #Inicializando as variáveis com o valor e o índice do 1º elemento
    if (count == 0):
        maiorNum = vetorA[count]
        menorNum = vetorA[count]
    else:
        #Testando o valor da vez com o atual maior
        if (vetorA[count] > maiorNum):
            maiorNum = vetorA[count]
            maiorIndice = count

        #Testando o valor da vez com o atual menor
        if (vetorA[count] < menorNum):
            menorNum = vetorA[count]
            menorIndice = count

#Saída do programa
print('Vetor A:', vetorA)
print('-'*50)
print(f'Maior número do vetor: {maiorNum}')
print(f'Índice do maior número do vetor: {maiorIndice}')
print(f'Menor número do vetor: {menorNum}')
print(f'Índice do menor número do vetor: {menorIndice}')
print('-'*50)