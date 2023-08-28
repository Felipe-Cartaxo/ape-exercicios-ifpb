#Problema
'''Escreva um programa para ler 6 números. Após a leitura dos números, verifique, para cada um deles, se é distinto, ou seja, não possui repetição.'''

import random

#Declaração de variáveis
n = 6
repeticao = False

#Inicialização do vetor
vetor = [None] * n

#Leitura dos elementos do vetor
print('-'*50)
for (count) in range (n):
    vetor[count] = int(input(f'Número [{count}]: '))

print('-'*50)

#Verificação da repetição dos elementos do vetor
for (count) in range (n):
    for (countAux) in range (1, n):
        if (count == countAux):
            break

        #Saída do programa
        if (vetor[count] == vetor[countAux]):
            repeticao = True
            print(f'Houve repetição nos índices [{count}] e [{countAux}]')
            
if (repeticao == False):
    print('Não houve repetição')
        
print('-'*50)