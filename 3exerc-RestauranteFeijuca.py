#variáveis
escolhendoOpcao = True
escolhendoAcompanhamento = True
arrayAcompanhamentos = [0,1,2,3,4]
selecaoAcompanhamentosCliente = []
valorTotalAcompanhamentos = 0
totalpagar = 0
dadosDoPedido = [
  {
    'volume': 0
  },
  {
    'opcao': '',
    'preco': 0,
    'aliquota': 0
  },
  {
    'acompanhamentos': []
  }

]
totalapagar = 0

print('Bem-vindo ao programa de feijoada do Ivisson Hiago')

def volumeFeijoada():
  """função que valida e coleta volume dentro do range aceito"""
  escolhendoVolume = True
  while escolhendoVolume:
    print('\nMenu volume Feijoada')
    volume = input('Entre com a quantidade que deseja(ml):')
    try:
      volume = int(volume)
    except ValueError:
      print('Entrada inválida. Valor esperado: numero. Tente novamente!')
      continue
    if volume < 300 or volume > 5000:
      print('Não aceitamos porções menores que 300ml ou maiores que 5L. Tente novamente!')
      continue
    else:
      volume = volume * 0.08  
      dadosDoPedido[0]['volume'] =  volume
    return volume


def opcaoFeijoada(volume):
  """função que coleta opcao de acordo com as disponíveis"""
  while escolhendoOpcao:
    opcao = input('\nEntre com a opção de feijoada: \nb - Básica (Feijão + paiol + costelinha \np - Premium (Feijão + paiol + costelinha + partes de porco \ns - Suprema (Feijão + paiol + costelinha + partes de porto + charque + calabresa + bacon\n')
    if 'b' in opcao:
      preco = volume * 1
      dadosDoPedido[1]['opcao'] = 'b'
      dadosDoPedido[1]['preco'] = preco
      dadosDoPedido[1]['aliquota'] = 1
      return
    elif 'p' in opcao:
      preco = volume * 1.25
      dadosDoPedido[1]['opcao'] = 'p'
      dadosDoPedido[1]['preco'] = preco
      dadosDoPedido[1]['aliquota'] = 1.25
      return
    elif 's' in opcao:
      preco = volume * 1.25
      dadosDoPedido[1]['opcao'] = 's'
      dadosDoPedido[1]['preco'] = preco
      dadosDoPedido[1]['aliquota'] = 1.50
      return
    else:
      print('Você não digitou uma opção válida!')
      continue


def acompanhamentoFeijoada():
  """função que coleta opcoes de acompanhamento de acordo com as disponíveis"""
  while escolhendoAcompanhamento:
    escolha = int(input('\nDeseja mais algum acompanhamento: \n0- não desejo mais acompanhamentos(encerrar pedido) \n1- 200g de arroz \n2- 150g de farofa especial \n3- 100g de couve cozida \n4- laranja descascada\n'))

    if escolha in arrayAcompanhamentos:
      if escolha == 0:
        break
      if escolha == 1:
        selecaoAcompanhamentosCliente.append(escolha)
        continue
      if escolha == 2:
        selecaoAcompanhamentosCliente.append(escolha)
        continue
      if escolha == 3:
        selecaoAcompanhamentosCliente.append(escolha)
        continue
      if escolha == 4:
        selecaoAcompanhamentosCliente.append(escolha)
        continue
    else:
      print('Opcão inválida! Tente novamente!')
      continue
  dadosDoPedido[2]['acompanhamentos'] = selecaoAcompanhamentosCliente
  return

#chamada das funções
volumeFeijoada()
opcaoFeijoada(dadosDoPedido[0]['volume'])
acompanhamentoFeijoada()

# soma dos valores dos acompanhamentos
listaAcompanhamentos = dadosDoPedido[2]['acompanhamentos']
for acomp in listaAcompanhamentos:
  if acomp == 1:
    valorTotalAcompanhamentos += 1 * 5
    continue
  if acomp == 2:
    valorTotalAcompanhamentos += 1 * 6
    continue
  if acomp == 3:
    valorTotalAcompanhamentos += 1 * 7
    continue
  if acomp == 4:
    valorTotalAcompanhamentos += 1 * 3
    continue
  else:
    break

volumePedido = dadosDoPedido[1]['preco']
aliquotaPedido = dadosDoPedido[1]['aliquota']

totalapagar = volumePedido + valorTotalAcompanhamentos
print(f'O valor a ser pago é (R$): {totalapagar} (volume = {volumePedido} * opcao = {aliquotaPedido} + acompanhamento = {valorTotalAcompanhamentos})' )