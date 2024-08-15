arquivo = open("arquivo-teste.txt")
# print(arquivo.read())
# print(arquivo.readline())

for linha in arquivo.readline():
    print(linha)

arquivo.close()