# Exercício 1: criar programa para que professor seja capaz de digitar todas as notas da turma + Nome do aluno
# ordenar de forma crescente e saber quantos alunos tiraram 10

#OPÇÃO 1
# alunos = int(input("Digite a quantidade de alunos: "))
# notas_classe = {}
#
# for x in range(0,alunos):
#     nome=input("Digite o nome do aluno: ")
#     nota=input("Digite a nota do aluno: ")
#     notas_classe[nome]=nota
# print(notas_classe)

#OPÇÃO 2

notas = {}
encerrrar = 'NÃO'

while 'N' in encerrrar.upper():
    aluno = input('Por favor, digite o nome do aluno: ')
    nota = float(input('Por favor, digite a nota do aluno: '))
    notas[aluno] = nota

    encerrrar = input('Deseja FINALIZAR a digitação? S- SIM ou N - NÃO  ')

total = 0

for nota in notas.values():
    if nota == 10.00:
        total = total +1
print('Ao todo, {} alunos tiraram nota 10!'.format(total))

print('NOTAS DA TURMA: ')
for aluno, nota in notas.items():
    print('O aluno {} tirou nota {}'.format(aluno,nota))