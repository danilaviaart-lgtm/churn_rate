import streamlit as st
st.title("Sobre el proyecto")

col1, col2 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col1:
    st.image("assets/about.png")

with col2:
    st.markdown("""
    Proyecto de Machine Learning sobre el analisis del Chrun Rate en un dataset de Telecom  desarrollado por `Daniel Lavía` para el Bootcamp de Data Science.
    Implementación de Machine Learning en Streamlit. 
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