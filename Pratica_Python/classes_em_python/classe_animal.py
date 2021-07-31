class Animal:
    
    def __init__(self, especie, tamanho):
        self.especie = especie
        self.tamanho = tamanho
    
    def carnivoro(self):
        print('Animal Carnívoro')
    
    def herbivoro(self):
        print('Animal herbívoro')

    def dados_do_animal(self):
        print(self.especie, self.tamanho)


