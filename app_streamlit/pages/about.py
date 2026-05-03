import streamlit as st
import os

# Obtiene la ruta absoluta de la carpeta donde está este script
current_dir = os.path.dirname(os.path.abspath(__file__))

img_about = os.path.join(current_dir, "../assets", "about.png")

col1, col2 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col1:
    st.image(img_about)
with col2:
    st.markdown("""
    Proyecto de Machine Learning sobre el analisis del Chrun Rate en un dataset de Telecom  desarrollado por `Daniel Lavía` para el Bootcamp de Data Science.
    Implementación de Machine Learning en Streamlit. 
    """)
    st.markdown("""
    #### Mejoras a futuro :
    * Segregar a los clientes por % de probabilidad con más variables, para no ser tan binario en 0 y 1.
    * Mejoras junto a Negocio de opciones en descuentos y servicios.
    * Mail automático con descuentos o servicios.
    """)
st.divider()
st.markdown("""
## Desglose del proyecto
### Dataset
El dataset utilizado es de https://www.kaggle.com/
### Dependencias
* **Python**
>* **Streamlit**
>* **joblib>=1.5.3**
>* **numpy>=2.4.4**
>* **openpyxl>=3.1.5**
>* **pandas>=2.3.3**
>* **scikit-learn>=1.8.0**
>* **sdv>=1.36.1**
>* **streamlit>=1.57.0**
>* **matplotlib>=3.10.9**
""")