#Variáveis de entrada
print('-----------------------------------------')
yearDig = int(input('Digite um ano: '))

#Processamento de dados
if ((yearDig % 4 == 0 and yearDig % 100 != 0) or yearDig % 400 == 0):
    yearType = 'é bissexto'
else:
    yearType = 'não é bissexto'

#Saída do programa
print('-----------------------------------------')
print(f'O ano {yearDig} {yearType}.')
print('-----------------------------------------')