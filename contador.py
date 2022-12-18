import numpy as N
import thundera
import collections

def countsite():
    post = thundera.thunder()
    nsite = [post['site'] for post in post ]
    res = N.array(nsite) 
    unique_res = N.unique(res) 

    repetidos = collections.Counter(nsite)

    site_counter = []

    for j in unique_res:
        csite = ({'label': str(j), 'valor': str(repetidos[j])})
        site_counter.append(csite)
    return site_counter

def countdata():
    post = thundera.thunder()
    nsite = [post['data'] for post in post ]
    res = N.array(nsite) 
    unique_res = N.unique(res) 

    repetidos = collections.Counter(nsite)

    data_counter = []

    for j in unique_res:
        csite = ({'label': str(j), 'valor': str(repetidos[j])})
        data_counter.append(csite)
    return data_counter


  
   



