def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

#pode armazenar a função dentro de uma variável
somar = soma
print(somar(3,4))

#uma função que tem como parametro outra função
def operacao_aritmetica(funcao, operador1, operador2):
    return funcao(operador1, operador2)

resultado = operacao_aritmetica(soma,13, 48)
print(resultado)


resultado = operacao_aritmetica(subtracao,13, 48)
print(resultado)


#função que retorna outra função 
def soma_parcial(a):
    #processamento pesado 1 - 10s que depende so da variavel a
    #processamento pesado 2 - 10s que depende so da variavel a
    #processamento pesado 3 - 40s que depende so da variavel a
    def concluir_soma(b):
        return a + b #10s
    return concluir_soma

# funcao = soma_parcial(10)
# resultado_final= funcao(12)
# print(resultado)

#tambem da para fazer assim:
resultado_final = soma_parcial(10)(12)
print(resultado_final)