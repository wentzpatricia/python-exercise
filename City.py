class City:
    def __init__(self, nameCity):
        self.__city = nameCity
        self.__qtdCasesCity = 0

    def getCity(self):
        return self.__city

    def setQtdCasesCity(self, qtCity):
        self.__qtdCasesCity += qtCity
    
    def getQtdCasesCity(self):
        return self.__qtdCasesCity

    def __str__(self):
        return f"{self.getCity()()}|{self.__city} {self.__qtdCasesCity}"