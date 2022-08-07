print('Bem Vindo a Loja do Ivisson Hiago')
valor = float(input('Entre com valor do produto:'))
quantidade = int(input('Entre com valor do quantidade:'))

#inicia a variavel do desconto
desconto = 0

#condição para desconto de 3%
if quantidade > 4 and quantidade <= 19:
  desconto = 0.03
#condição para desconto de 6%
elif quantidade > 19 and quantidade <= 99:
  desconto = 0.06
#condição para desconto de 10%
elif quantidade > 99:
  desconto =0.1
#sem desconto
else:
  desconto = 0

#calculo do valor sem o desconto. Ex. 10 * 15 = 150
valorTotalSemDesconto = valor * quantidade

#calculo do valor com o desconto. Ex. 100 - (100 * 0.03) = 97
valorTotalComDesconto = valorTotalSemDesconto - valorTotalSemDesconto*desconto

print(f'O valor sem desconto foi: R$ {valorTotalSemDesconto}')
print(f'O valor com desconto foi: R$ {valorTotalComDesconto} (desconto {desconto*100}%)')