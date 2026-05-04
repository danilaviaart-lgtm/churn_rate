import streamlit as st
import pandas as pd
import os

# Obtiene la ruta absoluta de la carpeta donde está este script
current_dir = os.path.dirname(os.path.abspath(__file__))

img_complete = os.path.join(current_dir, "../assets", "complete.png")
img_client = os.path.join(current_dir, "../assets", "client.png")
img_money = os.path.join(current_dir, "../assets", "money.png")
img_efici = os.path.join(current_dir, "../assets", "efici.png")
img_goals = os.path.join(current_dir, "../assets", "goals.png")
dataframe1 = os.path.join(current_dir, "../../data/processed/", "dataset_final_grupos.csv")
df = pd.read_csv(dataframe1)

st.title("Analisis Negocio Churn Rate TELECOM")
st.image(img_complete)
st.markdown("""
Para el negocio es muy importante tener un modelo que nos ayude a detectar fugas y poder ofrecer soluciones acorde a cada cliente.
Necesitamos generar un modelo de ML para tener una estrategia `Proactiva`, no esperemos que el cliente se vaya... anticipemos y ofrezcamos soluciones acorde a cada cliente.
""")

col1, col2 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col1:
    st.image(img_client, width=300)
with col2:
    st.markdown("""
    #### 👑 El Cliente en el Centro:
    Priorización Estratégica
                
    No todos los clientes impactan de la misma forma en la rentabilidad del negocio. Nuestro objetivo es blindar la relación con aquellos usuarios estratégicos que sostienen la estructura de ingresos. No se trata solo de evitar que se vayan, sino de crear barreras de salida basadas en la excelencia, asegurando que nuestra propuesta de valor sea tan alta que ni siquiera se planteen buscar alternativas.
    """)
st.divider()

col3, col4 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col3:
    st.markdown("""
    #### ⚡ La Fuerza de la Recurrencia:
    De Reactivos a Proactivos
    
    La previsibilidad financiera depende directamente de nuestra capacidad para retener clientes.
                
    Cada cliente perdido no es solo una factura menos este mes, es un agujero en la previsión de ingresos a largo plazo y un coste hundido en marketing y adquisición. 
    Debemos abandonar la postura reactiva y utilizar los datos para anticiparnos: monitorizar el comportamiento de los usuarios, identificar señales tempranas de insatisfacción y actuar con planes de retención antes de que el cliente tome la decisión de abandonarnos.
                    """)
with col4:
    st.image(img_money, width=300)
st.divider()

col5, col6 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col5:
    st.image(img_efici, width=300)
with col6:
    st.markdown("""
    #### ⚙️ Eficiencia Operativa
    La eficiencia consiste en saber elegir nuestras batallas. No podemos salvar a todos los clientes con el mismo nivel de esfuerzo. Debemos cruzar dos variables críticas: Probabilidad de fuga y Valor del cliente. Al identificar a los clientes de alto impacto económico que muestran riesgo de abandono, podemos desplegar a nuestros mejores equipos y recursos de manera quirúrgica. Salvar a una gran cuenta en riesgo justifica el tiempo invertido; destinar horas a clientes de bajo valor y baja retención es un desperdicio de recursos.
    """)
st.divider()

col7, col8 = st.columns([1, 1]) # La segunda columna es el doble de ancha
with col7:
    st.markdown("""
    #### 🛠️ El Feedback como Oportunidad
    No debemos temer a las quejas, sino a la indiferencia. Los problemas o frustraciones que los clientes experimentan con nuestro servicio son mapas del tesoro que nos indican exactamente dónde debemos mejorar. Al mapear y analizar sistemáticamente estos "puntos de dolor", dejamos de poner parches temporales y empezamos a rediseñar soluciones estructurales. Transformar una mala experiencia en una solución definitiva no solo salva a un cliente, sino que mejora el producto para todos los demás.           
    """)
with col8:
    st.image(img_goals, width=300)

st.divider()
st.markdown("""
## 🪣 Reflexión: El Síndrome del Cubo Agujereado
La metáfora del cubo agujereado ilustra el error más común en el crecimiento empresarial: la obsesión por las ventas (el agua que entra) ignorando la retención (los agujeros del cubo).

* **El esfuerzo inútil:** Gastar dinero y energía en adquirir nuevos clientes pierde todo su sentido si, una vez dentro, se escapan por la base debido a un mal servicio o falta de seguimiento.

* **La solución:** El crecimiento sostenible no se logra abriendo más el grifo, sino tapando primero las fugas. Entender por qué se van nuestros clientes es el primer paso para sellar esos agujeros. Solo cuando el cubo es estanco, el esfuerzo de ventas se traduce en un crecimiento real, escalable y duradero.
""")
st.divider()

st.markdown("""
## 📈 Métricas para medir las "Fugas" (Recurrencia y Abandono)
### 🚪 Customer Churn Rate (Tasa de Cancelación de Clientes):

* **Qué es:** El porcentaje de clientes que te abandonan en un periodo de tiempo determinado (mensual o anual).
* **Por qué importa:** Es la medida exacta de tu "cubo agujereado". Si tienes 100 clientes y se van 5 este mes, tu Churn es del 5%.

### 💸 Revenue Churn Rate (Tasa de Cancelación de Ingresos):

* **Qué es:** El porcentaje de dinero que pierdes cuando los clientes se van o reducen sus compras.

* **Por qué importa:** Como decíamos, no todos los clientes son iguales. Perder 5 clientes que pagan poco duele menos que perder a 1 solo cliente que factura grandes cantidades. Esto te da la visión financiera de la fuga.
""")