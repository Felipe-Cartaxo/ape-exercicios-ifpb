'''Problema: Faça um programa que leia uma string S e um valor inteiro N, e exiba na tela a string S com as suas vogais repetidas N vezes.
Exemplo:
Entrada: S: Hoje tem aula de Python
N: 3
Saída: Hooojeee teeem aaauuulaaa deee Pythooon'''

#Leitura da frase
frase = input('Informe uma frase qualquer: ')

#Leitura do número de repetições da vogal
n = int(input('Informe a quantidade de repetições: '))

#Leitura do tamanho da string
tam = len(frase)

#Geração de uma string vazia
fraseFinal = ''

#Formatação da frase
for (x) in range (tam):
    if (frase[x] == 'A' or frase[x] == 'E' or frase[x] == 'I' or frase[x] == 'O' or frase[x] == 'U' or frase[x] == 'a' or frase[x] == 'e' or frase[x] == 'i' or frase[x] == 'o' or frase[x] == 'u'):
        fraseFinal += frase[x] * n
    else:
        fraseFinal += frase[x]

#Saída do programa
print('-'*50)
print(f'Frase antes da formatação: {frase}')
print(f'Frase após a formatação: {fraseFinal}')
print('-'*50)