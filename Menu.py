from Color import Color
color = Color()

def menu_principal():
    return input(("\n"*4)+f"""{color.magenta}
 ====================================
 ------------------------------------{color.endColor} 
                MENU{color.magenta}
 ------------------------------------{color.endColor}
    0- Finalizar o Programa
    1- Cadastrar Estados
    2- Cadastrar Cidades
    3- Relatório de Estados
    4- Relatório de Cidades
    5- Atualizar números de casos {color.magenta}
 ------------------------------------
 ===================================={color.endColor}
    Escolha: """)