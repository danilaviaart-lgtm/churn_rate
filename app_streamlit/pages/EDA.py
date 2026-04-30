import streamlit as st
import pandas as pd

df = pd.read_csv('assets/dataset_final_grupos.csv')

st.title("Analisis EDA Churn Rate TELECOM")
st.image("assets/tecnico.png")
st.markdown("""
"Analisis de unos **`7000 clientes de nuestra operadora`**. La tasa de cancelación (Churn)
general es de **`26.32%`**.
Esto significa que `1 de cada 4 clientes se van a la competencia`
El análisis revela que los clientes que se dan de baja no son un grupo homogéneo.
Existen perfiles de riesgo muy claros.
""")

st.write("## Distribución de Fuga")
st.bar_chart(df['Churn'].value_counts())
st.divider()
st.write("## Distribución por Contratos")
col1, col2 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col1:
    contrato = df.groupby(['Contract', 'Churn']).size().unstack(fill_value=0)
    st.bar_chart(contrato, stack=False)

with col2:
    st.markdown("""
    La diferencia de tasa de cancelación es muy alta entre contratos.
    * **Contrato Mensual `(Month-to-month)`:** Tasa de Churn del **42.7%**. Casi la mitad de los clientes con este contrato se van. Es un punto de fuga masivo.
    * **Contrato Anual `(One year)`:** La tasa de cancelación cae drásticamente al **11.3%**.
    * **Contrato Bianual `(Two year)`:** La tasa es mínima, solo del **2.9%**.

    > **Conclusión de negocio:** La prioridad número uno debe ser incentivar a los clientes a migrar de contratos de mes a mes a los anules, ofreciendo servicios adicionales.
    """)

st.divider()
st.write("## ¿ Son más fieles con el tiempo ?")

col5, col6 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col5:
    st.write("Meses de Antiguedad con el Servicio")
    g_antiguedad= df.groupby(['g_antiguedad', 'Churn']).size().unstack(fill_value=0)
    ordenar = [
    "Hasta 12 meses", 
    "12 a 24", 
    "24 a 48", 
    "Más de 48", 
    ]
    g_antiguedad = g_antiguedad.reindex(ordenar)
    st.bar_chart(g_antiguedad, stack=False)
with col6:
    st.markdown("""
    Tenemos muy claro que cuantos más años estén con nosotros más contentos y menos provabilidades hay de que se vayan.
    * **Hasta 12 meses:** Los `clientes nuevos` son un riesgo casi la mitad se van antes del año.
    * **Más de 12 meses:** Se reduce muchisimo la `fuga de clientes`.
 > **Conclusión:** Invertir en un plan de **OFERTAS ESPECIALES** sólidas durante el primer año es crucial para "asegurar" al cliente a largo plazo.
                """)
st.divider()
st.write("## ¿ Cómo pagan nuestros clientes ?")

col5, col6 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col5:
    t_pagos = df.groupby(['PaymentMethod', 'Churn']).size().unstack(fill_value=0)
    st.bar_chart(t_pagos, stack=False)
with col6:
    st.markdown("""
    La forma de pago nos indica el nivel de compromiso del cliente.
    * **Cheque Electrónico `(Electronic check)`** **45.3%** (Muy Alto)
    * **Cheque por Correo `(Mailed check)`** 34.5%
    * **Transferencia Automática `(Bank transfer)`** 16.6%
    * **Tarjeta de Crédito `(automatic)`** 16.1%
    > **Conclusión:** Migrar a los clientes del cheque electrónico hacia métodos de pago automáticos (con un pequeño incentivo) debería ser una táctica clave.
                """)

st.divider()
st.write("## Otras Métricas")

col3, col4 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col3:
    st.write("Distribución de Generos")
    genero= df.groupby(['gender', 'Churn']).size().unstack(fill_value=0)
    st.bar_chart(genero, stack=False)
with col4:
    st.write("Tipo de Acceso a Internet")
    s_internet= df.groupby(['InternetService', 'Churn']).size().unstack(fill_value=0)
    st.bar_chart(s_internet, stack=False)

col7, col8 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col7:
    st.write("Soporte Tecnológico")
    tsoporte= df.groupby(['TechSupport', 'Churn']).size().unstack(fill_value=0)
    st.bar_chart(tsoporte, stack=False)
with col8:
    st.write("Seguridad Online")
    s_online= df.groupby(['OnlineSecurity', 'Churn']).size().unstack(fill_value=0)
    st.bar_chart(s_online, stack=False)

st.markdown("""
Muy atentos a los Servicios....
* **`Género:`** No detectamos relevancia entre hombres y mujeres.
* **`Acceso a Internet:`** Muchos clientes con Fibra Óptica se van.. hay que revisar las reseñas.
* **`Soporte Tecnológico:`** Gran adopción del servicio, si lo usan la gente no tiende a irse.
* **`Seguridad Online:`** El servicio de Seguridad Online funciona bien, deberíamos ofrecer este servicio para que la gente quede suscrita.     
""")
st.divider()