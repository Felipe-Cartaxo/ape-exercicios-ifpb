#Problema
'''Escreva um programa que leia um vetor V contendo N elementos inteiros (N será lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver, informe em que posição (índice).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K aparece.'''

#Leitura do tamanho do vetor
print('-'*50)
n = int(input('Digite o tamanho do vetor A: '))

#Inicialização do vetor A
vetorA = [None] * n

#Leitura do vetor A
print('-'*50)
for (count) in range (n):
    vetorA[count] = int(input('Digite os elementos do vetor A: '))

#Leitura do vetor K
print('-'*50)
k = int(input('Digite o valor de "K": '))

#Verificação se K está no vetor A
existe = False
for (testK) in (vetorA):
    if (testK == k):
        existe = True
        break

#Saída do programa
if (existe):
    print('-'*50)
    print(f'O valor {k} está nas seguintes posições: ')
    print('-'*50)
    for (count) in range (n):
        if (vetorA[count] == k):
            print(count)
else:
    print(f'O valor {k} não está no vetor')
print('-'*50)