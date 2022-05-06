from City import City
from State import State
from Color import Color

color = Color()
lst_estado = []

def relatorio_cidades():
    mostra_estados()
    mostra_cidades()

def mostra_cidades():
    sigla = input("Informe a UF do Estado: ").upper()
    if verifica_sigla(sigla)== True:
        for estado in lst_estado:
            if estado.get_sigla() == sigla:
                estado.imprime_cidades()
    else: input(f"\n{color.red}Erro.{color.endColor} UF não encontrada [Enter]")  

def verifica_sigla(sigla):
    for estado in lst_estado:
        if estado.get_sigla() == sigla:
            return True
    return False

def cadastrar_cidade():
    mostra_estados()
    sigla = input("Informe a UF do Estado: ").upper()
    if verifica_sigla(sigla) == True:
        for estado in lst_estado:
            if estado.get_sigla() == sigla:
                obj_cidade = input("Qual cidade você gostaria de adicionar? ").upper()
                if estado.verifica_cidade(obj_cidade) == True:
                    input(f"\n{color.red}Erro.{color.endColor} Cidade já cadastrada. [Enter]")
                else:
                    cidade = City(obj_cidade)
                    estado.set_lista_cidade(cidade)
    else: input(f"\n{color.red}Erro.{color.endColor} UF não encontrada [Enter]")

def relatorio_estados():
    mostra_estados()

def mostra_estados():
    if len(lst_estado) == 0:
        print("\nAinda não foram adicionados estados.\n")
    else:
        print(f"\n {color.cyan}=-=-=-=-=-=-=- Relatório de Estados =-=-=-=-=-=-=-{color.endColor}\n")
        for estado in lst_estado:
            print(f"{color.cyan}-->{color.endColor} {estado.get_estado().ljust(25)}({estado.get_sigla()}){color.cyan}|{color.endColor} Total de Casos: {estado.get_qtd_casos_estado()}")
        print("\n"*2)

def verifica_estado(nome_estado):
    for estado in lst_estado:
        if estado.get_estado() == nome_estado:
            return True
    return False

def cadastrar_estado():
    mostra_estados()
    
    obj_estado = input("Qual estado você gostaria de adicionar? ").upper()
    if verifica_estado(obj_estado) == False:
        sigla = input("Qual a UF deste estado? ").upper()
        if verifica_sigla(sigla) == False:
            estado = State(obj_estado, sigla)
            lst_estado.append(estado)
        else: input(f"\n{color.red}Erro.{color.endColor} UF já adicionado. [Enter]")
    else: input(f"\n{color.red}Erro.{color.endColor} Estado já adicionado na lista de registros. [Enter]")

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
                                    input(f"\b{color.red}Erro.{color.endColor} Insira somente números maiores que 0. [Enter]")
                                    continue
                else: input(f"\n{color.red}Erro.{color.endColor} Cidade não encontrada[Enter]")
    else:input(f"\n{color.red}Erro.{color.endColor} UF não encontrado[Enter]")     