'''Problema: Faça um programa que leia o email de uma pessoa e mostre, separadamente,
qual o login e qual o domínio.
Por exemplo, suponha que o email seja "fulano@provedor.com.br", então o login
será "fulano" e o domínio será "provedor.com.br".'''

#Leitura do email
email = input('Informe seu email: ')

#Fatiamento da string 'email'
emailSplit = email.split('@')

#Geração da variável contendo o login
login = emailSplit[0]

#Geração da variável contendo o domínio
domain = emailSplit[1]

#Saída do programa
print('-'*50)
print(f'Nome do usuário: {login}')
print(f'Domínio do email: {domain}')