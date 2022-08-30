from functions import *
class Products:
    def __init__(self, code, name, value, type, canBuy):
        self.code = code
        self.name = name
        self.value = value
        self.type = ptype
        self.canBuy = canBuy
    
    
    def getAllProducts(tipo):
        dados = getData("products")
        if tipo == "value":
            listProducts = list(dados.values())
        elif tipo == "key":
            listProducts = list(dados.keys())
        return listProducts



    def getProduct():
        return
    def getMovies():
        return
    def getSeries():
        return
    def getDocumentary():
        return


