'''Problema: Faça um programa que leia uma frase e a exiba criptografada. O método de
criptografia será baseado na seguinte regra: trocar alguns caracteres por outros,
conforme a tabela abaixo: 

Exemplo: "BOA NOITE" criptografado fica "BI ANIOTU"'''

#Leitura da frase
frase = input('Informe a frase que deseja criptografar: ').upper()

#Leitura do tamanho da frase
tam = len(frase)

#Geração de uma string vazia
fraseAux = ""

#Leitura dos caracteres de 'frase' e geração da string 'fraseAux'
for (x) in range (tam):
  if (frase[x] == 'A'):
    fraseAux += ' '
  elif (frase[x] == 'E'):
    fraseAux += 'U'
  elif (frase[x] == 'I'):
    fraseAux += 'O'
  elif (frase[x] == 'O'):
    fraseAux += 'I'
  elif (frase[x] == 'U'):
    fraseAux += 'E'
  elif (frase[x] == ' '):
    fraseAux += 'A'
  else:
    fraseAux += frase[x]

print('-'*50)
print(f'Antes da formatação: {frase}')
print(f'Frase após a formatação: {fraseAux}')
  