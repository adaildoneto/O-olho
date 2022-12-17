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


def abusca(aname):
    sites = ['http://ac24horas.com', 'http://contilnetnoticias.com.br', 'http://correio68.com', 'https://agencia.ac.gov.br', 'https://nahoradanoticia.com.br',
    'http://folhadoacre.com.br', 'http://yaconews.com', 'http://jornalopiniao.net', 'http://3dejulhonoticias.com.br', 'https://noticiadoacre.com.br',
    'http://agazetadoacre.com', 'http://www.acre.com.br', 'http://acreagora.com', 'https://acreinfoco.com', 
    'http://oaltoacre.com', 'http://agazeta.net', 'http://noticiasdahora.com.br',  'http://oacreagora.com', 'https://www.noticiasdafronteira.com.br', 
    'https://www.juruaonline.com.br', 'https://www.juruaemtempo.com.br', 'https://oestadoacre.com', 'https://oseringal.com', 'https://www.vozdonorte.com.br', 
    'https://acreonline.net' , 'https://acriticadoacre.com.br','http://portalquinari.com.br',
    'https://oacre.com.br',]

    jnews = len (sites)

    for i in range (jnews):
        turl = (sites[i] + '/wp-json/wp/v2/search/?subtype=post&search=' + aname)
        response = requests.get(turl)

        data = response.text
        
        if response.status_code == 200:  
            print('site ' + turl + ' ok!')
            dados = json.loads(data)
            for j in dados:
                titulo = j['title']
                link = j['url']
                side = sites[i]
                id_ = str(j['id'])
                
                pturl = (sites[i] + '/wp-json/wp/v2/posts/' + id_)
                response = requests.get(pturl)
                datas = response.text
                k = json.loads(datas)
                try:
                    cdata = k['date']
                    cdata1 = cdata[0:10]
                    chora = cdata[11:20]
                except KeyError:
                    cdata = 0
                
                try:
                    img = k['jetpack_featured_media_url']
                except KeyError:
                    turl = (sites[i] + '/wp-json/wp/v2/media/' + id_)
                    response = requests.get(turl)
                    if response.status_code == 200:
                        imagem = response.text
                        i_json = json.loads(imagem)
                        img = i_json['yoast_head_json']['og_image']['url']
                    else:
                        img = 'Não encontrado'
                
                
            #estruturando o conteudo dentro da celula
            resultado = []
            pdata = ({'titulo':titulo,'link': link,'data' : cdata1, 'hora' : chora, 'site' : side,'imagem' : img})
            resultado.append(pdata) 

        else:
         print('site ' + turl + ' não habilitado para o json')

    return resultado