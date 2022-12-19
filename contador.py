import numpy as N
import thundera
import collections
import re

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

def contarpalavra():
    post = thundera.thunder()
    nsite = [post['titulo'].lower() for post in post ]
    res = " ".join(str(s) for s in nsite)
    res = re.findall(r"[\w']+", res)
    tres = N.unique(res)
    fat = ['quase ','R','Um','Uns','Uma','Umas','um','em','por','uns','uma','umas','O','o','A','a','ante', 'até', 'após', 'com', 'contra', 'de', 'desde', 'em', 'entre', 'para','perante','por','sem','sobre','trás']
    proc = tres
    result = [ p for p in proc if p not in fat ]

    repetidos = collections.Counter(res)
    data_counter = []

    for j in result:
        csite = ({'x': str(j), 'value': str(repetidos[j])})
        if repetidos[j] > 25: 
            if len(j) > 2:
                data_counter.append(csite)

    return data_counter