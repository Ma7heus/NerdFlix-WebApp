<<<<<<< HEAD
from functions import *
=======
>>>>>>> 16a9bbb3cb1711c3af44da74c8647fb986779ad4
class Users:
    def __init__(self, name, nickName, password):
        self.name = name
        self.password = password
        self.nickName = nickName

<<<<<<< HEAD
    def getUser(tipo):
        dados = getData("users")
        if tipo == "value":
            listUsers = list(dados.values())
        elif tipo == "key":
            listUsers = list(dados.keys())
        return listUsers

    def getName():
        userValues = Users.getUser("value")
        listName = []
        for i in userValues:
            name = i['name']
            listName.append(name)
        return listName

    def getNickName():
        userValues = Users.getUser("value")
        listNickName = []
        for i in userValues:
            nickName = i['nickName']
            listNickName.append(nickName)
        return listNickName

    def getPassword():
        userValues = Users.getUser("value")
        listPassword = []
        for i in userValues:
            password = i['password']
            listPassword.append(password)
        return listPassword

    def getUserPassword(nameUser):
        listPassword = Users.getPassword()
        listUsers = Users.getNickName()
        indice = 0
        userPassword = None
        for i in listUsers:
            if i == nameUser:
                break
            indice +=1
        userPassword = listPassword[indice]

        return userPassword

=======
>>>>>>> 16a9bbb3cb1711c3af44da74c8647fb986779ad4
