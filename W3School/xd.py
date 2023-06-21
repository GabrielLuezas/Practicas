import ssl
from codaio import Coda
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import time
from datetime import datetime, date, time, timedelta


limite = date.today() - timedelta(days = 1)
# Obtener rows de una tabla: ejemplo: https://coda.io/apis/v1beta1/docs/G6ody-h41g/Tables/grid-LOFVqGm0t5/rows
### La tabla en la que quiero insertar las noticias es:
# https://coda.io/apis/v1beta1/docs/G6ody-h41g/Tables/grid-30lv9fOPY1/rows
# DocId: G6ody-h41g
# TableId: grid-30lv9fOPY1


# SACAR URL DE FEEDLY.XML COMO FUENTES

infile = open('feedly.xml', 'r')
contents = infile.read()
soup = BeautifulSoup(contents, 'xml')
urlaux = soup.find_all('outline')
listaulr = []
for i in range(0,len(urlaux)) :
    if (len(urlaux[i]) == 0) :
        urlseg = str(urlaux[i]).split("xmlUrl=")
        listaulr.append(urlseg[1].replace("/>",""))

#for i in listaulr: 
#    print(i)


# ESTE SCRIPT RECOGE LAS NOTICIAS DE FEEDLY Y LAS RECOGE EN CODA
API_KEY = 'c5d228f1-a38e-4956-b6e6-f6ceaac089d0'
#rss = 'https://www.incibe-cert.es/feed/avisos-sci/all'
b = float('0.0')
lenlista = len(listaulr)
for rss in listaulr :
    print((b/lenlista)*100)
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    d = feedparser.parse(rss.replace('"','')) #<<WORKS!!
    if (len(d.entries) > 10) :
        ent = 10
    else:
        ent = len(d.entries)
    coda = Coda('c5d228f1-a38e-4956-b6e6-f6ceaac089d0')
    for i in range(0,int(ent)) :
        try : 
            publicada = d.entries[i].published_parsed
            publicadodate = date (publicada.tm_year, publicada.tm_mon,publicada.tm_mday)
            if ( publicadodate > limite) : 
                #print(d.entries[i].title)
                #print(d.entries[i].description)
                #print(d.entries[i].link)
                #print('--------------------------------------------------------------')
                payload = {
                  'rows': [
                    {
                      'cells': [
                        {'column': 'c-_zKlSZgEHp', 'value': d.entries[i].title}, {'column': 'c-FaaJIgjDAb', 'value': d.entries[i].link}, {'column': 'c-w6-NqTjAXr', 'value': publicadodate.strftime("%m/%d/%Y")}
                      ],
                    },
                  ],
                }
                coda.upsert_row('G6ody-h41g','grid-30lv9fOPY1',payload)
        except :
            pass
    b = b+1