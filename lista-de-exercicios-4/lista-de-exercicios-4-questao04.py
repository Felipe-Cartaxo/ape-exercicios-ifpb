#Variáveis de entrada
nome = input('Informe seu nome: ')
sexo = input('Informe seu gênero (M ou F): ').upper()

#Saída do programa
if (sexo == 'M'):
    pronome = 'Sr'
else:
    pronome = 'Sra'

#Saída do programa
print(f'Olá, {pronome}. {nome}!')