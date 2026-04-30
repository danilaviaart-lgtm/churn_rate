#importamos los datos
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(layout="wide")
#modal para que salga todo en ventana
@st.dialog("📊 Resultados de la Predicción", width="large")
def modal_predicciones(df, modelo):
    # Realizar la predicción
    predicciones = modelo.predict(df)
    
    # si la devuelve que la calcule medias
    if hasattr(modelo, "predict_proba"):
        df['Probabilidad_%'] = (modelo.predict_proba(df)[:, 1] * 100).round(2)
        
        #media de probabilidad para mostrarla
        media_prob = df['Probabilidad_%'].mean()
        st.metric(label="Media de Probabilidad de Churn", value=f"{media_prob:.2f}%")
        st.divider()

    # logica de segmentacion
    def categorizar(dinero):
        if dinero < 20:
            return "Cliente importe bajo no ofrecere descuento"
        elif 30 <= dinero < 70:
            return "Cliente importe medio no ofrecere descuento sin cambiar de contrato"
        else:
            return "Cliente que ofrecemos descuento si o si"
            
    # Aplicamos la segmentación solo si la columna existe en el CSV
    if 'MonthlyCharges' in df.columns:
        df['Nivel_Gasto'] = df['MonthlyCharges'].apply(categorizar)
        
    st.success("¡Predicciones añadidas correctamente!")
    
    st.write("### Resultados")
    st.dataframe(df.head())

    # Opción para descargar el nuevo CSV desde dentro del modal
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar resultados en CSV",
        data=csv,
        file_name="predicciones_resultados.csv",
        mime="text/csv",
        use_container_width=True
    )


# pagina normal

st.title("Subir Archivo CSV")
col1, col2 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col1:
    st.image("assets/csv.png", width=300)
with col2:
    st.write("Recuerda que sea CSV o Excel")
    archivo_subido = st.file_uploader("Elige un archivo", type=["csv", "xlsx", "xls"])
    st.write("Si prefieres, puedes descargar un archivo sintentico de prueba")
    st.download_button(
        label="Descargar archivo de prueba",
        data=pd.read_csv('../data/processed/datos_prueba_ml2.csv').to_csv(index=False).encode('utf-8'),
        file_name="dataset_sintetico.csv",
        mime="text/csv",
        use_container_width=True
    )

if archivo_subido is not None:
    # Verificamos la extensión del nombre del archivo
    if archivo_subido.name.endswith('.csv'):
        df = pd.read_csv(archivo_subido)
    else:
        # Para archivos .xls o .xlsx
        df = pd.read_excel(archivo_subido)
    
    st.success("¡Archivo subido con éxito!")
    st.write("Vista previa de los datos:")
    st.dataframe(df) # Muestra una tabla interactiva

    @st.cache_resource
    def cargar_modelo():
        return joblib.load("../models/final_model.pkl") 

    # Cargamos el modelo
    modelo = cargar_modelo()

    # Boton para generar modal y predict
    if st.button("Generar Predicciones", type="primary", use_container_width=True):
        modal_predicciones(df, modelo)