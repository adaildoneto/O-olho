from flask import Flask, render_template
import json
from flask import request
import jsonify as jsonify
import update




app = Flask(  # Create a flask app
  __name__,
  template_folder='templates',  # Name of html file folder
  static_folder='static'  # Name of directory for static files
)



    #criando api da thundera

def thunder():
    posty = open('thundera.json')
    thunder = json.loads(posty.read())
    return thunder

def log():
    posty = open('log.json')
    logi = json.loads(posty.read())
      
    return logi

pdate = []
log1 = log()
pdate = log1[-1]

@app.route('/')  # What happens when the user visits the site

def base_page():
  
  post = thunder()
  
        
  return render_template(
    'base.html',  # Template file path, starting from the templates folder. 
     post=post,
     total = len(post),
     materia = pdate['materias'],
     hora = pdate['update']
  )


@app.route('/starting')
def dynamic_page():
    result = update.atualiza()

    return render_template(
    'base3.html',  # Template file path, starting from the templates folder. 
     post=thunder(),
     result = result
     
  )

@app.route('/json')
def test_json():
    list = thunder()
    
    return list 


@app.route('/search', methods=['GET'])
def search():
    
    name = request.args.get('name')
    
    post = thunder()

    result = []


    # result = db_users
    for k in post:
      if name in str(k['descricao']):
          cpost = ({'titulo':k['titulo'],'link': k['link'],'data' : k['data'], 'hora' : k['hora'], 'site' : k['site'],'imagem' : k['imagem'], 'descricao': k['descricao']})
          result.append(cpost)
    

    return render_template( 'base.html', post = result, total = len(result), materia = pdate['materias'], hora = pdate['update'] )    

 
if __name__ == "__main__":  # Makes sure this is the main process
  app.run(  # Starts the site
    host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
    port=8080,  # Randomly select the port the machine hosts on.
    debug= True,  #
  )
