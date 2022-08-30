from Users import *
from functions import *
import json
import os

nome = "mhb"
senha = Users.getUserPassword(nome)
print(senha)
listNickName = Users.getNickName()
print(listNickName)

