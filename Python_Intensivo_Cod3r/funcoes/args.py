
#recebera uma tupla ou uma lista
def soma(*args): #poderiamos chamar esse args de nums
    total = 0
    for n in args:
        total += n
    return total

#recebera um dicionario 1
# def resultado_final(**kwargs): #key word args  argumentos nomeados
#     print(kwargs['nome'])
#     print(kwargs['nota'])


#recebera um dicionario com quantos pares chave+valor eu quiser
def resultado_final(**kwargs): #keyword arguments  argumentos nomeados / argumentos de palavra chave
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
    return f'{kwargs["nome"]} foi {status}'