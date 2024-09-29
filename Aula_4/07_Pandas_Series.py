import pandas as pd
import numpy as np

serie = pd.Series([1,3,5,6,9])

print("Essa é uma estrutura de série no pandas: {}".format(serie))

indice = np.array(["A","B","C","D","E"])
serie = pd.Series([1,3,5,6,9], index = indice)
print("Essa é uma estrutura de série com um índice nomeado no pandas: {}".format(serie))