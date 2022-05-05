from Menu import menu_principal
from exercise import cadastrar_cidade
from exercise import cadastrar_estado
from exercise import relatorio_estados
from exercise import relatorio_cidades
from exercise import atualiza_casos

while True:
    teclado = menu_principal()
    if teclado == "0": break
    elif teclado == "1": cadastrar_estado()
    elif teclado == "2": cadastrar_cidade()
    elif teclado == "3": relatorio_estados()
    elif teclado == "4": relatorio_cidades()
    elif teclado == "5": atualiza_casos()