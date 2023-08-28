#Problema
'''Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a intercalação dos elementos de A e B.
Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]'''

#Leitura do tamanho do vetor
print('-'*50)
vetorTam = int(input('Digite o tamanho do vetor: '))
print('-'*50)

#Inicialização dos vetores
vetorA = [None] * vetorTam
vetorB = [None] * vetorTam

#Como o vetorResult é a resultante do vetorA + vetorB, logo preciserá ter o dobro do tamanho
vetorResult = [None] * (vetorTam * 2)

#Leitura dos elementos do vetorA
for (count) in range (vetorTam):
    vetorA[count] = int(input(f'vetorA[{count}] = '))

#Leitura dos elementos do vetorB
for (count) in range (vetorTam):
    vetorB[count] = int(input(f'vetorB[{count}] = '))

#Geração do vetorResult
for (count) in range (vetorTam):
    #Em resumo, vetorResult receberá os elementos do vetorA nos índices pares
    vetorResult[count * 2] = vetorA[count]
    #E receberá os elementos do vetorB nos índices ímpares
    vetorResult[count * 2 + 1] = vetorB[count]

#Saída do programa
print('-'*50)
print('Vetor A = ', vetorA)
print('Vetor B = ', vetorB)
print('Vetor C = ', vetorResult)
print('-'*50)