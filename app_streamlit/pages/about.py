import streamlit as st
import os

# Obtiene la ruta absoluta de la carpeta donde está este script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Une esa ruta con la ubicación de la imagen
image_path = os.path.join(current_dir, "../assets", "about.png")

# Verifica si el archivo existe antes de cargarlo (para evitar que la app explote)
if os.path.exists(image_path):
    st.image(image_path)
else:
    st.error(f"No se encontró la imagen en: {image_path}")
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