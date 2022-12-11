import random, string
from flask import Flask, render_template
import json
import pandas as pd
import subprocess
from flask import Blueprint
from flask_paginate import Pagination, get_page_args, get_page_parameter



app = Flask(  # Create a flask app
  __name__,
  template_folder='templates',  # Name of html file folder
  static_folder='static'  # Name of directory for static files
)

posty = open('thunder-ordenado.json')
thunder = json.loads(posty.read())

count = thunder['Titulo']
p = len(count)
p = int(p)
users = list(range(p))

def page_href(self, page):
    if self.href:
        page = 1 if page is None else page
        url = self.href.format(page)
    else:
        url = url_for(self.endpoint, page=page, **self.args)

    # Need to return a unicode object
    return url.decode('utf8') if PY2 else url

def get_users(offset=0,per_page=50):
    return users[offset: offset+per_page]

@app.route('/')  # What happens when the user visits the site

def base_page():

  posty = open('thunder-ordenado.json')
  thunder = json.loads(posty.read())

  titulo = thunder['Titulo']
  data = thunder['Data']
  site = thunder['site']
  Img = thunder['Imagem']
  link = thunder['Url']
  hora = thunder['Hora']

  post = []

  for k in titulo:
    cpost = ((titulo[k], link[k], data[k], hora[k], site[k], Img[k]))
    post.append(cpost)
  page = 1
  per_page = 50

  offset = (page - 1) * per_page

  
  users = titulo
  total = len(users)

  pagination_users = get_users(offset=offset,per_page=per_page)



  pagination = Pagination(page=page, total=total,
                            css_framework='bootstrap4',
                            search=False, record_name='bookmarks',
                            per_page=per_page)

        
  return render_template(
    'base.html',  # Template file path, starting from the templates folder. 
    post=post,
    users=pagination_users,
    page=page,
    per_page=per_page,
    pagination=pagination,
    
  )


@app.route('/starting')
def run_script():
  with open('update.py', mode='r', encoding='utf-8') as update:
    code = update.read()

  return exec(code)


if __name__ == "__main__":  # Makes sure this is the main process
  app.run(  # Starts the site
    host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
    port=8080,  # Randomly select the port the machine hosts on.
    debug= True,  #
  )
