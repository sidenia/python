#para essa solução com quantidade determinada melhor usar o for para esse ex abaixo
#x = 10

#while x:
#    print(x)
#    x -= 1

#print('Fim!')



#x = 0

#while x != -1:
#    x = float(input('Informe um numero ou -1 para sair: '))

#print('FIM')


total = 0
qnte = 0
nota = 0

while total != -1:
    total = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qnte += 1
        total += nota

print(f'A média da turma é {total / qnte}')