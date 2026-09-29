import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Configuration
st.set_page_config(page_title="Dashboard Prévision des Ventes", page_icon="📦", layout="wide")

st.title("📦 Tableau de Bord : Prévision des Ventes et Stocks")
st.markdown("Cette application utilise l'intelligence artificielle (modèle **Prophet**) pour anticiper les ventes futures et vous aider à gérer vos stocks.")

@st.cache_data
def load_and_train_model():
    # Chargement
    df = pd.read_csv('../data/store_sales.csv')
    df = df.rename(columns={'Date': 'ds', 'Sales': 'y'})
    df['ds'] = pd.to_datetime(df['ds'])
    
    # Entraînement de Prophet (rapide)
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
    model.fit(df)
    
    return model, df

model, df = load_and_train_model()

# Interface utilisateur
st.sidebar.header("Paramètres de Prévision")
jours_futurs = st.sidebar.slider("Combien de jours souhaitez-vous anticiper ?", min_value=7, max_value=180, value=30, step=7)

st.subheader(f"🔮 Prévision des ventes pour les {jours_futurs} prochains jours")

# Génération du futur
future = model.make_future_dataframe(periods=jours_futurs)
forecast = model.predict(future)

# Graphique interactif (Prophet a une méthode intégrée pour Streamlit/Plotly mais on va utiliser le basique)
fig1 = model.plot(forecast)
plt.title(f"Historique et Prévisions (Zoom sur la fin)")
plt.xlim(pd.Timestamp('2022-06-01'), forecast['ds'].max()) # On zoom sur les 6 derniers mois + futur
st.pyplot(fig1)

# Extraction des données futures uniquement
futur_uniquement = forecast.tail(jours_futurs)
total_ventes_prevues = int(futur_uniquement['yhat'].sum())
moyenne_journaliere = int(futur_uniquement['yhat'].mean())
pic_max = int(futur_uniquement['yhat'].max())

# Affichage des métriques clés
st.markdown("---")
st.subheader("📊 Recommandations Logistiques pour cette période")

col1, col2, col3 = st.columns(3)
col1.metric("📦 Volume Total à prévoir", f"{total_ventes_prevues} articles", "Demande globale")
col2.metric("🚚 Rythme d'expédition", f"{moyenne_journaliere} articles / jour", "Cadence moyenne")
col3.metric("🚨 Journée critique (Pic)", f"{pic_max} articles", "Stock de sécurité max")

st.info(f"💡 **Conseil** : Prévoyez un stock tampon d'au moins **{pic_max + 25} unités** (Pic maximum + Marge d'erreur de 25) pour éviter toute rupture lors de la journée la plus chargée de cette période.")

st.markdown("### Détail des prévisions journalières")
st.dataframe(futur_uniquement[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].rename(
    columns={'ds': 'Date', 'yhat': 'Prévision', 'yhat_lower': 'Minimum estimé', 'yhat_upper': 'Maximum estimé'}
).set_index('Date').round(0))
