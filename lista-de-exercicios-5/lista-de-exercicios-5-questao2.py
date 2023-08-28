#Variáveis de entrada
print ('------------------------------------------')
char = input('Digite um caractere qualquer: ')

#Processamento de dados
charValue = ord(char)

if (charValue >= 48 and charValue <= 57):
    charType = 'número'
elif (charValue >= 65 and charValue <= 90):
    charType = 'letra maiúscula'
elif (charValue >= 97 and charValue <= 122):
    charType = 'letra minúscula'
else:
    charType = 'caractere especial'
#Saída do programa
print ('------------------------------------------')
print (f'O caractere "{char}" é do tipo {charType}.')
print ('------------------------------------------')