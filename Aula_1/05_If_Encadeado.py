print('PROGRAMA VALIDADOR DE PASSAGEIROS')
idade = int(input('Por favor, digite a idade do passageiro: '))

"""
if (idade < 16):
    print('O passageiro não pode votar nem embarcar')
else:
    if(idade >=18):
        print('O passageiro deve votar e pode embarcar')
    else:
       print('O voto é opcional e pode embarcar')
"""

if (idade < 16):
    print('O passageiro não pode votar nem embarcar')
elif(idade >=18):
    print('O passageiro deve votar e pode embarcar')
else:
    print('O voto é opcional e pode embarcar')


