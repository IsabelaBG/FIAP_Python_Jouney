# Problema: otimizar um código de calculadora, para modulariza-los em funções

#CÓDIGO ORIGINAL
#
# opcao = 0
# while opcao !=6:
#     print("PROGRAMA CALCULADORA")
#     print("Escolha sua opção: ")
#     print("1 - Digitar valores")
#     print("2 - Realizar soma")
#     print("3 - Realizar subtração")
#     print("4 - Realizar divisão")
#     print("5 - Realizar multiplicação")
#     print("6 - Sair")
#     opcao = int(input("\nPor favor, insira sua opção: \n"))
#     if opcao == 1:
#         valor1 = float(input("Digite o 1º valor: "))
#         valor2 = float(input("Digite o 2º valor: "))
#         print("Os valores {} e {} foram armazenados \n\n".format(valor1,valor2))
#     elif opcao == 2:
#         print("\n\nRealizando uma soma entre {} e {}".format(valor1,valor2))
#         soma = valor1+valor2
#         print("O resultado da foi {}\n\n".format(soma))
#     elif opcao == 3:
#         print("\n\nRealizando uma substração entre {} e {}".format(valor1,valor2))
#         sub = valor1-valor2
#         print("O resultado da foi {}\n\n".format(sub))
#     elif opcao == 4:
#         print("\n\nRealizando uma divisão entre {} e {}".format(valor1,valor2))
#         div = valor1/valor2
#         print("O resultado da foi {}\n\n".format(div))
#     elif opcao == 5:
#         print("\n\nRealizando uma multiplicação entre {} e {}".format(valor1,valor2))
#         multi = valor1*valor2
#         print("O resultado da foi {}\n\n".format(multi))
#     elif opcao == 6:
#         print("Saindo do sistema")
#     else:
#         print("Opção inválida")

#CÓDIGO OTIIMIZADO

def exibir_menu():
    print("PROGRAMA CALCULADORA")
    print("Escolha sua opção!")
    print("1 - Digitar valores")
    print("2 - Realizar soma")
    print("3 - Realizar subtração")
    print("4 - Realizar divisão")
    print("5 - Realizar multiplicação")
    print("6 - Sair")

def exibe_resultado(resultado):
	print("O resultado foi {}".format(resultado))

def somar(valor1, valor2):
	soma = valor1 + valor2
	return soma

def subtrair(valor1, valor2):
	sub = valor1 - valor2
	return sub

def dividir(valor1, valor2):
	div = valor1 / valor2
	return div

def multiplicar(valor1, valor2):
	mult = valor1 * valor2
	return mult

opcao = 0
while(opcao != 6):
    exibir_menu()
    opcao = int(input("\nPor favor, insira sua opção:\n"))
    if (opcao == 1):
        valor1 = float(input("Digite o 1º valor"))
        valor2 = float(input("Digite o 2º valor"))
        print("Os valores {} e {} foram armazenados\n\n".format(valor1, valor2))
    elif (opcao == 2):
        print("\n\nRealizando a soma entre {} e {}".format(valor1, valor2))
        exibe_resultado(somar(valor1, valor2))
    elif (opcao == 3):
        print("\n\nRealizando a subtração entre {} e {}".format(valor1, valor2))
        exibe_resultado(subtrair(valor1, valor2))
    elif (opcao == 4):
        print("\n\nRealizando a divisão entre {} e {}".format(valor1, valor2))
        exibe_resultado(dividir(valor1, valor2))
    elif (opcao == 5):
        print("\n\nRealizando a multiplicação entre {} e {}".format(valor1, valor2))
        exibe_resultado(multiplicar(valor1, valor2))
    elif (opcao == 6):
        print("Saindo do sistema...")
    else:
        print("Opção inválida")

