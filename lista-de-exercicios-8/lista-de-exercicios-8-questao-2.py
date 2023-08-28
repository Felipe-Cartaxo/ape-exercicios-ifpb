#Problema
'''Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Faça um programa que mostre todos os números primos de 1 a N (obs: N será lido).'''

#Variáveis de entrada
while (True):
    num = int(input('Digite um número inteiro: '))
    if (num > 0):
        break
    print('Número inválido. Favor inserir um número maior do que zero.')
    print('-'*50)

#Processamento de dados  
for count in range(1, num + 1, 1):
    primo = True
    for countAux in range(2, count, 1):
        if count % countAux == 0:
            primo = False
            break

    #Saída do programa
    if primo:
        print(f'{count}', end=' ')