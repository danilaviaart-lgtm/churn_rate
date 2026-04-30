import streamlit as st
import pandas as pd

df = pd.read_csv('../data/processed/dataset_final_grupos.csv')

st.title("Analisis Negocio Churn Rate TELECOM")
st.image("assets/complete.png")
st.markdown("""
Para el negocio es muy improtante tener un modelo que nos ayude a detectar fugas y poder ofrecer soluciones acorde a cada cliente.
Necesitamos generar un modelo de ML para tener una estategia `reactiva`, no esperemos que el cliente se vaya... anticipemos y ofrezcamos soluciones acorde a cada cliente.
""")

col1, col2 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col1:
    st.image("assets/client.png", width=300)
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
    st.image("assets/money.png", width=300)
st.divider()

col5, col6 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col5:
    st.image("assets/efici.png", width=300)
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
    st.image("assets/goals.png", width=300)

st.divider()

