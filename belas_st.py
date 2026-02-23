import streamlit as st
import pandas as pd
from datetime import datetime
##from streamlit_option_menu import option_menu
##from streamlit_fullcalendar import calendar

# Configuração inicial
st.set_page_config(page_title="Belas Hair", page_icon="💇‍♀️", layout="wide")

# ===== HOME =====
st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#C71585;">💇‍♀️ Belas Hair</h1>
        <h3>Seu salão de beleza com experiência única ✨☕</h3>
        <img src="https://cdn-icons-png.flaticon.com/512/2920/2920322.png" width="120">
    </div>
    """,
    unsafe_allow_html=True
)

# ===== SIDEBAR =====
menu = st.sidebar.radio(
    "Menu",
    ["Home", "Clientes", "Serviços", "Estoque", "Financeiro", "Agenda"]
  ##  icons=["🏠", "👤", "✂️", "📦", "📊", "📅"]
)

# ===== DATA STORAGE (em memória) =====
if "clientes" not in st.session_state:
    st.session_state["clientes"] = pd.DataFrame(columns=["Nome", "Telefone", "Email"])

if "servicos" not in st.session_state:
    st.session_state["servicos"] = pd.DataFrame(columns=["Cliente", "Serviço", "Preço", "Data"])

if "estoque" not in st.session_state:
    st.session_state["estoque"] = pd.DataFrame(columns=["Produto", "Quantidade", "Preço Unitário"])

if "agenda" not in st.session_state:
    st.session_state["agenda"] = pd.DataFrame(columns=["Cliente", "Serviço", "Data", "Hora"])

# ===== LISTA DE SERVIÇOS =====
lista_servicos = [
    "Corte - R$70",
    "Corte Masculino - R$50",
    "Escova - R$180",
    "Manicure - R$30",
    "Unha de Gel - R$100",
    "Spa - R$250",
    "Hidratação - R$120",
    "Peeling - R$200",
    "Pé e Mão - R$80",
    "Cílios - R$150",
    "Sobrancelha - R$60",
    "Dia da Noiva - R$1200",
    "Dia da Mãe - R$800",
    "Facial - R$180",
    "Pintura - R$300",
    "Detox Capilar - R$220",
    "Mechas - R$400",
    "Barba - R$70",
    "Infantil Kids - R$90",
    "Outros Serviços - preço variável"
]

# ===== PÁGINAS =====
if menu == "Home":
    st.subheader("Bem-vindo ao sistema Belas Hair 💇‍♀️")
    st.info("Use o menu lateral para navegar entre as funções do sistema.")

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
    st.header("✂️ Registro de Serviços")
    cliente = st.text_input("Nome do Cliente")
    servico = st.selectbox("Serviço", lista_servicos)
    preco = float(servico.split("R$")[-1]) if "R$" in servico else 0.0
    if st.button("Registrar Serviço"):
        novo = pd.DataFrame([[cliente, servico, preco, datetime.now().strftime("%Y-%m-%d %H:%M")]],
                            columns=["Cliente", "Serviço", "Preço", "Data"])
        st.session_state["servicos"] = pd.concat([st.session_state["servicos"], novo], ignore_index=True)
        st.success("Serviço registrado com sucesso!")
    st.dataframe(st.session_state["servicos"])
    st.download_button("⬇️ Download Serviços", st.session_state["servicos"].to_csv(index=False), "servicos.csv")

elif menu == "Estoque":
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
    st.header("📊 Indicadores Financeiros")
    if not st.session_state["servicos"].empty:
        receita_total = st.session_state["servicos"]["Preço"].sum()
        st.metric("Receita Total", f"R$ {receita_total:.2f}")
        st.bar_chart(st.session_state["servicos"].groupby("Serviço")["Preço"].sum())
    else:
        st.info("Nenhum serviço registrado ainda.")

elif menu == "Agenda":
    st.header("📅 Agenda de Reservas")
    cliente = st.text_input("Nome do Cliente")
    servico = st.selectbox("Serviço", lista_servicos)
    data_reserva = st.date_input("Data")
    hora_reserva = st.time_input("Hora")
    if st.button("Confirmar Reserva"):
        novo = pd.DataFrame([[cliente, servico, str(data_reserva), str(hora_reserva)]],
                            columns=["Cliente", "Serviço", "Data", "Hora"])
        st.session_state["agenda"] = pd.concat([st.session_state["agenda"], novo], ignore_index=True)
        st.success("Reserva confirmada com sucesso! 🎉")

    st.dataframe(st.session_state["agenda"])
    st.download_button("⬇️ Download Agenda", st.session_state["agenda"].to_csv(index=False), "agenda.csv")

    # Exibir calendário visual
    events = [{"title": f"{row['Serviço']} - {row['Cliente']}", "start": f"{row['Data']}T{row['Hora']}"}
              for _, row in st.session_state["agenda"].iterrows()]
    if events:
        calendar(events=events)
