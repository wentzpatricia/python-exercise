from City import City
from Color import Color

color = Color()
class State:
    def __init__(self, nameState, initials):
        self.__name = nameState
        self.__initials = initials
        self.__listCity = []
        self.__qtdCasesState = 0
    
    def getInitials(self):
        return self.__initials

    def getState(self):
        return self.__name

    def getListCity(self):
        return self.__listCity

    def setListCity(self, city):
        self.__listCity.append(city)

    def printCity(self):
        print(f"\n{color.cyan}=-=-=-=-=- Relatório de cidades =-=-=-=-=-=-{color.endColor}")
        for city in self.__listCity:
           print(f"{color.cyan}--->{color.endColor} {city.getCity().ljust(15)}{color.cyan}|{color.endColor} Casos registrados: {city.getQtdCasesCity()}")
           print("")
    def verifyCity(self, nameCity):
        for city in self.__listCity:
            if city.getCity() == name_cidade:
                return True
            else: (f"{color.red}Erro.{color.endColor} Cidade não encontrada. [Enter]")

    def setQtdCasesState(self, qtCases):
        self.__qtdCasesState += qtCases

    def get_qtdCasesState(self):
        return self.__qtdCasesState

    def __str__(self):
        return f"{self.__name}({self.__initials}).... {self.__qtdCasesState}"


         

