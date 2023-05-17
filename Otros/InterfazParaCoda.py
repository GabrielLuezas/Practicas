from tkinter import *
from tkinter import ttk, messagebox
from codaio import Coda, Document, Cell, Row 
import pandas as pd

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('NOBRSEzMeJ', coda=coda)
table = doc.get_table("TKINTER")

def buscar_en_coda():
    valor_busqueda = entrada_buscar.get()
    df = pd.DataFrame(table.to_dict())
    resultados = df.loc[df.apply(lambda x: x.astype(str).str.contains(valor_busqueda, case=False).any(), axis=1)]
    if resultados.empty:
        resultados_texto = "No se encontraron resultados"
    else:
        resultados_texto = resultados.to_markdown(index=False)
    for widget in ventana.grid_slaves():
        if int(widget.grid_info()["row"]) == 6:
            widget.grid_forget()
    resultadofinal = Text(ventana, height=len(resultados_texto.split('\n')), width=45, wrap=NONE)
    resultadofinal.grid(row= 6, column=4)
    resultadofinal.insert(END, resultados_texto)
    resultadofinal.tag_configure('center', justify='center')
    resultadofinal.tag_add('center', '1.0', 'end')

def importar_a_coda():
    texto=entrada.get()
    texto2=entrada2.get()
    texto3=entrada3.get()
    celda1 = Cell(column='c-YDV8L12Kq8', value_storage= texto)
    celda2 = Cell(column='c-gITD98c54X', value_storage= texto2)
    celda3 = Cell(column='c-4E1QFCVR3A', value_storage= texto3)
    try:
        table.upsert_rows([[celda1, celda2, celda3]])
        messagebox.showinfo("Éxito", "Los datos han sido importados correctamente")
    except:
        messagebox.showerror("Error", "La importación ha fallado, por favor inténtelo de nuevo")

ventana = Tk()
ventana.geometry("1000x200")
ventana.title("Interfaz para añadir valores a coda")
etiqueta = ttk.Label(text="Fruta Favorita")
etiqueta.grid(row=0, column=0)
etiqueta2 = ttk.Label(text="Nombre")
etiqueta2.grid(row=0, column=1)
etiqueta3 = ttk.Label(text="Apellidos")
etiqueta3.grid(row=0, column=2)
entrada = Entry(ventana, width=20)
entrada.grid(row=1, column=0)
entrada2 = Entry(ventana, width=20)
entrada2.grid(row=1, column=1)
entrada3 = Entry(ventana, width=20)
entrada3.grid(row=1, column=2)
boton_txt = Button(ventana, text="Importar a Coda", command=importar_a_coda)
boton_txt.grid(row=1, column=3)
espacio = ttk.Label(text=" ")
espacio.grid(row=3, column=0)
espacio2 = ttk.Label(text=" ")
espacio2.grid(row=4, column=0)
entrada_buscar = Entry(ventana, width=20)
entrada_buscar.grid(row=5, column=2)
boton_buscar = Button(ventana, text="Buscar", command=buscar_en_coda)
boton_buscar.grid(row=5, column=3)
tabla_marco = ttk.Frame(ventana)
tabla_marco.grid(row=6, column=0, sticky="nsew")
ventana.mainloop()
