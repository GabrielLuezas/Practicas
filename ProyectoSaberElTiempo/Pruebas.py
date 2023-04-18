import pandas as pd
from codaio import Coda, Document, Cell, Row 
import requests

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('05ZbXhV8oe', coda=coda)
table = doc.get_table("Temperaturas Completar")

df = pd.DataFrame(table.to_dict())
ultimafila=(df.head(1))
ciudad=ultimafila.loc[ultimafila.index[0], 'Ciudad']

#Conseguir la columna Ciudad
df2 = pd.DataFrame(table.to_dict())
ciudades= df2["Ciudad"].values.tolist()
print (ciudades)
print (ciudad)

if ciudad in ciudades:
    print("La ciudad introducida ya esta en ciudades")
else:
    print("La ciudad introducida no esta en ciudades")