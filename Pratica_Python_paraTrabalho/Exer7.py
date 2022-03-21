lista = []
lista_inv = []
numero_par = 0
contador = 0

while (contador < 10):
    numero_par = int(input("Insira um numero: "))
    if(numero_par % 2 == 0):
        lista.append(numero_par)
        contador += 1
    else:
        pass
print(lista)

for i in range(9, -1, -1):
    lista_inv.append(lista[i])
print(lista_inv)
