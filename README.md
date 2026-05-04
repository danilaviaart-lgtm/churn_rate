# 📉 Predicción de Churn Rate - Sector TELECOM

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)

Este proyecto implementa una solución integral de **Machine Learning** para detectar y predecir la tasa de cancelación (Churn Rate) en una base de datos de clientes del sector de las telecomunicaciones. 

A través de una plataforma interactiva construida con **Streamlit**, el proyecto no solo entrena modelos predictivos, sino que proporciona herramientas visuales y prácticas para analizar el comportamiento de los usuarios, anticipar fugas y ofrecer recomendaciones de retención ("Proactividad - Cliente primero").

## ✨ Características de la Aplicación

La aplicación está dividida en varias secciones accesibles desde el menú lateral:

* 🏠 **Inicio:** Resumen del proyecto y definición técnica del Churn Rate.
* 📊 **EDA (Análisis Exploratorio de Datos):** Visualización de datos de una base de aproximadamente 7,000 clientes. Revela insights clave, como una tasa de cancelación general del **26.32%** (1 de cada 4 clientes) y la influencia directa del tipo de contrato (ej. mes a mes).
* 💼 **Negocio:** Enfoque estratégico del proyecto. Busca pasar de un modelo reactivo a uno **proactivo**, entendiendo que cada cliente es importante y que el ML es una herramienta para la retención.
* ⚙️ **Metodología Técnica:** Documentación paso a paso del pipeline de datos. Desde la ingesta de datos (dataset de Kaggle), hasta la limpieza (nulos, outliers) y la ingeniería de características (ej. cálculo de antigüedad basado en `TotalCharges` y `MonthlyCharges`).
* 📝 **Formulario de Retención (Herramienta):** Un formulario interactivo donde se pueden ingresar manualmente los datos demográficos y servicios contratados de un cliente específico para obtener una estimación de fuga en tiempo real y recomendaciones de actuación.
* 📁 **Trabajar con Fichero (Batch Processing):** Permite subir archivos `.csv` o `.xlsx` (hasta 200MB) para realizar predicciones masivas de Churn sobre toda una base de clientes de forma rápida.

## 🧠 Modelos de Machine Learning Evaluados

Durante la fase de experimentación (documentada en la carpeta `notebooks/`), se entrenaron y evaluaron múltiples algoritmos de clasificación para encontrar el que mejor se adaptara a la detección de fuga:

* 🌲 Random Forest (`trained_model_Random_Forest.pkl`)
* 🚀 Gradient Boosting (`trained_model_Gradient_Boosting.pkl`)
* 📈 Regresión Logística (`trained_model_Regresion_Logistica.pkl`)
* 📍 K-Nearest Neighbors (K-NN) (`trained_model_K-NN.pkl`)
* ⚔️ Support Vector Machines (SVC) (`trained_model_SVMSVC.pkl`)

El modelo con mejor rendimiento ha sido seleccionado y exportado como `final_model.pkl` para su despliegue en la aplicación.

## 📂 Estructura del Proyecto
```text
churn_rate/
├── .devcontainer/           # Configuración del entorno de desarrollo
├── app_streamlit/           # Código fuente de la aplicación web
│   ├── assets/              # Imágenes, iconos y estilos
│   ├── pages/               # Páginas individuales de la app
│   │   ├── about.py
│   │   ├── EDA.py
│   │   ├── Formulario.py
│   │   ├── Negocio.py
│   │   ├── portada.py
│   │   ├── subircsv.py
│   │   └── Tecnico.py
│   └── main.py              # Archivo principal de ejecución de Streamlit
├── data/                    # Almacenamiento de datos locales
│   ├── processed/           # Datos limpios y listos para ML
│   └── raw/                 # Datos originales (Kaggle)
├── models/                  # Modelos entrenados y exportados (.pkl)
├── notebooks/               # Jupyter Notebooks (Pipeline de ML)
│   ├── 01_Fuentes.ipynb     # Carga e inspección de datos
│   ├── 02_LimpiezaEDA.ipynb # Limpieza y Análisis Exploratorio
│   └── 03_Modelo.ipynb      # Entrenamiento y evaluación de modelos
├── pyproject.toml           # Dependencias y configuración del proyecto
└── README.md
```

## 🛠️ Instalación y Uso Local

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/danilaviaart-lgtm/churn_rate.git](https://github.com/danilaviaart-lgtm/churn_rate.git)
   cd churn_rate
   ```

2. **Crea un entorno virtual e instala las dependencias:**
   Si usas entornos virtuales estándar:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   pip install -r requirements.txt # (O usando poetry/pip install . si está en pyproject.toml)
   ```

3. **Ejecuta la aplicación de Streamlit:**
   ```bash
   streamlit run app_streamlit/main.py
   ```

4. **Accede a la app:**
   Abre tu navegador web y ve a `http://localhost:8501`.
