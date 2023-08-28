'''Problema: Faça um programa que leia uma frase e determine a quantidade de brancos contidos na mesma.'''

#Leitura da frase
frase = input('Informe uma frase: ')

#Leitura do tamanho da frase
tam = len(frase)

#Inicialização da variável 'count'
count = 0

#Contagem dos espaços na frase
for (x) in range (tam):
    if (frase[x] == ' '):
        count += 1

#Saída do programa
print('-'*50)
print(f'Há {count} espaços em branco na frase digitada')
print('-'*50)