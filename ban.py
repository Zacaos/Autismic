import streamlit as st
import time

st.set_page_config(page_title="Ir no banheiro", page_icon="🚽", layout="centered")

st.title("Pedir para ir no banheiro!")

# Estilo para botão grande
st.markdown("""
    <style>
    div.stButton > button {
        height: 3em;
        width: 100%;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        margin: 1em 0;
    }
    </style>
""", unsafe_allow_html=True)

# Função para animar "Ir no banheiro" subindo
def animar_oi():
    st.markdown("Muito bem, vamos ao banheiro...")
    placeholder = st.empty()
    for i in range(10, 0, -1):
        placeholder.markdown(f"<h1 style='text-align:center; color:rgb({255-i*20},{i*20},255); font-size:{30+i*5}px;'>Vamos ao Banheiro 🚽</h1>", unsafe_allow_html=True)
        time.sleep(0.1)
    placeholder.markdown("<h1 style='text-align:center; color:#FF69B4; font-size:60px;'>🚽Vamos ao Banheiro</h1>", unsafe_allow_html=True)
    st.success("Muito bem Parabéns! 🌈")

# Botão para acionar a animação
if st.button("Ir no banheiro 🚽"):
    animar_oi()
