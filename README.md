📊 NLP Feedback Classification Framework
Survey Analytics + Text Mining + Performance Scoring



🇪🇸 Descripción (Español)

Sistema replicable de NLP + Survey Analytics diseñado para analizar feedback textual combinado con escalas Likert, generando:

Clasificación binaria (Riesgo vs OK)

Clasificación multiclase (Negativo / Neutral / Positivo)

Índice de desempeño normalizado (0–100)

Agregaciones listas para Power BI / Looker

Interpretabilidad del modelo (tokens con mayor peso)

Este framework permite integrar datos estructurados y no estructurados en un sistema analítico escalable.

🎯 Objetivos del Proyecto

Integrar texto libre + escalas cuantitativas.

Detectar señales tempranas de deterioro.

Construir un score comparable entre períodos o entidades.

Diseñar un pipeline replicable para distintos contextos (Educación, Energía, RRHH, Customer Experience).

🧠 Modelado

TF-IDF Vectorization

Logistic Regression

class_weight balancing

Threshold tuning

SMOTE (opcional)

Evaluación con:

Accuracy

Precision / Recall

F1 Score

Confusion Matrix

📈 Survey Analytics

Escala Likert transformada a índice 0–100:

1 → 0
2 → 25
3 → 50
4 → 75
5 → 100

Score global = combinación ponderada de:

Índice Likert

Predicción de sentimiento textual

📊 Dashboard Ready Output

El sistema genera datasets agregados por:

Curso

Docente

Período

Nivel de riesgo

Listos para exportar a Power BI / Looker.

🔎 Interpretabilidad

Se extraen los tokens con mayor peso por clase para:

Transparencia

Auditoría del modelo

Identificación de patrones reales

⚖ Ética y Buenas Prácticas

Anonimización de datos

No uso para decisiones punitivas

Uso como herramienta de mejora continua


----------------------------------------------------------------------------------------------------------------------

🇬🇧 English Version
Project Overview

Replicable NLP + Survey Analytics framework designed to analyze textual feedback combined with Likert scales, generating:

Binary classification (Risk vs OK)

Multiclass sentiment classification

0–100 performance index

Dashboard-ready aggregations

Model interpretability (top weighted tokens)

Business Value

Early risk detection

Performance scoring

Scalable analytics framework

Hybrid structured + unstructured data integration

Tech Stack

Python

Scikit-learn

Pandas

TF-IDF

Logistic Regression

Imbalanced handling strategies

📂 Repository Structure
nlp-feedback-classification/
│
├── data/
│   └── sample_feedback.csv
│
├── notebooks/
│   └── nlp_feedback_modeling_framework.ipynb
│
├── README.md
├── LICENSE
└── requirements.txt

🚀 Potential Applications

Education performance analytics

Employee feedback analysis

Energy workforce evaluation

Customer satisfaction modeling

Operational sentiment monitoring

---

Author: David Parales  
Energy & Data Analytics
