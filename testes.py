from Users import *
from Products import *
from functions import *
import json
import os

a = Products.getAllProducts("value")

for i in a:
    print(i["nome"])
