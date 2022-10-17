---
title: Datos del INE
subtitle: Indices precio vivienda
category: Ejemplos
layout: default
---

<table class="doc">
    <tr>
        <td>
        Importamos las cabeceras, solo están disponibles unos pocos paquetes ya que la misión principal es recuperar y transformar datos, y generalmente esto lo hago usando pandas, las últimas líneas son necesarias para importar una biblioteca con los paths, los notebooks los uso desde visual studio (conectado a un servidor ipython remoto), o directamente en jupyter en el servidor remoto y por último los tiene que procesar github en el workflow, en su docker
        </td>
        <td>
{% highlight python %}
%load_ext autoreload
%autoreload 2
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import requests

cwd = Path.cwd()
home = Path.home()
module_path = f"{home}/serhi/src/lib" if cwd == home else f"{cwd.parents[1]}/lib"
sys.path.append(module_path)
import serhi
{% endhighlight %}
        </td>
    </tr>
    <tr>
        <td>En esta celda pondremos e nombre de la entidad y el nombre del notebook sin extensión</td>
        <td>
{% highlight python %}
# inicio
# cambiar como corresponda
ENTITY = 'ine'
NB_NAME = 'ine_indices'
{% endhighlight %}
        </td>
    </tr>
    <tr>
        <td>
        Con esta línea inicializamos la biblioteca de serhi, que establece las rutas donde deben gardarse los archivos 
        </td>
        <td>
{% highlight python %}
serhi.init(ENTITY, NB_NAME, Path.cwd().parents[0])
{% endhighlight %}
        </td>
    </tr>
    <tr>
        <td>la salida de la celda anterior en un entorno local será algo como esto, una recopilación de las diferentes rutas</td>
        <td>
            {% highlight bash %}
SerHi Tools
dir /home/node/serhi/src/entidades
serhi.CWD /home/node/serhi/src/entidades/ine
serhi.BASE_PATH ../../..
serhi.DATA_PATH ../../../data/process/ine/
serhi.DOWN_PATH ../../../tmp/download/ine/
serhi.OUT_FILE ../../../data/process/ine/ine_indices.csv
            {% endhighlight %}
        </td>
    </tr>
    <tr>
        <td>descargamos datos del instituto nacional de estadistica, los indices del precio de la vivienda, la rura donde se guardará el archivo <code>sergi.DOWN_PATH</code></td>
        <td>
            {% highlight python %}
def download_files(urls):
for loc in urls:
    url = loc['url']
    r = requests.get(url, allow_redirects=True)
    print(f'Downloading {url}')
    open(serhi.DOWN_PATH +  loc['file'], 'wb').write(r.content)

urls = [    
    {
    # indices precios vivienda
    'url':'https://www.ine.es/jaxiT3/files/t/es/xlsx/25171.xlsx?nocab=1',
    'file':'ine_ipv.xlsx'
    },
]

download_files(urls)    
            {% endhighlight %}
        </td>
    </tr>
    <tr>
        <td>leemos el archivo descargado</td>
        <td>
            {% highlight python %}
df = pd.DataFrame()
loc = urls[0]
file = loc['file']
df = pd.read_excel(serhi.DOWN_PATH + file, skiprows=7, nrows=76)            
            {% endhighlight %}
        </td>
    </tr>
    <tr>
        <td>vemos lo que tenemos</td>
        <td>
            {% highlight bash %}
                        2022T2	2022T1	2021T4	2021T3	2021T2	2021T1	
0	    Nacional	    NaN	    NaN	    NaN	    NaN	    NaN	    NaN
1	    General	        141.433	138.742	135.291	133.652	130.937	127.831	
2	    Vivienda nueva	153.51	153.365	148.64	145.073	141.088	106.098
3	    Vivienda segun.	139.707	136.511	133.292	132.009	105.803 104.067
4	    01 Andalucía	NaN	    NaN	    NaN	    NaN	    NaN	    NaN	    
5       rows × 24 columns         
            {% endhighlight %}
        </td>
    </tr>
    <tr>
        <td>desc</td>
        <td>
            {% highlight python %}
            {% endhighlight %}
        </td>
    </tr>
    <!-- template -->
    <tr>
        <td>desc</td>
        <td>
            {% highlight python %}
            {% endhighlight %}
        </td>
    </tr>
</table>