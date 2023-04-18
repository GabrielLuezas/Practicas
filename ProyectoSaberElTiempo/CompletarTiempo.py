import requests
from codaio import Coda, Document, Cell

token= "c5149980-deb1-4979-952f-f3d49ec5b038"
tabla="grid-MArENxYZlC"
url= f"https://coda.io/apis/v1beta1/docs/tables/{tabla}"
def check_for_new_row():
     response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
     rows_before = len(response.json()["items"][0]["rows"])
     response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
     rows_after = len(response.json()["items"][0]["rows"])
     if rows_after > rows_before:
            print("Se ha añadido una fila nueva.")
     else:
        print("No se ha añadido ninguna fila nueva.")  
       
      
    