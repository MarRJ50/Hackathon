import os
import requests

x = requests.get("http://10.20.131.251:5000/validation")
valor = x.json()
print(valor[u"value"])

