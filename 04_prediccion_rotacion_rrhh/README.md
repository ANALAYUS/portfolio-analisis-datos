# 📊 Proyecto: Predicción de Rotación de Personal (HR Attrition)

## 1. El Reto de Negocio 🏢
La rotación no deseada de empleados representa un costo altísimo para las empresas en términos de tiempo, capacitación y pérdida de talento clave. El objetivo de este proyecto fue dejar de reaccionar tarde a las renuncias y **adelantarnos con datos**, respondiendo a la pregunta central: *¿Qué factores impulsan realmente a un colaborador a dejar la organización?*

## 2. El Enfoque y Análisis 🔍
Utilizando un dataset de recursos humanos, implementé un flujo completo de Ciencia de Datos:
* **Limpieza y Preparación:** Tratamiento de variables categóricas, codificación y escalado de datos para preparar el terreno de Machine Learning.
* **Modelo Predictivo:** Entrené un modelo de **Regresión Logística** optimizado con `Scikit-Learn`, utilizando la técnica de balanceo de clases (`class_weight='balanced'`) para asegurar que el modelo detectara con precisión tanto a quienes se quedan como a quienes se van.

## 3. Hallazgos Clave (*Feature Importance*) 💡
Gracias a la interpretabilidad de los coeficientes del modelo, descubrimos que los principales factores que aumentan la probabilidad de rotación no son solo económicos, sino operativos y de estilo de vida laboral:
* **Horas Extra:** El exceso de horas extra encabeza la lista como uno de los detonantes más fuertes de renuncia.
* **Viajes de Negocio:** La alta frecuencia de viajes también correlaciona directamente con el desgaste y la salida de personal.

## 4. Valor para la Toma de Decisiones 🚀
Este modelo le permite al departamento de Recursos Humanos pasar de un enfoque reactivo a uno **preventivo**. Al identificar perfiles en "zona de riesgo", la compañía puede intervenir a tiempo ofreciendo planes de retención, mejorando la distribución de cargas de trabajo o ajustando políticas de viajes antes de que sea demasiado tarde.

<img width="675" height="387" alt="image" src="https://github.com/user-attachments/assets/72cc9fdb-a665-4888-840c-08f783922dec" />
