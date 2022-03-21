lista = []
soma_impar = 0
soma_par = 0
soma_total = 0
contador_impar = 0

for i in range(5):
    valor_lista = int(input("Insira um valor: "))
    lista.append(valor_lista)
    soma_total = soma_total + lista[i]

    if (lista[i] % 2 == 0):
        soma_par = soma_par + lista[i]
    else:
        soma_impar = soma_impar + lista[i]
        contador_impar += 1

porcent_impar_par = (contador_impar/5)*100
print("A soma dos numeros ímpares é igual a ", soma_impar)
print("A soma dos numeros pares é igual a ", soma_par)
print("A soma total dos numeros é igual a ", soma_total)
print(round(porcent_impar_par, 2), "%. dos valores sao impares")
