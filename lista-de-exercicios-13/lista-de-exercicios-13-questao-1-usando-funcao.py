'''Problema: Faça um programa que leia uma frase e determine a quantidade de brancos contidos na mesma.'''

print('-'*50)
#Leitura da frase
frase = input('Digite uma frase: ')

#Contagem de espaços na frase
count = frase.count(' ')

#Saída do programa
print('-'*50)
print(f'Há {count} espaços em branco na frase digitada')
print('-'*50)