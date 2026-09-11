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
no_available = 0
others_counter=0

for elemento in root.rglob('*'):
   print(len(str(elemento)))
   try:
    if elemento.is_file() == True:
        file_counter = file_counter + 1
        in_weight = elemento.stat().st_size
        total_weight += in_weight

    elif elemento.is_dir():
         directory_counter += 1
    else:
        others_counter += 1
   except OSError:
        no_available += 1

print(f'El número de archivos es {file_counter}')
print(f'El número de carpetas es {directory_counter}')
print(f'La comprobación es {directory_counter + file_counter + others_counter }')
print(f'El peso de los archivos es {round((total_weight/1024)/1024,2) } MB')
print(f'El peso de los archivos es {round(((total_weight/1024)/1024)/1024,2) } GB')


###### Vamos a generar comando en este script de python.
###### Lo que buscamos aqui es presentar los resultados de nuestra mediciones.
total_elements=directory_counter+file_counter
total_weight_mb= (total_weight/1024)/1024
from datetime import datetime

with open('inventario.txt','w', encoding='UTF-8') as reportes:
    reportes.write(f'{root.name}, Documentos pertencientes al expediente de vialidad\n')
    reportes.write(f'Generado: {datetime.now().strftime("%d/%b/%Y %H:%M:%S")}\n')
    reportes.write(f'El número de archivos es: {file_counter}\n')
    reportes.write(f'El número de carpetas es, {directory_counter}\n')
    reportes.write(f'El número archivos de otro formato es, {others_counter}\n')
    reportes.write(f'La comprobación es, {directory_counter+file_counter+others_counter}\n')
    reportes.write(f'El peso de los archivos es {round((total_weight/1024)/1024,2)} MB\n')
    reportes.write(f'El peso total de los archivos es: {round(((total_weight/1024)/1024)/1024,2)}GB\n')
    reportes.write(f'Los archivos no leidos son : {no_available}\n')

####### We've created a csv that will register new elements every day (row)
with open('history.csv','a',encoding='UTF-8') as new_rows:
    new_rows.write(f'{datetime.now().strftime('%Y-%m-%d')},{file_counter},{directory_counter},{total_elements},{round(total_weight_mb,2)},{others_counter}\n')


