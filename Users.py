from functions import *
class Users:
    def __init__(self, name, nickName, password):
        self.name = name
        self.password = password
        self.nickName = nickName

def getUser(tipo):
    dados = getData("users")
    if tipo == "value":
        listUsers = list(dados.values())
    elif tipo == "key":
        listUsers = list(dados.keys())
    return listUsers



