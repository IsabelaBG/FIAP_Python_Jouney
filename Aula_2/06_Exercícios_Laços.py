#Ex 1: exibir os números pares de 0 a 100
for n in range(0,101):
    if(n%2==0):
        print(n)

print('-------------------------------')

#Ex 2: exibir a soma dos números de 0 a 100
soma = 0
n = 0
while(n<=100):
    soma= soma+n
    n=n+1
print(soma)
print('-------------------------------')

#Ex 3: exibir o fatorial de um número fornecido pelo usuário
fatorial = 1
número = int(input('Insira o número para cálculo do fatorial: '))
for número in range(1,número+1):
    #fatorial = número * fatorial
    fatorial *= número
print ('{}! = {}'.format(número,fatorial))
print('-------------------------------')

#Ex 4: exibir horas, minutos e segundos de 1 dia
for h in range(0,24,1):
    for m in range(0,61,1):
        for s in range(0,61,1):
            print('Horas: {}, Minutos: {}, Segundos: {}'.format(h,m,s))