#Problema: elaborar um programa que recebe um número inteiro, calcula e exibe a tabuada desse número

# OPÇÃO 1:
Número = int(input("Por favor, digite um número inteiro: "))
Multiplicador = 1
while (Multiplicador <= 10):
    Multiplicacao = Número * Multiplicador
    Multiplicador = Multiplicador +1
    print(Multiplicacao)

# OPÇÃO 2:

# Número = int(input("Digite o número que deseja saber a tabuada: "))
# for multiplicador in range(1,11,1):
#     produto = multiplicador * Número
#     print("{} x {} = {}".format(multiplicador,Número,produto))

