'''Problema: Faça um programa que leia uma frase e a exiba invertida.'''

#Leitura da frase
frase = input('Informe uma frase: ')

#Leitura do tamanho da frase
tam = len(frase)

#Inversão da frase
print('-'*50)
print('Frase invertida: ', end='')
for (x) in range (tam - 1, -1, -1):
    #Saída do programa
    print(f'{frase[x]}', end='')
print()
print('-'*50)