#Problema
'''Faça um programa que calcule e mostre os números múltiplos de 5 do intervalo 50 a 300, juntamente com suas raízes e seus cubos.'''

import math

#Declaração de variáveis constantes/de controle
divisor = 5
numInicio = 50
numFinal = 300

coluna1 = 5
coluna2 = 10
coluna3 = 10

print(f'{"x":>{coluna1}} {"Raiz (x)":>{coluna2}} {"Cubo (x)":<{coluna3}}')

#Processamento de dados
for (count) in range (numInicio, numFinal + 1, 1):
    if (count % divisor == 0):
        numRaiz = math.sqrt(count)
        numCubo = count ** 3

        #Saída do programa
        print(f'{count:{coluna1}} {numRaiz:{coluna2:}.4f} {numCubo:{coluna3}}')