import json


def thundera():
    posty = open('thundera.json')
    thunder = json.loads(posty.read())

    titulo = thunder['Titulo']
    data = thunder['Data']
    site = thunder['site']
    Img = thunder['Imagem']
    link = thunder['Url']
    hora = thunder['Hora']
    

    postson = []

    for k in titulo:
        cpost = ({'titulo':titulo[k],'link': link[k],'data' : data[k], 'hora' : hora[k], 'site' : site[k],'imagem' : Img[k]})
        postson.append(cpost)
        
    return postson

novo = thundera()

jsonString = json.dumps(novo)
jsonFile = open("thundera.json", "w")
jsonFile.write(jsonString)
jsonFile.close()