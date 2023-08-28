'''Faça um programa que solicite ao usuário uma senha. Caso a senha digitada esteja correta, o programa deverá mostrar senha correta. Caso contrário, o programa deverá mostrar senha incorreta e pedir para o usuário tentar novamente digitar a senha correta. Mas, se o usuário fornecer três senhas incorretas, o programa deverá encerrar a sua execução. (Obs: a senha correta é “abcd”).'''

senhaCorreta = 'abcd'
count = 1
countLimite = 3
senha = 0
msgErro = 'Senha incorreta, tente novamente.'
msgCorreta = 'A senha digitada está correta!'
msgLimite = 'Você atingiu o limite de tentativas, o programa será encerrado.'

print('-'*50)
while (True):
    print(f'{count}º tentativa: ')
    senha = input('Digite a senha: ')
    print('-'*50)

    if (senha == senhaCorreta):
        print(msgCorreta)
        break
    if (count >= countLimite):
        print(msgLimite)
        break

    print(msgErro)

    count += 1

print('-'*50)