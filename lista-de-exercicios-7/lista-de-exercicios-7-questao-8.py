#Problema
'''Faça um programa que leia o código e a quantidade de cada item comprado por um cliente (a leitura do código “X” indica o fim dos dados de entrada). Ao final, calcule e exiba o total a pagar.
Veja o exemplo abaixo, considerando que o cliente pediu 3 Hamburger e 2 Cheese Bacon:
Entrada:
Código: H
Quantidade: 3
Código: B
Quantidade: 2
Código: X
Saída:
Total a pagar: R$ 29.00'''

#Declaração de variáveis constantes/de controle

cheeseFrangoPreco = 4
hambPreco = 5
cheeseBurgPreco = 6
cheeseBaconPreco = 7
totalLanches = 0

while (True):
    print('----------------------------------------------------------')
    print('Cheese Frango    (Código "F") = R$ 4,00')
    print('Hamburguer       (Código "H") = R$ 5,00')
    print('Cheese Burger    (Código "C") = R$ 6,00')
    print('Cheese Bacon     (Código "B") = R$ 7,00')
    print('----------------------------------------------------------')

    #Variáveis de entrada
    digLanche = input('Código: ').upper()

    if (digLanche == 'X'):
        break

    quantLanche = float(input('Quantidade: '))

    #Processamento de dados
    if (digLanche == 'F'):
        cheeseFrangoTotal = quantLanche * cheeseFrangoPreco
        totalLanches = totalLanches + cheeseFrangoTotal
    if (digLanche == 'H'):
        hambTotal = quantLanche * hambPreco
        totalLanches = totalLanches + hambTotal
    if (digLanche == 'C'):
        cheeseBurgTotal = quantLanche * cheeseBurgPreco
        totalLanches = totalLanches + cheeseBurgTotal
    if (digLanche == 'B'):
        cheeseBaconTotal = quantLanche * cheeseBaconPreco
        totalLanches = totalLanches + cheeseBaconTotal

#Saída do programa
print(f'Total a pagar: R$ {totalLanches:0.2f}')
print('----------------------------------------------------------')