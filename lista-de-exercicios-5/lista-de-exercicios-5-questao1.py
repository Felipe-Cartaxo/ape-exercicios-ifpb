#Variáveis de entrada
print('--------------------------------------------------')
numDia = input('Informe um dia da semana (de "1" a "7"): ')

#Processamento de dados
if (numDia == '1' or numDia == '7'):
    if (numDia == '7'):
        diaSemana = 'Sábado'
    else:
        diaSemana = 'Domingo'
    diaUtil = 'final de semana!'
else:
    if (numDia == '2'):
        diaSemana = 'Segunda'
    elif (numDia == '3'):
        diaSemana = 'Terça'
    elif (numDia == '4'):
        diaSemana = 'Quarta'
    elif (numDia == '5'):
        diaSemana = 'Quinta'
    else:
        diaSemana = 'Sexta'
    diaUtil = 'dia útil.'

#Saída do programa
print('--------------------------------------------------')
print(f'{diaSemana}, {diaUtil}')
print('--------------------------------------------------')