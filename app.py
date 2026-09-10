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

st.title(f'El número de archivos es')
st.metric('',f' {file_counter}')
st.title(f'El número de carpetas es')
st.metric('',f' {directory_counter}')
st.title(f'La comprobación es')
st.metric('',f'{directory_counter + file_counter + others_counter }')
st.title(f'El peso de los archivos es')
st.metric('',f'{round((total_weight/1024)/1024,2) } MB')
st.title(f'El peso de los archivos es')
st.metric('', f' {round(((total_weight/1024)/1024)/1024,2) } GB')

import anthropic

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
pregunta_user = st.text_input("Make a question about measurements from the documents")

if st.button("Pedir informe a Claude") and pregunta_user != "":
    pregunta = f"{pregunta_user} Datos del censo hoy: {file_counter+directory_counter}  File's size today{round(((total_weight/1024)/1024)/1024,2) } GB"          # tu prompt, con tus números adentro: {file_counter}, {total_weight}...
    respuesta = client.messages.create(
        model="claude-sonnet-5",           # el ID exacto, copiado de docs.claude.com/en/docs/about-claude/models — elige el más barato
        max_tokens=400,
        messages=[{"role": "user", "content": pregunta}],
    )
    st.write(respuesta.content[0].text)