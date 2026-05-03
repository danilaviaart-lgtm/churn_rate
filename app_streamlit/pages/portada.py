import streamlit as st
import os

# Obtiene la ruta absoluta de la carpeta donde está este script
current_dir = os.path.dirname(os.path.abspath(__file__))

img_frrh = os.path.join(current_dir, "../assets", "frrh.png")
st.title("Churn Rate TELECOM")
col1, col2 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col1:
    st.write("")
    st.image(img_frrh)
with col2:
    st.markdown("""
    ### Proyecto para detectar Churn Rate en un dataset de TELECOM
    Esta plataforma utiliza modelos de **`Machine Learning`** en tiempo real para analizar el comportamiento 
    de nuestra base de usuarios. Puedes subir un CSV o usar el formulario.
    """)
st.divider()
st.markdown("""
* **Fórmula:**
    `(Clientes perdidos en el periodo / Clientes totales al inicio del periodo) x 100`
""")

st.markdown("""
    * **EDA**: en esta sección encuentras un pequeño EDA del dataset
    * **Negocio**: ¿ Qué importancia tiene el MC en el Negocio ?
    * **Técnico**: En esta sección se muestran los pasos para el desarrollo de la metodología
    * **Formulario**: Puedes ingresar los detalles de tu cliente para obtener una estimación de la probabilidad de retención.
    Tambien devolverá recomendaciones para interactuar con el cliente.
    * **Subir CSV**: Puedes ingresar un CSV para procesar más rapido tu dataset.
""")