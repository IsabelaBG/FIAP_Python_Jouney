# Exercício 1: criar programa para que professor seja capaz de digitar todas as notas da turma
# ordenar de forma crescente e saber quantos alunos tiraram 10

#OPÇÃO 1
lista_notas = []
quantidade_alunos = int(input("Digite a quantidade de alunos: "))


while len(lista_notas)<quantidade_alunos:
    notas = int(input("Digite a nota do aluno: "))
    lista_notas.append(notas)

lista_notas.sort()
lista_notas.reverse()
print("A listagem de notas é: {} ".format(lista_notas))
notas_10= lista_notas.count(10)
print("A quantidade de alunos que tiraram 10 foi: {}".format(notas_10))

#OPÇÃO 2
# notas = []
# encerrar = "NÃO"
#
# while "N" in encerrar.upper():
#     notas.append(float(input("Por favor, digite uma nova nota: ")))
#     encerrar = input ("Deseja FINALIZAR a digitação? S- Sim ou N - Não")
# print("Ao total, {} alunos tiraram nota 10!".format(notas.count(10)))
#
# notas.sort()
# notas.reverse()
#
# print("NOTAS DA TURMA: ")
# for nota in notas:
#     print(nota)