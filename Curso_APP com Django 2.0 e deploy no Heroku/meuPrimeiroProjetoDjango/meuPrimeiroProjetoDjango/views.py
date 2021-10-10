from django.http import HttpResponse


def hello(request):
    return HttpResponse('Ola mundo')


def articles(request, year):
    return HttpResponse('O ano informado foi:' + str(year))

    # def fname(request, ano, mes, dia):
    #     a = []
    #     b = 2
    #     lerClientesBanco()
    #     for item in a:
    #         salvaNoBanco()

# posso criar uma função que ajuda outra função e ela nao precisa ser importada para urls
# ex:


def lerDoBancoDeDados(nome):
    # podeia ser uma query do banco
    lista_nomes = [
        {'nome': 'Ana', 'idade': 25},
        {'nome': 'pedro', 'idade': 22},
        {'nome': 'joao', 'idade': 24},
    ]

######################### ENCONTRA ANA MAS NÃO ENCONTRA OS OUTROS DOIS NOMES

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome': 'Não encontrado!', 'idade': 0}


def fname(request, nome):
    result = lerDoBancoDeDados(nome)
    if result['idade'] > 0:
        return HttpResponse("Pessoa encontrada: " + result['nome'] + " tem " + str(result['idade']) + " anos")    
    else:
        return HttpResponse('Pessoa não encontrada!')