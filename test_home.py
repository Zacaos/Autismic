import streamlit as st
import datetime

st.set_page_config(page_title="Versatis Hair - Agendamento", page_icon="💇‍♀️")

st.title("💇‍♀️ Versatis Hair - Agendamento Online")
st.write("Agende seu horário de forma rápida e prática!")

# Lista de serviços
servicos = ["Corte", "Escova", "Coloração", "Hidratação", "Progressiva"]
servico = st.selectbox("Escolha o serviço:", servicos)

# Seleção de data e hora
data = st.date_input("Selecione a data:", min_value=datetime.date.today())
hora = st.time_input("Selecione o horário:")

# Nome do cliente
nome = st.text_input("Seu nome:")

# Botão de agendamento
if st.button("Confirmar Agendamento"):
    if nome and servico and data and hora:
        mensagem = f"Olá, meu nome é {nome}. Gostaria de agendar {servico} no dia {data.strftime('%d/%m/%Y')} às {hora.strftime('%H:%M')}."
        numero_whatsapp = "5511959529328"  # Substitua pelo número da loja com DDD
        link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensagem.replace(' ', '+')}"
        
        st.success("Agendamento criado com sucesso!")
        st.markdown(f"[📲 Confirmar pelo WhatsApp]({link_whatsapp})", unsafe_allow_html=True)
    else:
        st.warning("Por favor, preencha todas as informações antes de confirmar.")