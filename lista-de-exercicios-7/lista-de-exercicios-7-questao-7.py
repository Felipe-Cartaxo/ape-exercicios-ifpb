#Problema
'''Faça um programa que leia a idade de várias pessoas visitantes de um show (a leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
• A média de idade do público;
• A porcentagem de pessoas com idade entre 18 e 21 anos;
• Idade do visitante mais jovem.'''

#Declaração de variáveis constantes/de controle
count = 1
idadeTotal = 0
idadeMenor = 999
countJovemAdulto = 0

while (True):
    print('----------------------------------------------------------------')
    
    #Variáveis de entrada
    idadeVisitante = int(input('Digite sua idade: '))

    #Processamento de dados
    if (idadeVisitante >= 18 and idadeVisitante <= 21):
        countJovemAdulto = countJovemAdulto + 1
    
    idadeTotal = idadeTotal + idadeVisitante

    if (idadeVisitante == 0):
        break

    if (idadeVisitante < idadeMenor):
        idadeMenor = idadeVisitante
    
    count = count + 1

idadeMedia = idadeTotal / (count - 1)
percJovemAdulto = (countJovemAdulto / (count - 1)) * 100

#Saída do programa

print('----------------------------------------------------------------')
print(f'MÉDIA DE IDADE DO PÚBLICO: {idadeMedia:0.2f}')
print(f'PORCENTAGEM DE PESSOAS ENTRE 18 E 21 ANOS: {percJovemAdulto:0.2f}%')
print(f'IDADE DO VISITANTE MAIS JOVEM: {idadeMenor}')
print('----------------------------------------------------------------')