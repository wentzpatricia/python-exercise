from City import City

class Estado:
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
        print("\n","\033[1;36m=-"*4,"Relatório de cidades:","=-"*4,"\033[0;0m\n")
        for cidade in self.__lst_cidades:
           print(f"\033[1;36m--->\033[0;0m {cidade.get_cidade().ljust(15)}\033[1;36m|\033[0;0m Casos registrados: {cidade.get_qtd_casos_cidade()}")
           print("")
    def verifica_cidade(self, nome_cidade):
        for cidade in self.__lst_cidades:
            if cidade.get_cidade() == nome_cidade:
                return True
            else: ("\033[1;31mErro.\033[0;0m Cidade não encontrada. [Enter]")

    def set_qtd_casos_estado(self, qt_deCasos):
        self.__qtd_casos_estado += qt_deCasos

    def get_qtd_casos_estado(self):
        return self.__qtd_casos_estado

    def __str__(self):
        return f"{self.__nome}({self.__sigla}).... {self.__qtd_casos_estado}"


         

