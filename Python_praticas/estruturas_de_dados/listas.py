L = [5,6,7]
list = [1, 'si', 3, 3, {'nome': 're'}, ['more', 'mio']]

list.append('teste')
# Adiciona um item ao fim da lista; equivale a a[len(a):] = [x].

list.extend(L)
# CONCATENA em uma lista, a outra passada como parametro
# Prolonga a lista, adicionando no fim todos os elementos da lista L passada como argumento; equivalente a a[len(a):] = L.

list.insert(0, 5)
# Insere um item em uma posição especificada. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, assim a.insert(0, x) insere no início da lista, e a.insert(len(a), x) equivale a a.append(x).

list.remove(3)
# Remove o primeiro item encontrado na lista cujo valor é igual a x. Se não existir valor igual, uma exceção ValueError é levantada.

list.pop()
list.pop([i])
# Remove o item nasposição dada e o devolve. Se nenhum índice for especificado, a.pop() remove e devolve o último item na lista. (Os colchetes ao redor do i indicam que o parâmetro é opcional, não que você deva digitá-los daquela maneira. Você verá essa notação com frequência na Referência da Biblioteca Python.)

list.index(x)
print(list.index('si'))
# Devolve o índice do primeiro item cujo valor é igual a x, gerando ValueError se este valor não existe

list.count(x)
print(list.count(3))
# Devolve o número de vezes que o valor x aparece na lista.

list.sort()
# # Ordena os itens na própria lista in place.

list.reverse()
# Inverte a ordem dos elementos na lista in place (sem gerar uma nova lista).

print(list)