from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa,ano)
        self.__cilindradas = cilindradas
    # Sobrescrita do método __str__()
    def __str__(self):
        # Invoco o metodo __str__() da SUPERCLASSE (Veículo)
        # Armazeno o retorno na variável "retorno"
        retorno = super().__str__()
        # "retorno" com as "__cilindradas"
        return f'''{retorno}
    - Cilindradas: {self.__cilindradas}'''



