#operadores logicos
# não existe ou exclusivo (xor) em python
#tabela verdade

b1 = True
b2 = False
b3 = True

print(b1 and b2 and b3)  # false
print(b1 or b2 or b3)   # true
print(b1 != b2) #!= equivale ao xor ^
print(not b1)
print(not b2)

print(b1 and not b2 and b3)

x = 3
y = 4

print(b1 and not b2 and x < y)