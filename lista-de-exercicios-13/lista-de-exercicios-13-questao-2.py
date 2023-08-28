'''Problema: Faça um programa que leia uma frase e a exiba sem os espaços em branco.'''

#Leitura da frase
frase = input('Informe uma frase: ')

#Leitura do tamanho da frase
tam = len(frase)

#Geração de uma string vazia
fraseFinal = ""

#Verificação e substituição das ocorrências
for (x) in range (tam):
    if (frase[x] == ' '):
        fraseFinal+= ''
    else:
        fraseFinal += frase[x]

#Saída do programa
print('-'*50)
print(f'Frase antes da formatação: {frase}')
print(f'Frase após a formatação: {fraseFinal}')