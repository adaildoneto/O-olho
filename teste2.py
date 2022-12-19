import thundera
import numpy as N
import re
import collections

def countword():
    post = thundera.thunder()
    nsite = [post['titulo'] for post in post ]
    res = " ".join(str(s) for s in nsite)
    res = re.findall(r"[\w']+", res)
    tres = N.unique(res)
    fat = ['quase ','R','Um','Uns','Uma','Umas','um','em','por','uns','uma','umas','O','o','A','a','ante', 'até', 'após', 'com', 'contra', 'de', 'desde', 'em', 'entre', 'para','perante','por','sem','sobre','trás']
    proc = tres
    result = [ p for p in proc if p not in fat ]

    repetidos = collections.Counter(res)
    data_counter = []

    for j in result:
        csite = ({'label': str(j), 'valor': str(repetidos[j])})
        if repetidos[j] > 25: 
            if len(j) > 4:
                data_counter.append(csite)

    return data_counter

countword()