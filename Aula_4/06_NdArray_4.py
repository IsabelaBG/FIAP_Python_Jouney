import numpy as np
# Cálculos algébricos
array_inicial = np.array([[499.50,25.00,15.48],[350.15,19.12,17.30]])
array_resultado = array_inicial - 2.5
print("O ndarray resultado após a operação de subtração é: ")
print(array_resultado)

array_resultado = array_inicial * 10
print("O ndarray resultado após a operação de multiplicação é: ")
print(array_resultado)

array_resultado = array_inicial **2
print("O ndarray resultado após a operação de exponenciação é: ")
print(array_resultado)

array_resultado = array_inicial >40
print("O ndarray resultado após a operação de comparação é: ")
print(array_resultado)

#Operações matriciais

array_a = np.array([[0,1],[2,0]])
array_b = np.array([[2,0],[4,3]])
array_sub = array_a - array_b
print("O resultado da subtração é: {}".format(array_sub))

array_multi1 = array_a * array_b
print("O resultado da multiplicação entre os elementos é: {}".format(array_multi1))

array_multi2 = array_a @ array_b
print("O resultado da multiplicação entre as matrizes é: {}".format(array_multi2))

#Operações básicas
print("O resultado da soma do elementos da matriz é : {}".format(array_a.sum()))

print("O maior elemento da matriz é : {}".format(array_a.max()))

print("O menor elemento da matriz é : {}".format(array_a.min()))

print("O resultado da soma de cada uma das colunas da matriz é : {}".format(array_a.sum(axis=0)))
