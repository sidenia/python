print('Bem Vindo a Pizzaria do Ivisson Hiago')
print('----------------------Cardápio----------------------')
print('| Código | Descrição  | Pizza Média(M) | Pizza Grande(G)|')
print('|   21   | Napolitana |    R$ 20,00    |     R$ 26,00   |')
print('|   22   | Margherita |    R$ 20,00    |     R$ 26,00   |')
print('|   23   | Calabresa  |    R$ 25,00    |     R$ 32,50   |')
print('|   24   | Toscana    |    R$ 30,00    |     R$ 39,00   |')
print('|   25   | Portuguesa |    R$ 30,00    |     R$ 39,00   |')
print('----------------------------------------------------')


# variáveis
comprando = 1
escolhendoTamanho = True
escolhendoSabor = True
pedido = []
valorTotal = 0

#array com códigos dos sabores das pizzas
arraySabores = [21,22,23,24,25]
#dicionário com os valores das pizzas por sabor e tamanho

pizzas = [
  {
    'napolitana': {
      'codigo': 21,
      'm': 20,
      'g': 26
    },
    'margherita': {
      'codigo': 22,
      'm': 20,
      'g': 26
    },
    'calabresa': {
      'codigo': 23,
      'm': 25,
      'g': 32.50
    },
    'toscana': {
      'codigo': 24,
      'm': 30,
      'g': 39
    },
    'portuguesa': {
      'codigo': 25,
      'm': 30,
      'g': 39
    },
  } 
]

while comprando == 1:
  #escolha de tamanho com opcao inválida caso entrada seja diferente de m ou g
  while escolhendoTamanho:
    tamanho = input('Qual o tamanho de pizza que deseja (M/G): ').lower()
    if 'm' in tamanho or 'g' in tamanho:
      break
    else:
      print('Opcao invalida')
      continue

  #escolha de sabor com opcao inválida caso entrada seja dos códigos de sabor existentes
  while escolhendoSabor:
    codigo = int(input('Entre com o código do sabor desejado: '))
    if codigo in arraySabores:
      if codigo == 21:
        print('Voce pediu uma Pizza Napolitana')
        pedido.append(pizzas[0]['napolitana'][tamanho])
      elif codigo == 22:
        print('Voce pediu uma Pizza Margherita')
        pedido.append(pizzas[0]['margherita'][tamanho])
      elif codigo == 23:
        print('Voce pediu uma Pizza Calabresa')
        pedido.append(pizzas[0]['calabresa'][tamanho])
      elif codigo == 24:
        print('Voce pediu uma Pizza Toscana')
        pedido.append(pizzas[0]['toscana'][tamanho])
      elif codigo == 25:
        print('Voce pediu uma Pizza Portuguesa')
        pedido.append(pizzas[0]['portuguesa'][tamanho])
      break
    else:
      print('Opcao invalida')
      continue

  print('Deseja pedir mais alguma coisa ?')
  print('Digite 1 - Sim')
  print('Digite 0 - Não')
  comprando = int(input('resposta:'))
  
  if comprando == 0:
    break

#valor total do pedido, soma dos elementos do array
valorTotal = sum(pedido)
print(f'O total do seu pedido é R$ {valorTotal}')
print('Agradecemos a preferência')