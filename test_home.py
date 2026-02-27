import streamlit as st

st.set_page_config(page_title="Versatis Hair", layout="centered")

st.title("💇‍♀️ Versatis Hair")
st.write("Bem-vindo(a)! Confira nossos serviços e agende pelo WhatsApp.")

# Lista de serviços
servicos = [
    "✂️ Corte",
    "💅 Manicure",
    "🎨 Tintura",
    "✨ Luzes",
    "🌸 Face Design"
]

# Slide/carrossel simples
st.subheader("Nossos Serviços")
for servico in servicos:
    st.image("https://via.placeholder.com/600x300?text=" + servico, caption=servico)

# Botão para WhatsApp
numero_whatsapp = "5511999999999"  # coloque aqui o número da loja
mensagem_padrao = "Olá, gostaria de agendar um horário na Versace Hair."
link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensagem_padrao.replace(' ', '%20')}"

st.markdown(f"[📲 Agendar pelo WhatsApp]({link_whatsapp})", unsafe_allow_html=True)