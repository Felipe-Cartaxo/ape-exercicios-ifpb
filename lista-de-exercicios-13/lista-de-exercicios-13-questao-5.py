'''Problema: Faça um programa que leia uma frase e a exiba com uma letra em cada linha.'''

#Leitura da frase
frase = input('Informe uma frase: ')

#Leitura do tamanho da frase
tam = len(frase)

#Saída do programa
print('Saída do programa: ')
for (x) in range (tam):
    print(f'{frase[x]}')