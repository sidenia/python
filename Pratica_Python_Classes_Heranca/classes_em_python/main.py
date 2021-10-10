from classe_animal import Animal

canino = Animal('Cachorro', 'médio')
felino1 = Animal('Gato', 'pequeno')
felino2 = Animal('Onça', 'grande')
inseto = Animal('Formiga', 'pequeno')

canino.dados_do_animal()
canino.carnivoro()

felino1.dados_do_animal()
felino1.carnivoro()

felino2.dados_do_animal()
felino2.carnivoro()

inseto.dados_do_animal()
inseto.herbivoro()