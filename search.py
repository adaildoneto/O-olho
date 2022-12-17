import thundera
import requests
import json


def busca(name):
  post = thundera.thundera()

  result = []

  # result = db_users
  for k in post:
    if name in str(k['descricao']):
      cpost = ({
        'titulo': k['titulo'],
        'link': k['link'],
        'data': k['data'],
        'hora': k['hora'],
        'site': k['site'],
        'imagem': k['imagem'],
        'descricao': k['descricao']
      })
      result.append(cpost)
  return result


