'''Problema: Faça um programa que leia uma frase e a exiba toda em letras maiúsculas.'''

#Leitura da frase
frase = input('Informe uma frase: ')

#Leitura do tamanho da frase
tam = len(frase)

#Geração de uma string vazia
fraseFinal = ""

#Alteração da frase para letras maiúsculas
for (x) in range (tam):
    #Ou seja, se a letra for minúscula
    if (ord(frase[x]) >= 97 and ord(frase[x]) <= 122):
        fraseFinal += chr(ord(frase[x]) - 32)
    #Casos onde há espaços na string
    elif (ord(frase[x]) == 32):
        fraseFinal += ' '
    #Demais casos, ou seja, caracteres que já estão maiúsculos ou outros tipos de caracteres que não são numéricos
    else:
        fraseFinal += frase[x]

#Saída do programa
print('-'*50)
print(f'Frase antes da formatação: {frase}')
print(f'Frase após a formatação: {fraseFinal}')