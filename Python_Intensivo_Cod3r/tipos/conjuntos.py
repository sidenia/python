#classe set
#diferente de listas e tuplas conjuntos não aceitam
#elementos duplicados

#print({1, 2, 3})
print(type({1, 2, 3}))
#print({1, 2, 3, 3, 3, 3, 3})

#conj não é uma estrutura indexada, nao tem index
conj = {1, 2, 3, 3, 3, 3, 3} 
#print(conj[1]) #set object nao suporta indexação
print(conj)
print(len(conj))
