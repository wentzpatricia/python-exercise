from City import City
from State import State

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
    else: input("\n\033[1;31mErro. UF não encontrada [Enter]\033[0;0m")  

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
                    input("\n\033[1;31mErro.\033[0;0m Cidade já cadastrada. [Enter]")
                else:
                    cidade = Cidade(obj_cidade)
                    estado.set_lista_cidade(cidade)
    else: input("\n\033[1;31mErro.\033[0;0m UF não encontrada [Enter]")

def relatorio_estados():
    mostra_estados()

def mostra_estados():
    if len(lst_estado) == 0:
        print("\nAinda não foram adicionados estados.\n")
    else:
        print("\n","\033[1;36m=-"*6," Relatório de Estados:","=-"*6,"\033[0;0m\n")
        for estado in lst_estado:
            print(f"\033[1;36m-->\033[0;0m {estado.get_estado().ljust(25)}({estado.get_sigla()})\033[1;36m|\033[0;0m Total de Casos: {estado.get_qtd_casos_estado()}")
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