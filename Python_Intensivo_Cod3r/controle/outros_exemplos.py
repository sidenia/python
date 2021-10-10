
#Um for dentro do outro
pessoas = ['Gui', 'Rebeca']
adj = ['capeca', 'inteligente']

for p in pessoas:
    for a in adj:
        print(f'{p} é {a}!')


#para um laço vazio usa-se o PASS
for i in [1,2,3]:
    pass

#só mostra os valores pares = usando CONTINUE = interrompe a repetição e vai pra próxima
for i in range(1, 10):
    if i % 2 == 1:
        continue #sempre que for impar ele continua e só imprimi abaixo ali se for par
    print(i, end=' ')

#usando BREAK = sai do laço quando atingir a condição

for i in range(1, 11):
    if i == 5:
        break
    print(i, end=' ')

print('FIM!')