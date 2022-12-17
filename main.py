from flask import Flask, render_template
from flask import request
import update
import thundera
import search

app = Flask(  # Create a flask app
  __name__,
  template_folder='templates',  # Name of html file folder
  static_folder='static'  # Name of directory for static files
)

@app.route('/')  # What happens when the user visits the site
def base_page():
  post = thundera.thunder()
  pdate = thundera.pdate()

  return render_template(
    'base.html',  # Template file path, starting from the templates folder. 
    post=post,
    total=len(post),
    materia=pdate['materias'],
    hora=pdate['update'])


@app.route('/starting')
def dynamic_page():
  result = update.atualiza()
  post = thundera.thunder()
  return render_template(
    'base3.html',  # Template file path, starting from the templates folder. 
    post=post,
    result=result)


@app.route('/log')
def log_json():
  list = thundera.log()

  return list


@app.route('/json')
def test_json():
  list = thundera.thunder()

  return list


@app.route('/busca')
def busca():

  return render_template('busca.html')

@app.route('/abusca')
def buscaad():

  return render_template('abusca.html')


@app.route('/search', methods=['GET'])
def pesquisa():
  
  name = request.args.get('name')
  
  result = search.busca(name=name)
  
  pdate = thundera.pdate()

  return render_template('base.html',
                         post=result,
                         total=len(result),
                         materia=pdate['materias'],
                         hora=pdate['update']
                         )


@app.route('/asearch', methods=['GET'])
def apesquisa():
  
  name = request.args.get('name')
  
  result = search.abusca(aname=name)
  
  pdate = thundera.pdate()

  return render_template('base.html',
                         post=result,
                         total=len(result),
                         materia=pdate['materias'],
                         hora=pdate['update']
                         )

if __name__ == "__main__":  # Makes sure this is the main process
  app.run(  # Starts the site
    host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
    port=8080,  # Randomly select the port the machine hosts on.
    debug=True,  #
  )
