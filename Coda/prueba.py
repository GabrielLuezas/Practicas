from codaio import Coda, Document, Cell, Row 
import pandas as pd

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('05ZbXhV8oe', coda=coda)
table = doc.get_table("Prueba")


row1  = table['i-fwUeBU2Jt6']
row2  = table['i-TVvykQKaN5']
print(table)
print(row1)

#Mediante panda, convierte la tabla en un objeto manipulable facilmente por panda, exporta la tabla a csv y a excell y luego lo muestra en pantalla
df = pd.DataFrame(table.to_dict())
df.to_csv('PruebaCSV.csv')
df.to_excel('PruebaExcell.xlsx')
print(df)
print(df.head)

#Conseguir el valor de una celda de una fila y columna concretas 
cell = table['i-kzGS5eVqkW']['c-mmnRbjpiHh']
print(cell)

#Instertar varias filas a una tabla
#celda1 = Cell(column='c-ZW-9sVXOvL', value_storage='Manolo')
#celda2 = Cell(column='c--pJGgINgeR', value_storage='Bros')
#celda3 = Cell(column='c-T3dMGwCtv3', value_storage='26')
#celda4 = Cell(column='c-mmnRbjpiHh', value_storage='Arandanos')
#celda1_2 = Cell(column='c-ZW-9sVXOvL', value_storage='Mario')
#celda2_2 = Cell(column='c--pJGgINgeR', value_storage='Ruiz')
#celda3_2 = Cell(column='c-T3dMGwCtv3', value_storage='32')
#celda4_2 = Cell(column='c-mmnRbjpiHh', value_storage='Manzana')
#table.upsert_rows([[celda1, celda2, celda3, celda4], [celda1_2, celda2_2, celda3_2, celda4_2]])
#print("Las filas han sido añadidas con exito")

#Actualizar una fila de una tabla
celda1 = Cell(column='c-ZW-9sVXOvL', value_storage='Prueba')
celda2 = Cell(column='c--pJGgINgeR', value_storage='Prueba')
celda3 = Cell(column='c-T3dMGwCtv3', value_storage='49')
celda4 = Cell(column='c-mmnRbjpiHh', value_storage='Piña')
celda1_2 = Cell(column='c-ZW-9sVXOvL', value_storage='Mario')
celda2_2 = Cell(column='c--pJGgINgeR', value_storage='Ruiz')
celda3_2 = Cell(column='c-T3dMGwCtv3', value_storage='32')
celda4_2 = Cell(column='c-mmnRbjpiHh', value_storage='Manzana')
table.update_row(row1, [celda1, celda2, celda3, celda4])



