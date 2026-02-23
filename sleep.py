import streamlit as st
import os

st.title("💤 Hora de Dormir")
st.write("Escolha em quanto tempo deseja desligar o computador:")

# Opções de tempo em minutos
opcoes = {
    "10 minutos": 10,
    "20 minutos": 20,
    "30 minutos": 30
}

# Seleção pelo usuário
escolha = st.radio("Tempo para desligar:", list(opcoes.keys()))

if st.button("Agendar Desligamento"):
    minutos = opcoes[escolha]
    segundos = minutos * 60
    comando = f"shutdown -s -t {segundos}"
    
    # Executa o comando no Windows
    os.system(comando)
    
    st.success(f"Computador será desligado em {minutos} minutos.")

# Botão para cancelar desligamento
if st.button("Cancelar Desligamento"):
    os.system("shutdown -a")
    st.info("Desligamento cancelado.")
