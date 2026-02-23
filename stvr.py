import streamlit as st

# Sidebar
st.sidebar.title("Versatis Hair")
menu = st.sidebar.radio("Navegação", ["Login", "Agenda", "Financeiro", "Produtos", "Precificação"])

# Login
if menu == "Login":
    st.title("Login")
    user = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        st.success(f"Bem-vindo {user}!")

# Agenda
elif menu == "Agenda":
    st.title("Agenda de Serviços")
    st.date_input("Data")
    st.text_input("Cliente")
    st.selectbox("Serviço", ["Corte", "Escova", "Tintura"])
    st.button("Agendar")

# Financeiro
elif menu == "Financeiro":
    st.title("Controle Financeiro")
    st.metric("Entradas", "R$ 5.000")
    st.metric("Saídas", "R$ 2.000")
    st.metric("Lucro", "R$ 3.000")

# Produtos
elif menu == "Produtos":
    st.title("Cadastro de Produtos")
    st.text_input("Nome do Produto")
    st.number_input("Preço", min_value=0.0)
    st.number_input("Estoque", min_value=0)
    st.button("Salvar")

# Precificação
elif menu == "Precificação":
    st.title("Precificação de Serviços")
    servico = st.selectbox("Serviço", ["Corte Masculino", "Corte Feminino", "Escova", "Tintura"])
    custo = st.number_input("Custo", min_value=0.0)
    margem = st.slider("Margem de Lucro (%)", 0, 100, 30)
    preco_final = custo * (1 + margem/100)
    st.write(f"Preço sugerido: R$ {preco_final:.2f}")
