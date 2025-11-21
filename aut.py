import streamlit as st
import time

st.set_page_config(page_title="Balões de Parabéns", page_icon="🎈", layout="centered")

st.title("🎈 Solte seus balões de comemoração!")

# Estilo para botões grandes
st.markdown("""
    <style>
    div.stButton > button {
        height: 3em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        margin: 0.5em 0;
    }
    </style>
""", unsafe_allow_html=True)

# Função para simular balões por cor
def soltar_balao(cor_nome, emoji_cor, emoji_balao):
    st.markdown(f"## {emoji_balao} Subindo balões {cor_nome}...")
    with st.empty():
        for i in range(10):
            st.markdown(f"<h1 style='text-align: center;'>{emoji_balao * (i % 5 + 1)}</h1>", unsafe_allow_html=True)
            time.sleep(0.1)
    st.success(f"🎉 Parabéns! Você soltou balões {cor_nome.upper()} {emoji_cor}")

# Layout dos botões por cor
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    if st.button("🔵 Soltar Azul"):
        soltar_balao("azuis", "💙", "🔵")

with col2:
    if st.button("🔴 Soltar Vermelho"):
        soltar_balao("vermelhos", "❤️", "🔴")

with col3:
    if st.button("🟢 Soltar Verde"):
        soltar_balao("verdes", "💚", "🟢")

with col4:
    if st.button("🟡 Soltar Amarelo"):
        soltar_balao("amarelos", "💛", "🟡")

# Botão para soltar todos os balões com st.balloons()
st.markdown("---")
if st.button("🎊 Soltar Todos os Balões"):
    st.balloons()
    st.success("🎉 Parabéns! Todos os balões foram soltos com sucesso!")