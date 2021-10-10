nomes = ('Francisca', 'Sidenia', 'Sidenia', 'Bezerra')
#valores de tupla nao podem ser alterados.

print(type(nomes))
print(nomes[0])
print(nomes[1:2]) #imprimirá só o primeiro, nao incluirá o segundo
print(nomes[1:3]) #inclui o segundo elemento mas nao imprimi o 3
print(nomes[1:-1]) #imprimi do primeiro ao penultimo
print(nomes[1:]) #imprime do primeiro ao ultimo
print(nomes[2:]) #todos à partir do terceiro (nao inclui o segundo)
print(nomes[:-2]) #todos até o antepenultimo
print(nomes)
print('Sidenia' in nomes)

x = ('Renata')
print(type(x)) #sairá como string porque o paranteses nao é usado só para tupla
# mas se voce inserir uma virgula após o nome ('Renata',) mesmo que tenha só um ai vai imprimir tipo tupla
