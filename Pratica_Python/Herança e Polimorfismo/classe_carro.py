from classe_chave_eletrica import Chave


class Carro(Chave):

    def __init__(self, marca, cor, placa):
        self.marca = marca
        self.cor = cor
        self.placa = placa

    def ligar(self):
        Chave.ligado(self)

    def desligar(self):
        Chave.desligado(self)
    
    def dados_do_carro(self):
        print(self.marca, self.cor, self.placa)



carro1 = Carro('Gol', 'Branco', 'ASD-3425')
# print(carro1.marca, carro1.cor,carro1.placa)
carro1.dados_do_carro()
carro1.ligar()
carro1.desligar()