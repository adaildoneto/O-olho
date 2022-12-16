import json

def thundera():
    posty = open('thundera.json')
    thunder = json.loads(posty.read())
    
    return thunder 

post = thundera()   

lista = []

for i in post:
    obj = i['link']
    lista.append(obj)

print (lista)