
lst_estado = []

#classe estado -------------------------------------------
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

# classe cidades -----------------------------------------
class Cidade:
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
   
# relatorio cidades -------------------------------------
def relatorio_cidades():
    mostra_estados()
    mostra_cidades()

# mostra cidades ----------------------------------------
def mostra_cidades():
    sigla = input("Informe a UF do Estado: ").upper()
    if verifica_sigla(sigla)== True:
        for estado in lst_estado:
            if estado.get_sigla() == sigla:
                estado.imprime_cidades()
    else: input("\n\033[1;31mErro. UF não encontrada [Enter]\033[0;0m")  

# verifica sigla -------------------------------------------
def verifica_sigla(sigla):
    for estado in lst_estado:
        if estado.get_sigla() == sigla:
            return True
    return False

# cadastrar cidades -------------------------------------
def cadastrar_cidade():
    mostra_estados()
    sigla = input("Informe a UF do Estado: ").upper()
    if verifica_sigla(sigla) == True:
        for estado in lst_estado:
            if estado.get_sigla() == sigla:
                obj_cidade = input("Qual cidade você gostaria de adicionar? ").upper()
                if estado.verifica_cidade(obj_cidade) == True:
                    input("\n\033[1;31mErro.\033[0;0m Cidade já cadastrada. [Enter]")
                else:
                    cidade = Cidade(obj_cidade)
                    estado.set_lista_cidade(cidade)
    else: input("\n\033[1;31mErro.\033[0;0m UF não encontrada [Enter]")

# relatorio estados -------------------------------------
def relatorio_estados():
    mostra_estados()

# mostra estados ----------------------------------------
def mostra_estados():
    if len(lst_estado) == 0:
        print("\nAinda não foram adicionados estados.\n")
    else:
        print("\n","\033[1;36m=-"*6," Relatório de Estados:","=-"*6,"\033[0;0m\n")
        for estado in lst_estado:
            print(f"\033[1;36m-->\033[0;0m {estado.get_estado().ljust(25)}({estado.get_sigla()})\033[1;36m|\033[0;0m Total de Casos: {estado.get_qtd_casos_estado()}")
        print("\n"*2)

# verifica estados -------------------------------------
def verifica_estado(nome_estado):
    for estado in lst_estado:
        if estado.get_estado() == nome_estado:
            return True
    return False
# cadastrar estados -------------------------------------
def cadastrar_estado():
    mostra_estados()
    
    obj_estado = input("Qual estado você gostaria de adicionar? ").upper()
    if verifica_estado(obj_estado) == False:
        sigla = input("Qual a UF deste estado? ").upper()
        if verifica_sigla(sigla) == False:
            estado = Estado(obj_estado, sigla)
            lst_estado.append(estado)
        else: input("\n\033[1;31mErro.\033[0;0m UF já adicionado. [Enter]")
    else: input("\n\033[1;31mErro.\033[0;0m Estado já adicionado na lista de registros. [Enter]")

def atualiza_casos():
    mostra_estados()
    sigla = input("Informe a UF do Estado: ").upper()
    if verifica_sigla(sigla) == True:
        for estado in lst_estado:
            if estado.get_sigla() == sigla:
                estado.imprime_cidades()
                obj_cidade = input("\nQual cidade você gostaria de atualizar os casos? ").upper()
                if estado.verifica_cidade(obj_cidade) == True:
                   for cidade in estado.get_lista_cidade():
                       if cidade.get_cidade() == obj_cidade:
                            
                            while True:
                                casos = input("\nPor favor, insira os números de caso do dia: ")
                                if casos.isdigit():
                                    casos = int(casos)
                                    cidade.set_qtd_casos_cidade(casos)
                                    estado.set_qtd_casos_estado(casos)
                                    break
                                else: 
                                    input("\b\033[1;31mErro.\033[0;0m Insira somente números maiores que 0. [Enter]")
                                    continue
                else: input("\n\033[1;31mErro.\033[0;0m Cidade não encontrada[Enter]")
    else:input("\n\033[1;31mErro.\033[0;0m UF não encontrado[Enter]")
                
# menu ---------------------------------------------------
def menu_principal():
    return input(("\n"*4)+"""\033[1;34m
 ====================================
 ------------------------------------\033[0;0m 
                MENU\033[1;34m
 ------------------------------------\033[0;0m
    0- Finalizar o Programa
    1- Cadastrar Estados
    2- Cadastrar Cidades
    3- Relatório de Estados
    4- Relatório de Cidades
    5- Atualizar números de casos \033[1;34m
 ------------------------------------
 ====================================\033[0;0m
    Escolha: """)

while True:
    teclado = menu_principal()
    if teclado == "0": break
    elif teclado == "1": cadastrar_estado()
    elif teclado == "2": cadastrar_cidade()
    elif teclado == "3": relatorio_estados()
    elif teclado == "4": relatorio_cidades()
    elif teclado == "5": atualiza_casos()

