import streamlit as st
st.title("Churn Rate TELECOM")
st.image("assets/frrh.png")
st.markdown("""
    ### Proyecto para detectar Churn Rate en un dataset de TELECOM
    
    Esta plataforma utiliza modelos de **Machine Learning** en tiempo real para analizar el comportamiento 
    de nuestra base de usuarios. Puedes subir un CSV o usar el formulario.
    La metodología esta dividida entre
    * **EDA**: En esta sección encuentras un pequeño EDA del dataset
    * **Negocio**: ¿ Qué importancia tiene el MC en el Negocio ?
    * **Tecnico**: En esta seccion se muestran los pasos para el desarrollo de la metodología
    * **Formulario**: Puedes ingresar los detalles de tu cliente para obtener una estimación de la probabilidad de retención.
    Tambien devolverá recomendaciones para interactuar con el cliente.
    * **Subir CSV**: Puedes ingresar un CSV para procesar más rapido tu dataset.
""")