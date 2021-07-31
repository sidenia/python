
for i in range(10):
    print(i)

print("==============================")

for i in range(11):
    print(i)

print("==============================")

            #ini  fim  passo
for i in range(1, 100, 7): # de 1 até 100, pulando de 7 em 7 (passo 7)
    print(i)

print("==============================")


for i in range(20, 0, -3): # de 20 decresce até 0 com passo de 3
    print(i)

print("==============================")

#percorrendo lista
numeros = [2, 4, 6, 8]
for n in numeros:
    #imprimir todos na mesma linha com end passando o espaço ou vírgula
    print(n, end=" ")

print("==============================")

texto = "Python é muito massa!"
for letra in texto:
    print(letra, end=' ')

print("==============================")


#mesmo que o set nao seja indexado voce pode percorrer com o for
for n in {1, 2, 4, 4}:
    print(n, end=' ')

print("==============================")


#for em um dicionário
produto = {
    'nome': 'caneta',
    'preço': 8.80,
    'desconto': 0.5
}

for atributo in produto:
    print(atributo,':', produto[atributo])

print("==============================")
            #subst. produto[atributo]
for atributo, valor in produto.items():
    print(atributo,':', valor)

print("==============================")
#para percorrer só os valores:
for valor in produto.values():
    print(valor, end=' ')


print("==============================")
#para percorrer só as chaves (atributos):
for atributos in produto.keys():
    print(atributos, end=' ')
