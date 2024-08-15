#compare três metais e veja qual o mais pesado
#entrada de dados
ouro = float(input('Por favor, digite o peso do ouro: '))
prata = float(input('Por favor, digite o peso do prata: '))
cobre = float(input('Por favor, digite o peso do cobre: '))

if(ouro>prata):
    if(ouro>cobre):
        print('O ouro é o mais pesado')
    else:
        print('O cobre é o mais pesado')
elif(prata>cobre):
    print('A prata é mais pesada')