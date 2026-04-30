import streamlit as st
import pandas as pd
import numpy as np
import os

st.write("Carpetas detectadas:", os.listdir("."))

st.set_page_config(layout="centered")

pagina_inicio = st.Page("pages/portada.py", title="Inicio")
pagina_eda = st.Page("pages/EDA.py", title="EDA")
pagina_negocio = st.Page("pages/Negocio.py", title="Negocio")
pagina_tecnico = st.Page("pages/Tecnico.py", title="Técnico")
pagina_formulario = st.Page("pages/Formulario.py", title="Formulario")
pagina_subircsv = st.Page("pages/subircsv.py", title="Subir CSV")
pagina_about = st.Page("pages/about.py", title="about")

# 2. Agrupas las páginas en el menú de navegación con separadores
pg = st.navigation(
    {
        "Principal": [pagina_inicio],
        "Metogología": [pagina_eda, pagina_negocio, pagina_tecnico],
        "Herramientas": [pagina_formulario, pagina_subircsv],
        "About": [pagina_about]
    }
)

# 3. Ejecutas la navegación
pg.run()