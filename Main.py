from Menu import menu_principal
from Service import registerCity
from Service import registerState
from Service import reportCity
from Service import reportState
from Service import updateCases

while True:
    teclado = menu_principal()
    if teclado == "0": break
    elif teclado == "1": registerState()
    elif teclado == "2": registerCity()
    elif teclado == "3": reportState()
    elif teclado == "4": reportCity()
    elif teclado == "5": updateCases()