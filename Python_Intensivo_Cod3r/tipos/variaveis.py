a = 3
b = 4.4
print(a+b)

texto = 'Sua idade é ...'
idade = 23

# assim nao vai imprimir pois tem dois tipos diferentes
#print(texto + idade)
# se voce fizer assim ele aceita, mas nao é uma boa pratica
# print(texto+str(idade))

# melhor forma de fazer essa impressao é com o fstring
print(f'{texto} {idade}')  # dentro disso nao funciona o + pra concatenar


print(3 * 'Bom dia ')
saudacao = 'boa tarde '
print(3 * saudacao)


# constantes não existe em Python portanto tem uma convenção que diz para usar maíscula
PI = 3.1415
raio = float(input('Informe o raio da circunferencia: '))
#print(type(raio)) retorna o tipo da variável
#area = PI * pow(raio, 2)
area = PI * raio * raio
#print("A área é " + str(area))
print(f'A área é de {area} m2.')



