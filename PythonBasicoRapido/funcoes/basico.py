# Python nao tem sobrecarga
# voce pode ter duas funcoes com mesmo nome e parametros diferentes
# elas serão interpretadas de forma diferente.

def saudacao():
    print('Bom dia')

# passandao parametro padrão, ou seja quando não for preenchido trará isso!

def saudacao(nome = 'Ituber'):
    print(f'Bom dia {nome}!')

def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia {nome}!\nVocê tem {idade} anos ?\n')

#só executa a função se rodar o python no arquivo principal
if __name__ == '__main__':
    saudacao('Ana', 30)

def soma_e_multiplica(a, b, x):
    return a + b * x