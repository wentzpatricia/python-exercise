from City import City
from Color import Color

color = Color()
class State:
    def __init__(self, nome_estado, sigla):
        self.__nome = nome_estado
        self.__sigla = sigla
        self.__lst_cidades = []
        self.__qtd_casos_estado = 0
    
    def get_sigla(self):
        return self.__sigla

    def get_estado(self):
        return self.__nome

    def get_lista_cidade(self):
        return self.__lst_cidades

    def set_lista_cidade(self, cidade):
        self.__lst_cidades.append(cidade)

    def imprime_cidades(self):
        print(f"\n{color.cyan}=-=-=-=-=- Relatório de cidades =-=-=-=-=-=-{color.endColor}")
        for cidade in self.__lst_cidades:
           print(f"{color.cyan}--->{color.endColor} {cidade.get_cidade().ljust(15)}{color.cyan}|{color.endColor} Casos registrados: {cidade.get_qtd_casos_cidade()}")
           print("")
    def verifica_cidade(self, nome_cidade):
        for cidade in self.__lst_cidades:
            if cidade.get_cidade() == nome_cidade:
                return True
            else: (f"{color.red}Erro.{color.endColor} Cidade não encontrada. [Enter]")

    def set_qtd_casos_estado(self, qt_deCasos):
        self.__qtd_casos_estado += qt_deCasos

    def get_qtd_casos_estado(self):
        return self.__qtd_casos_estado

    def __str__(self):
        return f"{self.__nome}({self.__sigla}).... {self.__qtd_casos_estado}"


         

