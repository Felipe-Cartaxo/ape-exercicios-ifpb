#Problema
'''Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles
Obs: não use o comando for, use while.'''

#Declaração de variáveis constantes/de controle
numTotal = 0
count = 1

#Variáveis de entrada
print('---------------------------------------')
while (count <= 30):
    print(f'Digite o {count}º número: ', end='')
    num = int(input(''))
    #Processamento de dados
    numTotal = numTotal + num
    count = count + 1

#Saída do programa
print('---------------------------------------')
print(f'A soma dos números digitados é {numTotal}.')
print('---------------------------------------')