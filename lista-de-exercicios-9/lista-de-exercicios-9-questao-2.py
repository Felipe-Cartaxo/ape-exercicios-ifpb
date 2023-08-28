#Problema
'''Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.'''

#Tamanho do vetor
vetorTotal = 5

#Inicialização do vetor A e da variável que contabilizará as ocorrências
vetorA = [None] * vetorTotal
vetorIgual = 0

#Leitura do vetor A
print('-'*50)
for (count) in range (vetorTotal):
    vetorA[count] = int(input('Digite os elementos do vetor: '))

#Leitura do valor K
print('-'*50)
k = int(input('Digite o valor de "K": '))

#Contagem das ocorrências
for (count) in range (vetorTotal):
    if (vetorA[count] == k):
        vetorIgual += 1

#Saída do programa
print('-'*50)
print(f'Quantidade de ocorrências: {vetorIgual}')
print('-'*50)