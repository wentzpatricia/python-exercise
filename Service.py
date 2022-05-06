from City import City
from State import State
from Color import Color

color = Color()
listState = []

def reportCity():
    showState()
    showCity()

def showCity():
    initials = input("Informe a UF do Estado: ").upper()
    if verifyInitials(initials)== True:
        for state in listState:
            if state.getInitials() == initials:
                state.printCity()
    else: input(f"\n{color.red}Erro.{color.endColor} UF não encontrada [Enter]")  

def verifyInitials(initials):
    for state in listState:
        if state.getInitials() == initials:
            return True
    return False

def registerCity():
    showState()
    initials = input("Informe a UF do estado: ").upper()
    if verifyInitials(initials) == True:
        for state in listState:
            if state.getInitials() == initials:
                objCity = input("Qual cidade você gostaria de adicionar? ").upper()
                if state.verifyCity(objCity) == True:
                    input(f"\n{color.red}Erro.{color.endColor} Cidade já cadastrada. [Enter]")
                else:
                    city = City(objCity)
                    state.setListCity(city)
    else: input(f"\n{color.red}Erro.{color.endColor} UF não encontrada [Enter]")

def reportState():
    showState()

def showState():
    if len(listState) == 0:
        print("\nAinda não foram adicionados estados.\n")
    else:
        print(f"\n {color.cyan}=-=-=-=-=-=-=- Relatório de estados =-=-=-=-=-=-=-{color.endColor}\n")
        for state in listState:
            print(f"{color.cyan}-->{color.endColor} {state.getState().ljust(25)}({state.getInitials()}){color.cyan}|{color.endColor} Total de cases: {state.get_qtd_cases_state()}")
        print("\n"*2)

def verifyState(nameState):
    for state in listState:
        if state.getState() == nameState:
            return True
    return False

def registerState():
    showState()
    
    objState = input("Qual estado você gostaria de adicionar? ").upper()
    if verifyState(objState) == False:
        initials = input("Qual a UF deste state? ").upper()
        if verifyInitials(initials) == False:
            state = State(objState, initials)
            listState.append(state)
        else: input(f"\n{color.red}Erro.{color.endColor} UF já adicionado. [Enter]")
    else: input(f"\n{color.red}Erro.{color.endColor} estado já adicionado na lista de registros. [Enter]")

def updateCases():
    showState()
    initials = input("Informe a UF do estado: ").upper()
    if verifyInitials(initials) == True:
        for state in listState:
            if state.getInitials() == initials:
                state.printCity()()
                objCity = input("\nQual cidade você gostaria de atualizar os casos? ").upper()
                if state.verifyCity(objCity) == True:
                   for city in state.getListCity()():
                       if city.getCity() == objCity:
                            
                            while True:
                                cases = input("\nPor favor, insira os números de caso do dia: ")
                                if cases.isdigit():
                                    cases = int(cases)
                                    city.setQtdCasesState(cases)
                                    state.setQtdCasesState(cases)
                                    break
                                else: 
                                    input(f"\b{color.red}Erro.{color.endColor} Insira somente números maiores que 0. [Enter]")
                                    continue
                else: input(f"\n{color.red}Erro.{color.endColor} Cidade não encontrada[Enter]")
    else:input(f"\n{color.red}Erro.{color.endColor} UF não encontrado[Enter]")     