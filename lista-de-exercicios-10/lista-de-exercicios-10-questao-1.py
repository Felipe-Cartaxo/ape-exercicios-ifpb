#Problema
'''Escreva um programa que leia um vetor contendo N elementos inteiros (N será lido), calcule e exiba:
• A quantidade de elementos pares;
• A quantidade de elementos ímpares;
• A soma de todos os elementos;
• A média dos elementos do vetor.'''

#Leitura do tamanho do vetor
print('-'*50)
n = int(input('Digite o tamanho do vetor: '))
print('-'*50)

#Declaração de variáveis
vetor = [None] * n
countPar = 0
countImpar = 0
numSoma = 0

#Leitura dos elementos do vetor
for (count) in range (n):
    vetor[count] = int(input(f'Número [{count}]: '))
    
    #Contagem dos números pares
    if (vetor[count] % 2 == 0):
        countPar += 1

    #Contagem dos números ímpares
    if (vetor[count] % 2 != 0):
        countImpar += 1

    #Somatório dos elementos do vetor
    numSoma = numSoma + vetor[count]

#Cálculo da média do vetor
numMedia = numSoma/(count + 1)

#Saída do programa
print('-'*50)
print(f'Quantidade de elementos pares:      {countPar}')
print(f'Quantidade de elementos ímpares:    {countImpar}')
print(f'Soma de todos os elementos:         {numSoma}')
print(f'Média dos elementos do vetor:       {numMedia:.1f}')
print('-'*50)
