#Problema
'''Faça um programa que leia vários números, determine e mostre o maior e o menor deles.
Obs: a leitura do número 0 (zero) encerra o programa.'''

#Declaração de variáveis constantes/de controle
numMaior = 0

#Processamento de dados
print('----------------------------------------------------------')
while (True):
    #Variáveis de entrada
    num = int(input('Digite um número: '))
    if (num == 0):
        break
    if (num > numMaior):
        numMaior = num

#Saída do programa
print('----------------------------------------------------------')
print(f'Dentre os números digitados, o maior número é {numMaior}.')
print('----------------------------------------------------------')