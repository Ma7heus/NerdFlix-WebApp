from Users import *
from Products import *
from functions import *
import json
import os

a = Products.getAllProducts("value")
tipoProduct = None

for i in a:
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
print(a)