nota = float(input('Informe o valor da nota: '))
comportado = True if input('Comportado (s/n): ') == 's' else False

print(nota)

if nota >= 9 and comportado:
    print('Parabéns! Quadro de honra!')
elif nota >= 6:
    print('Aprovado')
else: 
    print('Você reprovou')