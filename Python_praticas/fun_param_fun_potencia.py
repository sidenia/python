def cria_potencia(x):
    def potencia(num):
        return x ** num
    return potencia

# Potência de 2 e 3
potencia_2 = cria_potencia(2)
potencia_3 = cria_potencia(3)

# Resultado
print(potencia_2(2))
print(potencia_3(2))

########################################################
#pra adicionar algum comportamento antes ou depois de alguma funcao
def decorator(funcao):
    def wrapper():
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print ("Estou depois da execução da função passada como argumento")

    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")

funcao_decorada = decorator(outra_funcao)
funcao_decorada()