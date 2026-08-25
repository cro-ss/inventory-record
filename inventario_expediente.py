# Escribe tu código aquí :-)
from pathlib import Path
root =  Path(r'C:\Users\chris\OneDrive\Desktop\Crostian Asus\Ing_Bermeo_C\CLAUDE_CODE\GAD_TARQUI_2026')
print(root.exists())

contador = 0
for elemento in root.rglob('*'):
    print(elemento)
    #print(elemento.stat().st_size)
    contador = contador+1
print('Elementos en el expediente', contador)
#### Parte 2 pesar cada uno de los documentos.
#---------- probamos primero el elemento tipo stat
#-------------------------------------------------------------
# Vamos a pesar cada archivo(file), carpetas se pesan distinto.
file_counter = 0
directory_counter=0
total_weight = 0
for elemento in root.rglob('*'):
    if elemento.is_file() == True:
        file_counter = file_counter + 1
        in_weight = elemento.stat().st_size
        total_weight += in_weight
    else:
        directory_counter += 1
print(f'El número de archivos es {file_counter}')
print(f'El número de carpetas es {directory_counter}')
print(f'La comprobación es {directory_counter + file_counter }')
print(f'El peso de los archivos es {round((total_weight/1024)/1024,2) } MB')
print(f'El peso de los archivos es {round(((total_weight/1024)/1024)/1000,2) } GB')


###### Vamos a generar comando en este script de python.
###### Lo que buscamos aqui es presentar los resultados de nuestra mediciones.
from datetime import datetime

with open('inventario.txt','w', encoding='UTF-8') as reportes:
    reportes.write(f'Invetario GAD_PARROQUIAL_TARQUI_2026, Documentos pertencientes al expediente de vialidad\n')
    reportes.write(f'El número de archivos es: {file_counter}\n')
    reportes.write(f'El número de carpetas es, {directory_counter}\n')
    reportes.write(f'La comporbación es, {directory_counter+file_counter}\n')

