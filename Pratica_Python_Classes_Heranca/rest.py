import requests

def consulta():
    response = requests.get('http://127.0.0.1:5000/pessoa/')
    print(response.status_code)
    for pessoa in response.json():
        print(pessoa['id'], pessoa['nome'], pessoa['idade'])

def insere():
    nome: "Larissa"
    idade = 22
    pessoa = {"nome": nome, "idade": idade}
    response = requests.post('http://127.0.0.1:5000/pessoa/', json=pessoa)
    print(response.status_code)
    print(response.json())

#consulta
