#Problema: criar um script que valide o usuário "admin" e a senha "123"
#O script deve rodar infinitas vezes até o usuário acertar login e senha

login = input("Por favor, digite o login: ")
senha = float(input("Por favor, digite a senha: "))

validacao_login = False
tentativas = 0

while (validacao_login is False):
    tentativas = tentativas + 1
    if (login.upper() == 'ADMIN' and senha == 123):
        print("Você está logado no sistema")
        validacao_login = True
    else:
        print("Tente novamente")
        login = input("Por favor, digite o login: ")
        senha = float(input("Por favor, digite a senha: "))
    print("Para fazer o login foram utilizadas {} tentativas" .format(tentativas))


