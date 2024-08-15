conteudo = "Teste de criação de arquivo de texto."

arquivo = open("novo-teste.txt","w")

arquivo.write(conteudo)
arquivo.close()

add = "Testando add novo texto."

arquivo = open("novo-teste.txt", "a")
arquivo. write(add)
arquivo.close()