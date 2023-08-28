#Problema
'''Faça um programa que leia um número N, calcule e mostre os N primeiros termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...). O valor lido para N sempre será maior ou igual a 2.'''

#Declaração de variáveis
numAux = 1
numAnt = 0
numFib = 0
count = 1

#Variáveis de entrada
print('-'*50)
while (True):
    num = int(input('Digite um número inteiro: '))
    if (num >= 2):
        break
    print('Número inválido. Por favor digite um número maior ou igual a 2.')
    print('-'*50)
print('-'*50)

'''
Lógica da sequência de Finonacci:

1º Termo: 1 (numAnt) + 1 (numAux) = 2 (numFib)
2ª Termo: 2 (numAnt) + 1 (numAux) = 3 (numFib)
3ª Termo: 3 (numAnt) + 2 (numAux) = 5 (numFib)
4ª Termo: 5 (numAnt) + 3 (numAux) = 8 (numFib)...
'''
#Processamento de dados
while (count < num):
    if (count == 1):
        print(f'{count}º termo: {numFib}')

    numFib = numAux + numAnt
    numAnt = numFib
    numAux = numFib - numAux
    count += 1

    #Saída do programa
    print(f'{count}º termo: {numFib}')

print ('-'*50)
print('Fim do programa')
print ('-'*50)