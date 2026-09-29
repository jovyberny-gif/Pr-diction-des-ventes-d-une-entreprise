# 📈 Prédiction des Ventes d'une Entreprise (Time Series Forecasting)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Prophet](https://img.shields.io/badge/Prophet-Meta%20AI-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)

## 📌 À propos du projet
Ce projet s'attaque à un défi logistique et financier majeur dans le secteur du commerce : l'optimisation et la gestion des stocks. 
En analysant 3 années d'historique de ventes, l'objectif est d'identifier les tendances de croissance et les fortes variations saisonnières pour anticiper la demande future. 

Grâce à l'algorithme **Prophet** (développé par l'équipe Data Science de Meta), nous prédisons les ventes futures et traduisons ces chiffres en **recommandations métiers concrètes** (stock de sécurité, pics critiques, rythme d'expédition) via un Tableau de Bord (Dashboard) interactif.

## 🚀 Fonctionnalités
- **Génération de données réalistes** : Script python simulant 3 ans d'activité avec tendance, bruit, et saisonnalité annuelle/hebdomadaire.
- **Analyse Exploratoire (EDA)** : Décomposition des séries temporelles (Trend, Seasonality, Residuals) avec `statsmodels`.
- **Modélisation Avancée** : Prédiction algorithmique avec Prophet et analyse de l'erreur absolue moyenne (MAE).
- **Interface Logistique (Dashboard)** : Application Streamlit pour générer les recommandations de gestion des stocks en temps réel selon une fenêtre temporelle choisie.

## 📂 Structure du Projet

```text
sales_prediction/
│
├── app/
│   └── app.py                  # Tableau de Bord interactif (Streamlit)
│
├── data/
│   └── store_sales.csv         # Le jeu de données généré (ventes quotidiennes)
│
├── notebooks/
│   ├── 01_EDA_and_Trends.ipynb # Notebook : Moyennes glissantes et décomposition
│   └── 02_Modeling_Prophet.ipynb # Notebook : Entraînement et prédictions Prophet
│
├── generate_data.py            # Script de génération du dataset initial
├── requirements.txt            # Liste des dépendances Python
└── README.md                   # Ce fichier
```

## 💻 Installation et Utilisation en Local

### 1. Cloner le dépôt
```bash
git clone https://github.com/jovyberny-gif/Pr-diction-des-ventes-d-une-entreprise.git
cd Pr-diction-des-ventes-d-une-entreprise
```

### 2. Créer un environnement virtuel (Recommandé)
```bash
python -m venv venv
# Sur Windows :
venv\Scripts\activate
# Sur Mac/Linux :
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Régénérer le jeu de données (Optionnel)
```bash
python generate_data.py
```

### 5. Lancer l'Application Web (Dashboard)
Naviguez dans le dossier `app/` et lancez l'application Streamlit :
```bash
cd app
python -m streamlit run app.py
```
L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`.
