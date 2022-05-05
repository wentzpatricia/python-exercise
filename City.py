class City:
    def __init__(self, nome_cidade):
        self.__cidade = nome_cidade
        self.__qtd_casos_cidade = 0

    def get_cidade(self):
        return self.__cidade

    def set_qtd_casos_cidade(self, qt_deCasos_cidades):
        self.__qtd_casos_cidade += qt_deCasos_cidades
    
    def get_qtd_casos_cidade(self):
        return self.__qtd_casos_cidade

    def __str__(self):
        return f"{self.get_cidade()}|{self.__cidade} {self.__qtd_casos_cidade}"