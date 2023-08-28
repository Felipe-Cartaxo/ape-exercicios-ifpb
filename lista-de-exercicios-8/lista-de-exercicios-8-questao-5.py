'''Faça um programa que, leia a temperatura dos 30 dias do mês de abril diga qual o dia mais quente e o dia mais frio do mês (obs: suponha que não haja empates).'''

qtdDias = 3
count = 1
maiorTemp = -300
menorTemp = 300

print('-'*50)

while (count <= qtdDias):
    print(f'{count}º dia: ')
    tempDia = int(input('Informe a temperatura: '))
    print('-'*50)

    if (tempDia > maiorTemp):
        maiorTemp = tempDia
        diaMaiorTemp = count
    
    if (tempDia < menorTemp):
        menorTemp = tempDia
        diaMenorTemp = count

    count += 1

print(f'Maior temperatura: Dia {diaMaiorTemp}, com {maiorTemp} graus.')
print(f'Menor temperatura: Dia {diaMenorTemp}, com {menorTemp} graus.')
print('-'*50)