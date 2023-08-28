#Problema
'''Faça um programa que leia 20 números inteiros, determine e mostre o maior deles.'''

#Declaração de variáveis
numAux = 0

#Processamento de dados
print('---------------------------------')
for (count) in range (20, 0, -1):
    
    #Variáveis de entrada
    num = int(input(f'Digite um número inteiro: '))
    if (num > numAux):
        numAux = num

#Saída do programa
print('---------------------------------')
print(f'O maior número é {numAux}.')
print('---------------------------------')