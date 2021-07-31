#operadores ternarios
#f string é do python 3
lockdown = True
grana = 30

# parte verdadeira + conexao logica + parte falsa
status = 'Em casa' if lockdown else 'Uhuuu'

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuu'

print(status)
print(f'O status é {status}')