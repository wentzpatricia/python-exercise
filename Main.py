from Menu import menu_principal
from Service import cadastrar_cidade
from Service import cadastrar_estado
from Service import relatorio_estados
from Service import relatorio_cidades
from Service import atualiza_casos

while True:
    teclado = menu_principal()
    if teclado == "0": break
    elif teclado == "1": cadastrar_estado()
    elif teclado == "2": cadastrar_cidade()
    elif teclado == "3": relatorio_estados()
    elif teclado == "4": relatorio_cidades()
    elif teclado == "5": atualiza_casos()