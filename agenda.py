import streamlit as st
import pandas as pd
from datetime import datetime

# ===== CONFIGURAÇÃO =====
st.set_page_config(page_title="Versatis Beauty", page_icon="💇‍♀️", layout="wide")

# ===== LOGIN =====
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="logo.jpeg" width="400">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<h1 style='text-align:center;color:#C71585;'>💇‍♀️ Versatis Beauty</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Seu salão de beleza com experiência única ✨☕</h3>", unsafe_allow_html=True)

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario == "admin" and senha == "1234":
            st.session_state["logged_in"] = True
            st.success("Login realizado com sucesso! 🎉")
        else:
            st.error("Usuário ou senha inválidos.")
    st.stop()

# ===== DADOS EM MEMÓRIA =====
if "clientes" not in st.session_state:
    st.session_state["clientes"] = pd.DataFrame(columns=["Nome", "Telefone", "Email"])

if "servicos" not in st.session_state:
    st.session_state["servicos"] = pd.DataFrame(columns=["Cliente", "Serviço", "Preço", "Data"])

if "estoque" not in st.session_state:
    st.session_state["estoque"] = pd.DataFrame(columns=["Produto", "Quantidade", "Preço Unitário"])

if "agenda" not in st.session_state:
    st.session_state["agenda"] = pd.DataFrame(columns=["Cliente", "Serviço", "Data", "Hora"])

if "financeiro" not in st.session_state:
    st.session_state["financeiro"] = pd.DataFrame(columns=["Data", "Descrição", "Valor"])

if "cupons" not in st.session_state:
    st.session_state["cupons"] = pd.DataFrame(columns=["Cliente", "Serviço", "Valor", "Data"])

# ===== MENU =====
menu = st.sidebar.radio(
    "Menu",
    ["Home", "Clientes", "Serviços", "Estoque", "Financeiro", "Agenda", "Cupom Fiscal"]
)


# ===== PÁGINAS =====
if menu == "Home":
    
    st.markdown("<h1 style='text-align:center;color:#C71585;'>Versatis Beauty</h1>", unsafe_allow_html=True)
    st.info("Selecione opções no menu lateral.")

elif menu == "Clientes":
    
    st.header("👩‍🦰 Cadastro de Clientes")
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    email = st.text_input("Email")
    if st.button("Salvar Cliente"):
        novo = pd.DataFrame([[nome, telefone, email]], columns=["Nome", "Telefone", "Email"])
        st.session_state["clientes"] = pd.concat([st.session_state["clientes"], novo], ignore_index=True)
        st.success("Cliente cadastrado com sucesso!")
    st.dataframe(st.session_state["clientes"])
    st.download_button("⬇️ Download Clientes", st.session_state["clientes"].to_csv(index=False), "clientes.csv")

elif menu == "Serviços":
    mostrar_logo()
    st.header("✂️ Registro de Serviços")
    lista_servicos = [
        "Corte", "Corte Masculino", "Escova", "Manicure", "Unha de Gel", "Spa", "Hidratação",
        "Peeling", "Pé e Mão", "Cílios", "Sobrancelha", "Dia da Noiva", "Dia da Mãe",
        "Facial", "Pintura", "Detox Capilar", "Mechas", "Barba", "Infantil Kids", "Outros Serviços"
    ]

    cliente = st.text_input("Nome do Cliente")
    servico = st.selectbox("Serviço", lista_servicos)
    preco = st.number_input("Preço (R$)", min_value=50.0, step=10.0)

    if st.button("Registrar Serviço"):
        novo = pd.DataFrame([[cliente, servico, preco, datetime.now().strftime("%Y-%m-%d %H:%M")]],
                            columns=["Cliente", "Serviço", "Preço", "Data"])
        st.session_state["servicos"] = pd.concat([st.session_state["servicos"], novo], ignore_index=True)
        st.success("Serviço registrado com sucesso!")

    st.dataframe(st.session_state["servicos"])
    st.download_button("⬇️ Download Serviços", st.session_state["servicos"].to_csv(index=False), "servicos.csv")

elif menu == "Estoque":
    mostrar_logo()
    st.header("📦 Gestão de Estoque")
    produto = st.text_input("Produto")
    quantidade = st.number_input("Quantidade", min_value=0)
    preco_unit = st.number_input("Preço Unitário", min_value=0.0)
    if st.button("Adicionar Produto"):
        novo = pd.DataFrame([[produto, quantidade, preco_unit]], columns=["Produto", "Quantidade", "Preço Unitário"])
        st.session_state["estoque"] = pd.concat([st.session_state["estoque"], novo], ignore_index=True)
        st.success("Produto adicionado ao estoque!")
    st.dataframe(st.session_state["estoque"])
    st.download_button("⬇️ Download Estoque", st.session_state["estoque"].to_csv(index=False), "estoque.csv")

elif menu == "Financeiro":
    mostrar_logo()
    st.header("📊 Controle Financeiro")
    descricao = st.text_input("Descrição")
    valor = st.number_input("Valor (R$)", min_value=0.0)
    if st.button("Registrar Movimento"):
        novo = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), descricao, valor]], columns=["Data", "Descrição", "Valor"])
        st.session_state["financeiro"] = pd.concat([st.session_state["financeiro"], novo], ignore_index=True)
        st.success("Movimento financeiro registrado!")
    st.dataframe(st.session_state["financeiro"])
    st.download_button("⬇️ Download Financeiro", st.session_state["financeiro"].to_csv(index=False), "financeiro.csv")

elif menu == "Agenda":
    mostrar_logo()
    st.header("📅 Agenda de Serviços")
    cliente = st.text_input("Cliente")
    servico = st.text_input("Serviço")
    data = st.date_input("Data")
    hora = st.time_input("Hora")
    if st.button("Agendar"):
        novo = pd.DataFrame([[cliente, servico, str(data), str(hora)]], columns=["Cliente", "Serviço", "Data", "Hora"])
        st.session_state["agenda"] = pd.concat([st.session_state["agenda"], novo], ignore_index=True)
        st.success("Agendamento realizado!")
    st.dataframe(st.session_state["agenda"])
    st.download_button("⬇️ Download Agenda", st.session_state["agenda"].to_csv(index=False), "agenda.csv")

elif menu == "Cupom Fiscal":
    mostrar_logo()
    st.header("🧾 Emissão de Cupom Fiscal")
    cliente = st.text_input("Cliente")
    servico = st.text_input("Serviço")
    preco = st.number_input("Valor do serviço (R$)", min_value=50.0, step=10.0)
    data_cupom = st.date_input("Data da emissão", value=datetime.today())

    if st.button("Emitir Cupom Fiscal"):
        cupom = pd.DataFrame([[cliente, servico, preco, str(data_cupom)]],
                             columns=["Cliente", "Serviço", "Valor", "Data"])
        st.session_state["cupons"] = pd.concat([st.session_state["cupons"], cupom], ignore_index=True)
        st.success("Cupom fiscal emitido com sucesso! 🎉")

    st.dataframe(st.session_state["cupons"])
    st.download_button("⬇️ Download Cupons", st.session_state["cupons"].to_csv(index=False), "cupons.csv")