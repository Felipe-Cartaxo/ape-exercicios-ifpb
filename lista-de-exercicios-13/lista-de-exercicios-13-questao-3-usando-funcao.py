'''Problema: Faça um programa que leia uma frase e a exiba toda em letras maiúsculas.'''

#Leitura da frase
frase = input('Informe uma frase: ')

#Altereção das letras da string para maiúsculas
fraseFinal = frase.upper()

#Saída do programa
print('-'*50)
print(f'Frase antes da formatação: {frase}')
print(f'Frase após a formatação: {fraseFinal}')