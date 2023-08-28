'''Problema: Faça um programa que leia uma frase e a exiba sem os espaços em branco.'''

#Leitura da frase
frase =  input('Informe uma frase: ')

#Varredura das ocorrências de espaços em branco de 'frase'
fraseFinal = frase.replace(' ', '')

#Saída do programa
print('-'*50)
print(f'Frase antes da formatação: {frase}')
print(f'Frase após a formatação: {fraseFinal}')