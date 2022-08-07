print('Bem-vindo ao controle de estoque da Mercearia do Ivisson Hiago')
estoque = []
opcaoSelecionada = 0
codigo = 0

def cadastrarProduto(codigo):
  """Função responsável pelo cadastro de produtos no estoque"""
  print("Você selecionou a opção Cadastrar Produto")
  print("Código do Produto 00" + str(codigo))
  nome_produto = input("Por favor entre com o nome do produto: ").capitalize()
  fabricante = input("Por favor entre com o nome do fabricante: ").capitalize()
  valor_produto = float(input("Por favor entre com o valor do produto:"))

  estoque.append(
      {
          "CODIGO":codigo,
          "NOME":nome_produto,
          "FABRICANTE":fabricante,
          "VALOR":valor_produto
      }
  )
  return print('Produto Cadastrado com sucesso!')
   
def consultar_produto():
  """Função responsável pela consulta de produtos no estoque, todos, por código ou por fabricante"""
  opcoesDisponiveis = [1,2,3,4]
  id = None

  # se o estoque tiver vazio volta ao menu principal
  if len(estoque) == 0:
    print('Não há produtos em estoque! Cadastre um produto antes de consultar!')
    return

  while not id in opcoesDisponiveis:
    id = input("\nEscolha a opção desejada: \n1 - Consultar todos os produtos \n2 - Consultar produtos por código \n3 - Consultar produtos por fabricante \n4 - Retornar\n")
    try:
      id = int(id)
    except ValueError:
      print('Entrada inválida. Tente novamente! Valor esperado de 1 a 4')
      continue
    # consulta todos os produtos
    if id == 1:
      for produto in estoque:
        print(produto)
        id = None
        continue
    # consulta produtos por código
    elif id == 2:
      print("Digite o código do produto: ")
      codigo_digitado = int(input())
      for produto in estoque:
        try:
          if produto['CODIGO'] == codigo_digitado:
              print(produto)
              id = None
          continue
        except:
          print("Código não encontrado")
          continue
    # consulta produtos por fabricante
    elif id == 3:
      print("Digite o fabricante do(s) produto(s): ")
      fabricante_digitado = input().capitalize()
      for produto in estoque:
          try:
            if produto['FABRICANTE'] == fabricante_digitado:
              print(produto)
              id = None
              continue
          except:
            print("Fabricante não encontrado. Tente novamente!")
            id = None
            continue         
    # retorna ao menu principal
    elif id == 4:
      return
    #valida número fora do range permitido de opcoes
    else:
      print("Opção inválida. Digite um valor de 1 a 4.")
      id = None
      continue
  
def remover_produto():
    """Função responsável por deletar produtos do estque"""
    print("Digite código para remover o produto: ")
    codigo_para_remover = int(input())
   
    for produto in estoque:
        if produto["CODIGO"] == codigo_para_remover:
            estoque.pop(estoque.index(produto))
   
    return print(f'Produto {codigo_para_remover} removido com sucesso!')

#Execução do programa, chamada de funções  
while opcaoSelecionada != 4:
  opcaoSelecionada = input('\nEscolha a opção desejada: \n1 - Cadastrar produto \n2 - Consultar produtos \n3 - Remover produto \n4 - sair\n')
  
  try:
    opcaoSelecionada = int(opcaoSelecionada)
  except ValueError:
    print('Entrada inválida. Valor esperado: numero de 1 a 4. Tente novamente!')
    continue

  if opcaoSelecionada == 1:
    codigo+= 1
    cadastrarProduto(codigo)
  elif opcaoSelecionada == 2:
    consultar_produto()
  elif opcaoSelecionada == 3:
    remover_produto()
  elif opcaoSelecionada == 4:
    break
  else:
    print('Opcão inválida. Tente novamente!  Digite um número de 1 a 4.')
    continue