#criando a classe
class Computador:
    #método construtor __init__  self = this em java.
    def __init__(self, marca, memoria, processador):
        self.marca = marca
        self.memoria = memoria
        self.processador = processador
    
    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou desligando')
    
    def Parametros(self):
        print(self.marca, self.memoria, self.processador)
    

#instanciando objetos
#self serve para acessar propriedades de uma instancia, sejam elas atributos ou métodos
computador1 = Computador('Asus', '16gb', 'Intel')
computador2 = Computador('Dell', '8gb', 'Ryzen5')
computador3 = Computador('Chromebook', '32gb', 'Ryzen3')

#print(computador1.marca, computador1.memoria, computador1.processador)
computador1.Parametros()
computador1.Ligar()
computador1.Desligar()

