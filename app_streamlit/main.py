import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="centered")

pagina_inicio = st.Page("pages/portada.py", title="Inicio", icon="🏠")
pagina_eda = st.Page("pages/EDA.py", title="EDA", icon="📊")
pagina_negocio = st.Page("pages/Negocio.py", title="Negocio", icon="📈")
pagina_tecnico = st.Page("pages/Tecnico.py", title="Técnico",icon = "🔧")
pagina_formulario = st.Page("pages/Formulario.py", title="Formulario", icon="📝")
pagina_subircsv = st.Page("pages/subircsv.py", title="Trabajar con fichero" ,icon="📁")
pagina_about = st.Page("pages/about.py", title="about",icon="👨‍💻")

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