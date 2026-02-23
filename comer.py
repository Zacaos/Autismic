import streamlit as st
import pandas as pd

# Definição de recursos e meses
recursos = ["Cluster GKE", "Big Table", "Cloud Composer", 
            "Applications (nulls)", "Notebooks EDA", 
            "Big Query", "Cloud Storage"]

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", 
         "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

# Criação de dataframe vazio
df = pd.DataFrame(index=recursos, columns=meses)

st.title("Relatório Forecast - Cost Manager")

# Input manual dos custos
for recurso in recursos:
    for mes in meses:
        valor = st.text_input(f"Custo {recurso} - {mes}", "0")
        df.loc[recurso, mes] = float(valor)

# Cálculo de médias trimestrais
trimestres = {
    "Q1": ["Jan", "Fev", "Mar"],
    "Q2": ["Abr", "Mai", "Jun"],
    "Q3": ["Jul", "Ago", "Set"],
    "Q4": ["Out", "Nov", "Dez"]
}

for q, meses_q in trimestres.items():
    df[q] = df[meses_q].astype(float).mean(axis=1)

# Ajustes de uso compartilhado
df.loc["Big Table"] = df.loc["Big Table"].astype(float) * (1/3)
df.loc["Cluster GKE"] = df.loc["Cluster GKE"].astype(float) * (1/2)

# Exportação CSV
csv = df.to_csv().encode("utf-8")
st.download_button("Baixar Relatório CSV", csv, "forecast_cost_manager.csv", "text/csv")