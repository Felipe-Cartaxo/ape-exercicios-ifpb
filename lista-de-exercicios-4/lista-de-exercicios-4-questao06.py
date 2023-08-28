#Variáveis de entrada
print('---------------------------------')
nome = input('Informe seu nome: ')
conceito = input('Informe seu conceito: ').upper()

#Saída do programa
if (conceito == 'A'):
    recomendacao = 'Fortemente recomendado'
elif (conceito == 'B' or conceito == 'C'):
    recomendacao = 'Recomendado'
else:
    recomendacao = 'Não recomendado'

#Saída do programa
print('---------------------------------')
print(f'Nome do estudante: {nome}')
print(f'Conceito {conceito}: {recomendacao}.')
print('---------------------------------')