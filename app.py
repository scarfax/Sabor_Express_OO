from modelos.restaurante import Restaurante

restaurante_1 = Restaurante ('Bar do Zé', 'gourmet')
restaurante_1.receber_avaliacao ('Carosella', 3)
restaurante_1.receber_avaliacao ('Jacquin', 2)
restaurante_1.receber_avaliacao ('Rizzo', 5)

restaurante_2 = Restaurante ('Angu do Gosma', 'bristrô')
restaurante_2.receber_avaliacao ('Carosella', 8)
restaurante_2.receber_avaliacao ('Jacquin', 4)
restaurante_2.receber_avaliacao ('Rizzo', 3)

restaurante_3 = Restaurante ('Serjão Lanches', 'self service')

restaurante_1.alternar_estado()
restaurante_2.alternar_estado()

def main ():
    Restaurante.listar_restaurantes() 

if __name__=='__main__':
    main()