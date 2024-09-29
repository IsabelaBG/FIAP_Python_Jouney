import numpy as np
#funções numpy para popular array, matrizes. ao indicar o ntype limita-se para inteiros

array_zerado = np.zeros((3,4))
print("O array gerado com 0 ficou assim: ")
print(array_zerado)

array_com_um = np.ones((5,2),dtype=np.int32)
print("O array gerado com 1 ficou assim: ")
print(array_com_um)

array_aleatorio = np.empty((6,3),dtype=np.int64)
print("O array gerado com valores aleatórios ficou assim: ")
print(array_aleatorio)

array_gerado = np.arange(10)
print("O array gerado ficou assim: ")
print(array_gerado)

array_gerado = np.arange(10).reshape(2,5)
print("O array gerado com reshape ficou assim: ")
print(array_gerado)