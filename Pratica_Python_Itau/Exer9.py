# matriz triagular inferior 5 x 5
import numpy as np
matriz = np.ones((5, 5))
for i in range(5):
    print("Elemento da Matriz com Índice", i, j)
    numero = int(input("Insira um valor: "))
    matriz[i, j] = numero
    if(i > j):
        matriz[i, j] = 0
    else:
        pass
print(matriz)
