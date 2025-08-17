# Customer Churn Predictor 📊

Este proyecto implementa un pipeline completo de **análisis y predicción de churn (fuga de clientes)**.  
El objetivo es demostrar buenas prácticas en **análisis de datos, preprocesamiento, modelado y despliegue reproducible**.

---

## 📂 Estructura del Proyecto
```
customer_churn_predictor/
│
├── data/
│ ├── raw/ # Datos crudos (ej: churn.csv)
│ ├── processed/ # Datos limpios/listos para modelado
│ └── external/ # Datos externos (si aplica)
│
├── notebooks/
│ └── 01_exploracion.ipynb # Exploración inicial del dataset
│
├── src/
│ ├── config.py # Rutas y parámetros globales
│ ├── data_preprocessing.py # Funciones para cargar y limpiar datos
│ └── ... (futuros módulos de modelado, evaluación, etc.)
│
├── logs/ # Logs del proyecto
├── requirements.txt # Dependencias del entorno
├── .gitignore # Archivos ignorados por git
└── README.md # Documentación del proyecto
```

---

## 🚀 Uso

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/<tu_usuario>/customer_churn_predictor.git
   cd customer_churn_predictor

2. **Crear entorno virtual e instalar dependencias**

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

    pip install -r requirements.txt

3. **Exploración inicial**

    Abrir el notebook
    ```bash
    jupyter notebook notebooks/01_exploracion.ipynb

## 📊 Datos

El dataset de churn se ubica en:
    ```data/raw/churn.csv```

## ⚠️ Nota importante:

Los datasets grandes o sensibles no se incluyen en este repositorio. Solo se mantiene un archivo de ejemplo ```churn.csv``` para propósitos de demostración.

---
## ✅ Estado Actual del Proyecto

* ☑️ Estructura inicial del proyecto

* ☑️ Configuración de entorno virtual y dependencias

* ☑️ Módulo de preprocesamiento de datos

* ☑️ Primer notebook de exploración

* ⬜ Modelado predictivo (pendiente)

* ⬜ Evaluación y visualización de resultados

* ⬜ Documentación avanzada con Sphinx

---
## 👨‍💻 Autor

Proyecto desarrollado por ```ramonguerraa``` , como parte de su portafolio de proyectos de ```Data Science & Analytics```.