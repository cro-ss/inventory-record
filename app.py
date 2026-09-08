import streamlit as st
from pathlib import Path
st.title('inventory')
st.metric('Archivos_Documentos_PARAPEPUDOS_OCIOSOS', 1999 )


root =  Path(r'C:\Users\chris\OneDrive\Desktop\Crostian Asus\Ing_Bermeo_C\CLAUDE_CODE\GAD_TARQUI_2026')
st.metric('raiz_archivos',root.exists())

contador = 0
for elemento in root.rglob('*'):
    contador = contador+1
st.metric('Elementos en el expediente', contador)
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

st.metric('',f'El número de archivos es {file_counter}')
st.metric('',f'El número de carpetas es {directory_counter}')
st.metric('',f'La comprobación es {directory_counter + file_counter + others_counter }')
st.metric('',f'El peso de los archivos es {round((total_weight/1024)/1024,2) } MB')
st.metric('',f'El peso de los archivos es {round(((total_weight/1024)/1024)/1024,2) } GB')