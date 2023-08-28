'''Problema: Faça um programa que leia uma frase e a exiba com a inicial de cada palavra em maiúsculo.'''

#Leitura da frase
frase =  input('Informe uma frase: ')

#Geração de uma string vazia
fraseFinal = ""

#Leitura do tamanho da frase
tam = len(frase)

#Alteração para letras maiúsculas de cada palavra
for (x) in range (tam):
    #Ou seja, se a letra for minúscula
    if (ord(frase[x]) >= 97 and ord(frase[x]) <= 122):
        if (x == 0 or frase[x - 1] == ' '):
            fraseFinal += chr(ord(frase[x]) - 32)
        else:
            fraseFinal += frase[x]
    else:
        fraseFinal += frase[x]

#Saída do programa
print('-'*50)
print(f'Frase antes da formatação: {frase}')
print(f'Frase após a formatação: {fraseFinal}')
print('-'*50)