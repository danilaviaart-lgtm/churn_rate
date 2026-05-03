import streamlit as st
import pandas as pd
import os

# Obtiene la ruta absoluta de la carpeta donde está este script
current_dir = os.path.dirname(os.path.abspath(__file__))

img_complete = os.path.join(current_dir, "../assets", "complete.png")
img_client = os.path.join(current_dir, "../assets", "client.png")
img_money = os.path.join(current_dir, "../assets", "money.png")
img_efici = os.path.join(current_dir, "../assets", "efici.png")
img_goals = os.path.join(current_dir, "../assets", "goals.png")
dataframe1 = os.path.join(current_dir, "../../data/processed/", "dataset_final_grupos.csv")
df = pd.read_csv(dataframe1)

st.title("Analisis Negocio Churn Rate TELECOM")
st.image(img_complete)
st.markdown("""
Para el negocio es muy importante tener un modelo que nos ayude a detectar fugas y poder ofrecer soluciones acorde a cada cliente.
Necesitamos generar un modelo de ML para tener una estrategia `Proactiva`, no esperemos que el cliente se vaya... anticipemos y ofrezcamos soluciones acorde a cada cliente.
""")

col1, col2 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col1:
    st.image(img_client, width=300)
with col2:
    st.markdown("""
    ## Cliente primero
    Todo cliente es importante, pero algunos clientes son más importantes. No dejemos que ninguno se vaya.
    """)
st.divider()

col3, col4 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col3:
    st.markdown("""
    ## Recurrencia
    Previsión de ingresos por cliente. Si perdemos clientes, perdemos ingresos. Localicemos posibles fugas y actuemos proactivamnete.
    """)
with col4:
    st.image(img_money, width=300)
st.divider()

col5, col6 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col5:
    st.image(img_efici, width=300)
with col6:
    st.markdown("""
    ## Eficiencia
    El tiempo es Oro, por lo tanto la eficiencia es Oro.
    Si detectamos los clientes con más provabilidad de fuga, podemos destinar el tiempo que tenemos en lo que realmente importa. Cliente con buenos importes y que se vayan a ir.
    """)
st.divider()

col7, col8 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col7:
    st.markdown("""
    ## Pain Points
    Detectemos nuestros puntos malos y actuemos en consecuencia.
    Detectamos problemas con nuestros servicios para ofrecer mejores soluciones.            
    """)
with col8:
    st.image(img_goals, width=300)

st.divider()

st.markdown("""
## Reflexión :

La metafora del cubo agujereado nos ayuda a entender los problemas de nuestro negocio.
Jamas vamos a llenar el cubo agujereado, pero podemos entender que es lo que nos falta para llegar a la meta.
Y asi intentar tapar esos agujeros.
""")