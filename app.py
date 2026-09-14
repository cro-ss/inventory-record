import streamlit as st
from pathlib import Path
import pandas as pd
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

# calling a csv history
history= pd.read_csv('history.csv', parse_dates=["date"])
st.dataframe(history)
st.line_chart(history, x='date', y='n_elements')
context = history.tail(8).to_csv(index=False)










###############################_____________CLAUDE___________________________###################################
# HERE WE JUST CALLING AN API THAT CAN MAKE ASSUMPTIONS ON MY DATA
# Claude won't read dataframe just str which means that i need to return the csv
import anthropic
context= history.tail(8).to_csv(index=False)
client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
pregunta_user = st.text_input('')


for i in range(100):
    if st.button("Pedir informe a Claude") and pregunta_user != "":
        pregunta = f"""Tu rol es de analista de datos experto en contratación pública, el contexto es:{context}.
                        Algo importante que tienes que entender es que en una fecha (2026-08-17 hasta 2026-08-24) si hubo crecimiento real y orgánico del expediente, con algunos elementos por leer debido al MAXPATH.
                        Despues desde 2026-08-26 al 2026-09-04 creamos un if para leer los n_unclassified, los elementos que existian pero no eran leidos por la limitación del MAXPATH.
                        Desde el 2026-09-07 en adelante, al romper la barrera de caracteres se pudo identificar si los archivos de rutas grandes eran files or directories.  
                        Pregunta:{pregunta_user} """          # tu prompt, con tus números adentro: {file_counter}, {total_weight}...
        respuesta = client.messages.create(
            model="claude-sonnet-5",           # el ID exacto, copiado de docs.claude.com/en/docs/about-claude/models — elige el más barato
            max_tokens=8000,
            messages=[{"role": "user", "content": pregunta}],
        )

        for bloque in respuesta.content:
        
            if bloque.type == 'text':
                st.write(bloque.text)
            
        #st.write(respuesta.stop_reason)
        #st.write(respuesta.usage)