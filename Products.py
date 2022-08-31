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

            #tratando dados dentro do dicionario
            tipoProduct = None
            for i in listProducts:
                tipo = i["tipo"]
                if tipo == 1:
                    tipoProduct = "Serie"        
                    i.update({"tipo":tipoProduct})                    
                elif tipo == 2:
                    tipoProduct = "Movie"       
                    i.update({"tipo":tipoProduct})
                elif tipo == 3:
                    tipoProduct = "Documentary"       
                    i.update({"tipo":tipoProduct})
                else:
                    tipoProduct = "unknown"       
                    i.update({"tipo":tipoProduct})  
            for i in listProducts:
                if i["canBuy"] == True:
                    i.update({"canBuy": "Available"})
                elif i["canBuy"] == False:
                    i.update({"canBuy": "Unavailable"})
                else:
                    i.update({"canBuy": "unknown"})     
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


