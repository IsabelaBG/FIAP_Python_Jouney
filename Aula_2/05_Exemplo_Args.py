def teste_args(arg,*args):
    print('primeiro argumento: {}'.format(arg))
    for argumentos in args:
        print('demais argumentos: {}'.format(argumentos))

teste_args('Hello', 'World','!','!')