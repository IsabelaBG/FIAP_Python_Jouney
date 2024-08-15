import numpy as np

#convertendo lista em array usando NumPy
lista = [1,2,3]
print(lista)
novo_array = np.array(lista)
print(novo_array)

print("Esse é um ndarray com {} dimensões".format(novo_array.ndim))
print("As dimensões desse ndarray possuem os seguintes tamanhos: {}".format(novo_array.shape))
print("Ao todo, esse ndarray contém {} elementos".format(novo_array.size))
print("Os elementos presentes nesse ndarray são do tipo: {}".format(novo_array.dtype))
print("Os elementos presentes nesse ndarray ocupam: {} bytes".format(novo_array.itemsize))