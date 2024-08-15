#Criação de um dicionário JSon
import _json
import json

contatos = {
    "Clark Kent":
        {"Celular":"11999333777",
         "Email":"super@krypto.co"},
    "Bruce Wayne":
        {"Celular":"1188888999",
         "Email":"bat@kaverna.co"}
}

dados_json = json.dumps(contatos, indent=3)
print(dados_json)