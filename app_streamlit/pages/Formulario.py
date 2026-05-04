import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Obtiene la ruta absoluta de la carpeta donde está este script
current_dir = os.path.dirname(os.path.abspath(__file__))

img_undraw = os.path.join(current_dir, "../assets", "undraw.png")
img_good = os.path.join(current_dir, "../assets", "good.png")
img_sad = os.path.join(current_dir, "../assets", "sad.png")
modelofinal = os.path.join(current_dir, "../../models", "final_model.pkl")

# 1. Definimos el Modal con toda la lógica de predicción dentro
@st.dialog("Análisis de Retención de Cliente")
def mostrar_resultados(datos_df):
    # Cargamos el modelo
    # Nota: Asegúrate de que la ruta sea correcta relativa a donde ejecutas streamlit
        modelo_final = joblib.load(modelofinal)
        
        # Realizamos la predicción
        prediccion = modelo_final.predict(datos_df)
        probabilidades = modelo_final.predict_proba(datos_df)
        churn_prob = probabilidades[0, 1]  # Probabilidad de la clase 1 (Churn)
        
        # Lógica de categorización de gasto
        monthly_charges = datos_df['MonthlyCharges'].iloc[0]
        contract = datos_df['Contract'].iloc[0]

        # Mostrar resultados en el Modal
        print(prediccion)
        st.write(f"## **Probabilidad de Riesgo:** {churn_prob:.2f}%")
        if churn_prob >= 0.6:
            st.image(img_sad, width=300)
            st.error("## **Probabilidad de Riesgo:** ALTA")
            if contract == "Month-to-month":
                if monthly_charges > 30:
                    st.info("**Acción:** El cliente tiene ALTO riesgo de irse. Su pago mensual es alto y no tiene contrato anual. Ofrece un descuento 30% si se pasa al plan anual.")
                else:
                    st.info("**Acción:** El cliente tiene ALTO riesgo de irse. Su pago mensual es bajo y no tiene contrato anual. Ofrece un descuento 20% si se pasa al plan anual y un servicio gratis.")
            else:
                if monthly_charges > 30:
                    st.info("**Acción:** El cliente tiene ALTO riesgo de irse. Su pago mensual es alto y tiene contrato anual. Ofrece un descuento 30% y un servicio gratis.")
                else:
                    st.info("**Acción:** El cliente tiene ALTO riesgo de irse. Su pago mensual es bajo y tiene contrato anual. Ofrece un descuento 20%")        
            
        elif 0.4 <= churn_prob < 0.6: # Corregido: elif en lugar de else if, y lógica de límites
            st.image(img_good, width=300)
            st.warning("## **Probabilidad de Riesgo:** MEDIO")
            if contract == "Month-to-month":
                if monthly_charges > 30:
                    st.info("**Acción:** El cliente tiene MEDIO riesgo de irse. Su pago mensual es alto y no tiene contrato anual. Ofrece un 15% de descuento y plan anual")
                else:
                    st.info("**Acción:** El cliente tiene MEDIO riesgo de irse. Su pago mensual es bajo y no tiene contrato anual. Ofrece un 5% de descuento , plan anual y servicio gratis.")
            else:
                if monthly_charges > 30:
                    st.info("**Acción:** El cliente tiene MEDIO riesgo de irse. Su pago mensual es alto y tiene contrato anual.")
                else:
                    st.info("**Acción:** El cliente tiene MEDIO riesgo de irse. Su pago mensual es bajo y tiene contrato anual.")                     
        else:
            st.image(img_good, width=300)
            st.success("## **Probabilidad de Riesgo:** BAJA")
            if contract == "Month-to-month":
                if monthly_charges > 30:
                    st.info("**Acción:** El cliente tiene BAJO riesgo de irse. Su pago mensual es alto y no tiene contrato anual.")
                else:
                    st.info("**Acción:** El cliente tiene BAJO riesgo de irse. Su pago mensual es bajo y no tiene contrato anual.")
            else:
                if monthly_charges > 30:
                    st.info("**Acción:** El cliente tiene BAJO riesgo de irse. Su pago mensual es alto y tiene contrato anual.")
                else:
                    st.info("**Acción:** El cliente tiene BAJO riesgo de irse. Su pago mensual es bajo y tiene contrato anual.")                
            
        if st.button("Cerrar"):
                st.rerun()

st.title("Formulario")
col1, col2 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col1:
    st.image(img_undraw, width=300)
with col2:
    st.markdown("""
    Puedes ingresar los detalles de tu cliente para obtener una estimación de la probabilidad de retención.
    Tambien devolverá recomendaciones para interactuar con el cliente.
    """)


with st.form("formulario_cliente"):
    st.write("### Datos Demográficos")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("Género", ["Male", "Female"])
        senior = st.radio("¿Es Senior Citizen?", [0, 1], format_func=lambda x: "Sí" if x == 1 else "No")
    with col2:
        partner = st.radio("¿Tiene pareja? (Partner)", ["No", "Yes"])
        dependents = st.radio("¿Tiene dependientes?", ["No", "Yes"])
    
    st.write("### Servicios Contratados")
    col3, col4, col5 = st.columns(3)
    with col3:
        phone_service = st.selectbox("Servicio Telefónico", ["No", "Yes"])
        multiple_lines = st.selectbox("Múltiples Líneas", ["No", "Yes", "No phone service"])
        internet_service = st.selectbox("Servicio de Internet", ["No", "DSL", "Fiber optic"])
    with col4:
        online_security = st.selectbox("Seguridad Online", ["No", "Yes", "No internet service"])
        online_backup = st.selectbox("Backup Online", ["No", "Yes", "No internet service"])
        device_protection = st.selectbox("Protección de Dispositivo", ["No", "Yes", "No internet service"])
    with col5:
        tech_support = st.selectbox("Soporte Técnico", ["No", "Yes", "No internet service"])
        streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
        streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

    st.write("### Contrato y Facturación")
    col6, col7 = st.columns(2)
    with col6:
        antiguedad = st.slider("Antigüedad (meses)", 0, 100, 12)
        contract = st.selectbox("Tipo de Contrato", ["Month-to-month", "One year", "Two year"])
        paperless = st.radio("Facturación Electrónica", ["No", "Yes"])
    with col7:
        payment = st.selectbox("Método de Pago", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
        monthly_charges = st.number_input("Cargos Mensuales ($)", min_value=0.0, value=50.0)
        total_charges = st.number_input("Cargos Totales ($)", min_value=0.0, value=500.0)

    enviado = st.form_submit_button("Analizar Riesgo")
    
if enviado:
    #dataframe para la gestion, info del modelo machine learning
    nuevos_datos = pd.DataFrame({
        'Antiguedad': [antiguedad],
        'SeniorCitizen': [senior],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
        'gender': [gender],
        'Partner': [partner],
        'Dependents': [dependents],
        'PhoneService': [phone_service],
        'MultipleLines': [multiple_lines],
        'InternetService': [internet_service],
        'OnlineSecurity': [online_security],
        'OnlineBackup': [online_backup],
        'DeviceProtection': [device_protection],
        'TechSupport': [tech_support],
        'StreamingTV': [streaming_tv],
        'StreamingMovies': [streaming_movies],
        'Contract': [contract],
        'PaperlessBilling': [paperless],
        'PaymentMethod': [payment]
    })
    
  #enviar modal
    mostrar_resultados(nuevos_datos)