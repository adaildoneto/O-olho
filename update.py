from datetime import datetime
import json
import requests
import pytz

def atualiza():

   

   def log():
      posty = open('log.json')
      logi = json.loads(posty.read())
      
      return logi

   
   def thundera():
      posty = open('thundera.json')
      thunder = json.loads(posty.read())
      
      return thunder 

   post = thundera()   

   lista = []

   for i in post:
      obj = i['link']
      lista.append(obj)

   novo = post

   total = []

   sites = ['http://ac24horas.com', 'http://contilnetnoticias.com.br', 'http://correio68.com', 'https://agencia.ac.gov.br', 'https://nahoradanoticia.com.br',
   'http://folhadoacre.com.br', 'http://yaconews.com', 'http://jornalopiniao.net', 'http://3dejulhonoticias.com.br', 'https://noticiadoacre.com.br',
   'http://agazetadoacre.com', 'http://www.acre.com.br', 'http://acreagora.com', 'https://acreinfoco.com', 
   'http://oaltoacre.com', 'http://agazeta.net', 'http://noticiasdahora.com.br',  'http://oacreagora.com', 'https://www.noticiasdafronteira.com.br', 
   'https://www.juruaonline.com.br', 'https://www.juruaemtempo.com.br', 'https://oestadoacre.com', 'https://oseringal.com', 'https://www.vozdonorte.com.br', 
   'https://acreonline.net' , 'https://acriticadoacre.com.br','http://portalquinari.com.br',
   'https://oacre.com.br',]

   jnews = len (sites)

   for i in range (jnews):
      turl = (sites[i] + '/wp-json/wp/v2/posts')
      response = requests.get(turl)

      data = response.text
      
      if response.status_code == 200:  
         print('site ' + turl + ' ok!')
         dados = json.loads(data)
         for j in dados:
            titulo = j['title']['rendered']
            descricao = j['content']['rendered']
            link = j['link']
            side = sites[i]
            
            try:
                img = j['jetpack_featured_media_url']
            except KeyError:
                img = 'Imagem não encontrada'        
            
            try:
               cdata = j['date']
               cdata1 = cdata[0:10]
               chora = cdata[11:20]
            except KeyError:
               cdata = 0

            #estruturando o conteudo dentro da celula
            cpost = ({'titulo':titulo,'link': link,'data' : cdata1, 'hora' : chora, 'site' : side,'imagem' : img, 'descricao': descricao})

                  
            
            if (link not in lista):
               novo.append (cpost)
               total.append (cpost)
            
      else:
         print('site ' + turl + ' não habilitado para o json')

   filename = 'thundera.json'
   with open(filename, 'w') as json_file:
      json.dump(novo, json_file, 
                           indent=4,  
                           separators=(',',': '))

   resulta = []
   log1 = log()
   result = len(total)
   
   chora = datetime.now(pytz.timezone('America/Rio_Branco'))
   
   resulta = ({'update': chora ,
               'materias': result
               })
   log1.append(resulta)

   filename2 = 'log.json'
   with open(filename2, 'w') as json_file:
      json.dump(log1, json_file,indent=4, sort_keys=True, default=str)
     
   return result