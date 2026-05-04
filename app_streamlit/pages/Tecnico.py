import streamlit as st
import pandas as pd
import numpy as np
import os
# Obtiene la ruta absoluta de la carpeta donde está este script
current_dir = os.path.dirname(os.path.abspath(__file__))

img_1 = os.path.join(current_dir, "../assets", "1.png")
resultados = os.path.join(current_dir, "../../data/processed/", "resultados_modelos.csv")

st.title("Metodología Técnica")
st.image(img_1)

st.markdown("""
## 1. 🛠️ Preparación y Transformación de Datos 
El proceso comienza con la selección de un dataset de Kagle.
Una vez lo seleccionamos hacemos una limpieza principal de : nulos, revisión outliers, duplicados, etc.
Para rellenar las faltantes, se utilizan medias o en el caso de la Antiguedad se utiliza la divisón del `TotalCharges` por `MonthlyCharges`.
""")

codigo1 = """
#Quitamos los 0 en antiguedad y lo dividimos por los cargos mensuales
mask = df['Antiguedad'] == 0
df.loc[mask, 'Antiguedad'] = (df['TotalCharges'] / df['MonthlyCharges']).astype(int)"""
st.code(codigo1)

st.markdown("""
Una vez hemos limpiado el dataset lo guardamos en un archivo `dataset_final.csv` para poder trabajarlo a posterior.
### Variable objetivo
El objetivo principal es predecir si un cliente se va de la empresa o no, por lo que se utiliza la variable `Churn` como variable objetivo.
Como la variable es de tipo texto("Yes","No"), se utiliza `LabelEncoder` para transformar las etiquetas de texto en valores numéricos (1,0), lo cual facilita el procesamiento por algoritmos de clasificación.
""")

codigo2 = """
le = LabelEncoder()
y = le.fit_transform(y)"""
st.code(codigo2)

st.markdown("""
### Features
Se seleccionan las features de cada tipo, categoricas y númericas para luego poder preprocesarlas.
""")
codigo3 = """
# Seleccionamos las important features de cada tipo, categoricas y númericas para luego poder preprocesarlas.
num_features = ['Antiguedad','MonthlyCharges']
cat_features = ['InternetService', 'PaymentMethod', 'Contract', 
    'PaperlessBilling', 'OnlineSecurity', 'TechSupport', 'SeniorCitizen']
"""
st.code(codigo3)
st.markdown("""
* **Segmentación de Features:**

    * **Variables Numéricas (3):** `Antiguedad`, `MonthlyCharges`.
    * **Variables Categóricas (7):** Información general y detalles de servicios contratados (género, servicios de internet, seguridad, métodos de pago, etc.).
""")

st.markdown("""   
## 2. 🏗️ Arquitectura del Pipeline de Preprocesamiento
Para todo el proceso se utiliza un `Pipeline` con `ColumnTransformer` para garantizar que se puede reproducir el mismo preprocesamiento en cualquier momento, asi evitando el `*data leakage*`.        
* **Tratamiento Numérico:** Aplicación de `StandardScaler` para evitar que unas variables "dominen" a otras, asegurando que variables con rangos grandes no dominen injustamente el modelo sobre otras.
""")
codigo4 = """
pre_num = Pipeline(steps=[
    ('scaler', StandardScaler())
pre_log = Pipeline(steps=[
    ('logaritmico', FunctionTransformer(np.log1p, validate=True))
])# Al Eliminar TotalCharges se elimina la multicolinealidad
"""
st.code(codigo4)
            
st.markdown("""
* **Tratamiento Categórico:** Aplicación de `OneHotEncoder` con `drop='first'`. Esto convierte categorías en columnas binarias evitando la "trampa de la variable ficticia" (multicolinealidad).
Tambien usamos `handle_unknown='ignore'` por si encontramos un valor desconocido en el test no bloque el modelo.
            """)
codigo5 = """
pre_cat = Pipeline(steps=[
    ('onehot', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'))
])
"""
st.code(codigo5)
st.markdown("""
Construimos todo en un ColumnTransform para aplicac diferentes transformaciones a distintas columnas de un conjunto de datos (dataset) al mismo tiempo, agrupando todo el proceso en un solo paso.
""")
codigo6 ="""
ct = ColumnTransformer(transformers=[
    ('num', pre_num, num_features),
    ('cat', pre_cat, cat_features)
])
"""
st.code(codigo6)

st.markdown("""
## 3. 🧠 Modelos
Se utilizan los modelos de `Regresion Logistica`, `Random Forest`, `SVM(SVC)`, `Gradient Boosting` y `K-NN` . El modelo final se entrena con `GridSearchCV` para encontrar los mejores hiperparametros.
""")
codigo7 ="""
modelos = {
    'Regresion_Logistica': LogisticRegression(max_iter=1000, random_state=semilla,class_weight='balanced'),
    'Random_Forest': RandomForestClassifier(random_state=semilla,class_weight='balanced'),
    'SVM(SVC)': SVC(probability=True, random_state=semilla,class_weight='balanced'),
    'Gradient_Boosting': GradientBoostingClassifier(random_state=semilla),
    'K-NN': KNeighborsClassifier()
}"""
st.code(codigo7)
st.markdown("""
Usamos `PCA` para eliminar la `Multicolinealidad` y reducir las dimensiones de las features. Lo ponemos en un 0.95% para que explique el 95% de los clientes y solo destruya un 5%. Lo insertamos directamente en el pipeline.
""")
codigo8 ="""
('PCA', PCA(n_components=0.95)
"""
st.code(codigo8)

st.markdown("""          
## 4. 📊 Evaluación Comparativa de Modelos
Se entrenan y evalúan cinco algoritmos bajo condiciones similares para identificar el mejor candidato:
""")
df = pd.read_csv(resultados)
st.table(df)

st.markdown("""
* **Decisión:** Elegimos **Regresión Logística** por su equilibrio y buen ROC-AUC porque mide la capacidad real del modelo para distinguir entre clases sin importar el desbalance de datos ni el umbral de decisión.
A diferencia del Accuracy o el Recall, evalúa la calidad de la separación probabilística, asegurando que el modelo sea robusto y confiable.
""")

st.markdown("""
## 5. 🧪 Hiperparámetros (GridSearchCV)
Con la Regresión Logística seleccionada, se realiza una búsqueda en rejilla (*Grid Search*) para maximizar el *Recall*:
* **Parámetros probados:** Regularización `C` (fuerza), tipos de penalización (`l1`, `l2`) y diferentes algoritmos de optimización (`liblinear`, `lbfgs`).
""")

codigo9 ="""
param_grid = [
    {
        'clasificador__solver': ['liblinear'], 
        'clasificador__penalty': ['l1', 'l2'], 
        'clasificador__C': [0.01, 0.1, 1, 10, 100]
    },
    {
        'clasificador__solver': ['lbfgs'], 
        'clasificador__penalty': ['l2'], 
        'clasificador__C': [0.01, 0.1, 1, 10, 100]
    }
]
grid_search = GridSearchCV(
    estimator=modelo_final, # pipeline solo del modelo ganador
    param_grid=param_grid,
    scoring='recall',
    cv=5,
    n_jobs=-1
)"""
st.code(codigo9)


st.markdown("""
            
* **Ganador:** `C=0.1`, penalización `l1`, solver `liblinear`.
* **Resultado:** Se logra un *CV Score* (Recall medio en validación cruzada) de **0.8089**.
""")

st.markdown("""
## 6. 🚀 Modelo y producción
            
Nuestro modelo final :
* **Salida del Modelo:** Genera la predicción binaria y la probabilidad porcentual.
* **Variables de Salida:**
    * `Prediccion_Modelo`: Clasificación final (0 o 1).
    * `Churn Rate`: Probabilidad de que el cliente abandone el servicio.
            
Exportamos como `final_model.pkl` en la carpeta `models` y se aplica sobre dataset sintetico de 3000 registros generados con la librería Synthetic Data Vault (SDV).
    """)