from Users import *
import json

# function that get dara on database files
def getData(arquivo):
    dataType = "" 
    if arquivo == "users":
        dataType = "dataBase/users.json"
    elif arquivo == "products":
        dataType = "dataBase/products.json"
    elif arquivo == "clients":
        dataType = "dataBase/clients.json"
    else:
        print("nome de arquivo nao existe")
    
    with open(dataType, "r", encoding="utf-8") as DB:
        dados = json.load(DB)
        DB.close()
    return dados




