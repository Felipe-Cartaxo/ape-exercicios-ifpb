#Problema
'''Escreva um programa que leia um vetor A de N números inteiros (N será lido) e um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os respectivos elementos de a multiplicados por K.
Ex: A = [1,2,3], K = 5, B = [5,10,15].'''

print('-'*50)
#Leitura do tamanho do vetor
n = int(input('Digite o tamanho do vetor A: '))
print('-'*50)

#Inicialização dos vetores A e B
vetorA = [None] * n
vetorB = [None] * n

#Leitura do vetor A
for (count) in range (0, n, 1):
    vetorA[count] = int(input('Digite os elementos do vetor A: '))

print('-'*50)
#Leitura da constante K
k = int(input('Digite o valor da constante "K": '))

#Geração do vetor B
for (count) in range (0, n, 1):
    vetorB[count] = vetorA[count] * k

#Saída do programa
print('-'*50)
print('Vetor A = ', vetorA)
print('Constante K = ', k)
print('Vetor B = ', vetorB)
print('-'*50)