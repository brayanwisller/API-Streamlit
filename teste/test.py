import streamlit as st
import pandas as pd
import numpy as np
import time
import random
import re
from st_on_hover_tabs import on_hover_tabs
from streamlit_autorefresh import st_autorefresh
# import streamlit_authenticator as stauth
# import sqlite3
# import yaml
# from yaml import SafeLoader

st.set_page_config(layout="wide")


st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

if "modo_escuro" not in st.session_state:
    st.session_state["modo_escuro"] = False

# Defina as cores dinâmicas antes do sidebar
modo_escuro = st.session_state["modo_escuro"]
navtab_bg = "#000000" if modo_escuro else "#2d72da"
icon_bg = "#000000" if modo_escuro else "#2d72da"
icon_color = "#FFFFFF"
background = "#606060" if modo_escuro else "#FFFFFF"
text = "#FFFFFF" if modo_escuro else "#000000"

with st.sidebar:
    tabs = on_hover_tabs(
        tabName=['Inicio', 'Teste', 'Gráfico', 'Feedback', 'Conta', 'Configurações'],
        iconName=['home', 'money', 'dashboard', 'feedback', 'account_circle', 'settings'],
        styles={
            'navtab': {
                'background-color': navtab_bg,
                'color': '#FFFFFF',
                'font-size': '18px',
                'transition': '.3s',
                'white-space': 'nowrap',
                'text-transform': 'uppercase',
            },
            'tabStyle': {':hover :hover': {'color': 'red', 'cursor': 'pointer'}},
            'tabStyle' : {'list-style-type': 'none',
                                                 'margin-bottom': '30px',
                                                 'padding-left': '30px'},
            'iconStyle': {
                'position': 'fixed',
                'left': '7.5px',
                'text-align': 'left',
                'background-color': icon_bg,
                'color': icon_color,
                'border-radius': '8px',
            },
        },
        key="1")

if tabs == "Configurações":
    st.title("Configurações")
    st.write("Modo Escuro")
    on = st.toggle("", value=st.session_state["modo_escuro"])
    st.session_state["modo_escuro"] = on
    if on:
        st.write("Modo escuro ativado.")
    else:
        st.write("Modo escuro desativado.")

    st_autorefresh(interval=500, key="autorefresh")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background} !important;
        color: {text} !important;
    }}
    section[data-testid="stSidebar"] {{
        background-color: {navtab_bg} !important;
        color: #FFFFFF !important;
    }}
    .on-hover-tab, .navtab, .stTabs [role="tab"] {{
        background-color: {navtab_bg} !important;
        color: #FFFFFF !important;
    }}
    .stButton>button {{
        background-color: #000000 !important;
        color: #FFFFFF;
    }}
    .stButton>button:hover {{
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border: none !important;
    }}
    .stButton>button:active,
    .stButton>button:focus,
    .stButton>button:visited {{
        background-color: #000000 !important;
        color: #FFFFFF !important;
        outline: none !important;
        border: none !important;
    }}
    .stButton>button:active {{
        background-color: #000000 !important;
    }}
    st.download_button {{
        background-color: #000000 !important;
        color: #FFFFFF;
    }}
    st.download_button:hover {{
        background-color: #000000 !important;
        color: #FFFFFF;
    }}
    .stTextInput>div>input {{
        background-color: {navtab_bg};
        color: #FFFFFF;
    }}
    .on-hover-tab i, .on-hover-tab svg, .on-hover-tab [class*="icon"], .navtab i, .navtab svg {{
        background-color: {icon_bg} !important;
        color: {icon_color} !important;
        border-radius: 8px !important;
    }}
    [data-testid="stToggle"] > label {{
        background-color: {navtab_bg} !important;
        color: #FFFFFF !important;
    }}
    st.write, st.subheader, st.header, st.title, {{
        color: {text} !important;
    }}
    st.toggle, st.selectbox, st.multiselect, st.text_input, st.text_area {{
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}

    .block-container {
        padding-top: 0rem; !important;
    }

    header {
        padding: 0rem; !important;
        margin: 0rem; !important;
        height: 0rem; !important;
        visibility: hidden;
    }
    [data-testid="stDecoration"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if tabs == "Inicio":

    st.title("Página Inicial")
    st.subheader("Seja bem vindo ao inicio")

    opcoes = st.selectbox(
            "Escolha uma opção abaixo",
            ("Teste 1", "Teste 2", "Teste 3"),
        )

    st.write("A opção escolhida foi: ", opcoes)

    st.divider()

    st.header("Dados Coletados")
    

    if st.button("Start"):
        col1, col2 = st.columns([3, 1])

        if "dados" not in st.session_state:
            st.session_state["dados"] = pd.DataFrame(
                np.random.randn(1, 1),
                columns=["Valores"]
            )

        dados = st.session_state["dados"]

        # progress_bar = st.sidebar.progress(0)
        # status_text = st.sidebar.empty()
        # last_row = np.random.randn(1, 1)
        # chart = st.line_chart(dados)


        with col1:
            if opcoes == "Teste 1":
                st.subheader("Teste 1")
                # for i in range(1, 101):
                    # new_rows = last_row[1, :] + np.random.randn(5, 1).cumsum(axis=0)
                    # status_text.text(f"{i}% completo")
                    # chart.add_rows(new_rows)
                    # progress_bar.progress(i)
                    # last_row = new_rows
                    # time.sleep(0.05)
                col1.line_chart(dados)
                col2.write(dados)
                
                # progress_bar.empty()

            elif opcoes == "Teste 2":
                st.subheader("Teste 2")
                col1.bar_chart(dados)
                col2.write(dados)
            elif opcoes == "Teste 3":
                st.subheader("Teste 3")     
                col1.area_chart(dados)
                col2.write(dados)

if tabs == "Teste":
    st.title("Página de Teste")
    st.subheader("Tabela de Avaliações")

    dataframes = pd.DataFrame(
    {
        "nome": ["Alex", "Diego", "Carlos"],
        "estrelas": [random.randint(0, 5) for _ in range(3)],
    }
    )

    st.dataframe(dataframes, 
            column_config={
                "nome": "Nome",
                "estrelas": st.column_config.NumberColumn(
                    "Avaliação",
                    help="Avaliações recebidas",
                    format="%d ⭐",
                ),
            },
            hide_index=True
            )
    
    st.divider()

    st.subheader("Formulário Teste")
    adicionar_selectbox = st.selectbox(
        "Escolha um metodo de contato",
        ("Email", "Celular", "Whatsapp")
    )
    st.write("O metodo escolhido foi: ", adicionar_selectbox)

    st.divider()

    st.subheader("Upload de Arquivos")
    upar_arquivos = st.file_uploader("Arquivo", accept_multiple_files=True)
    enviar = st.button("Enviar")

    if upar_arquivos and enviar:
        for upar_arquivo in upar_arquivos:
            dados = upar_arquivo.read()
            st.write("Nome do arquivo: ", upar_arquivo.name)
            if dados:
                st.write("Dados enviados")
            else:
                st.write("Ocorreu um erro ao enviar os dados")
    elif enviar:
        st.write("Nenhum arquivo selecionado para envio.")

    st.divider()

    st.subheader("Seção de Dados")

    @st.cache_data

    def carregar_dados():
        dataframe = np.random.randn(10, 10)
        dataframe = pd.DataFrame(dataframe, columns=[f"Coluna {i}" for i in range(1, 11)])
        st.table(dataframe)
        return dataframe

    @st.cache_data
    def converter_para_download(dataframe):
        return dataframe.to_csv().encode('utf-8')  
    
    dataframe = carregar_dados()
    csv = converter_para_download(dataframe)
    
    if st.button("Download dos Dados"):
        with st.spinner("Preparando download..."):
            time.sleep(2)
            st.download_button(
                label="Download CSV 📊",
                data=csv,
                file_name="dados.csv",
                mime="text/csv",
                key="download-csv",
            )

    

if tabs == "Gráfico":
    st.title("Gráficos")
    st.write("Grafico de Barras")

    if "grafico" not in st.session_state:
        st.session_state["grafico"] = pd.DataFrame(
            np.random.randn(10, 2),
            columns=["Teste 1", "Teste 2"],
        )
    
    grafico = st.session_state["grafico"]

    graf = grafico.copy()

    opcoes = ['Teste 1', 'Teste 2']
    selecionado = st.segmented_control(
        "Selecione uma opção", opcoes, selection_mode='single'
    )

    if selecionado == 'Teste 1':
        st.write("Você selecionou Teste 1")
        st.bar_chart(graf['Teste 1'], use_container_width=True, color="#317BEB")
    elif selecionado == 'Teste 2':
        st.write("Você selecionou Teste 2")
        st.bar_chart(graf['Teste 2'], use_container_width=True, color="#CC00FF")
    else:
        st.write("Nenhuma opção selecionada.")
        st.bar_chart(graf, use_container_width=True, color=["#317BEB", "#CC00FF"])
    st.divider()

if tabs == "Feedback":
    st.title("Feedback")
    st.write("Por favor, avalie nosso serviço:")

    feedback = ["Uma", "Duas", "Tres", "Quatro", "Cinco"]

    selecionado = st.feedback("stars")
    if selecionado is not None:
        st.write(f"Você selecionou: {feedback[selecionado]} estrelas.")

        if selecionado < 2:
            st.write("Lamentamos que nosso site não foi do seu agrado. Deixe um comentario sobre melhorias que podemos fazer!")
        else:
            st.write("Obrigado pelo seu feedback!")

        if selecionado < 4:
            resposta = st.text_input("Deixe um comentário:")
            if resposta:
                st.write("Seu comentário:", resposta)

if tabs == 'Conta':
    st.title("Sua Conta")

    @st.dialog("Login")

    def settings_dialog():
        st.write("Por favor, faça login para continuar.")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        email = st.text_input("Email", placeholder="@gmail.com")
        telefone = st.text_input("Telefone", placeholder="(11) 91234-5678")
        endereço = st.text_input("Endereço")

        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            entrar = st.button("Entrar")
        with col3:
            sair = st.button("Sair")

        if len(username) < 2:
            st.error("O nome de usuário não pode ser menor que 2 caracteres.")
            return
        
        if len(password) <= 7:
            st.error("A senha deve ter pelo menos 8 caracteres.")
            return
        
        if email and not email.endswith("@gmail.com"):
            st.error("O email deve ser do tipo @gmail.com")
            return
            
        telefone_regex = r"^\(\d{2}\) \d{9}$"
        if telefone and not re.match(telefone_regex, telefone):
            st.error("O telefone deve estar no formato (XX) XXXXX-XXXX.")
            return
            
        if entrar:
            if username and password and email and telefone and endereço:
                st.session_state['usuario_logado'] = username
                st.session_state['email'] = email
                st.session_state['telefone'] = telefone
                st.session_state['endereço'] = endereço
                st.success("Login bem-sucedido!")
            else:
                st.error("Por favor, preencha todos os campos.")

        if sair:
            if 'usuario_logado' in st.session_state:
                del st.session_state['usuario_logado']
                del st.session_state['email']
                del st.session_state['telefone']
                del st.session_state['endereço']
            st.success("Você saiu da sua conta.")
            st.stop()

    if 'usuario_logado' in st.session_state:
        st.subheader(f"Bem-vindo, {st.session_state['usuario_logado']}!")
        st.write("Aqui estão suas informações de conta:")
        st.write("Nome: ", st.session_state['usuario_logado'])
        st.write("Email: ", st.session_state.get('email'))
        st.write("Telefone: ", st.session_state.get('telefone'))
        st.write("Endereço: ", st.session_state.get('endereço'))

    st.write("Para atualizar suas informações, faça logout e faça login novamente com os novos dados.")

    if st.button("Login"):
        settings_dialog()

    if st.button("Logout"):
        if 'usuario_logado' in st.session_state:
            del st.session_state['usuario_logado']
            del st.session_state['email']
            del st.session_state['telefone']
            del st.session_state['endereço']
        st.success("Você saiu da sua conta.")
        st.stop()

    


    # with open("config.yaml") as file:
        #config = yaml.load(file, Loader=SafeLoader)

    # authenticator = stauth.Authenticate(
        # config['credentials'],
        # config['cookie']['name'],
        # config['cookie']['key'],
        # config['cookie']['expiry_days'],
        # config['preauthorized']
    # )

    # name, authentication_status, username = authenticator.login('Login', 'main')
    # if authentication_status:
        # authenticator.logout('Logout', 'main')
        # st.success(f"Bem-vindo {name}!")
        # st.write("Você está logado.")
    # elif authentication_status is False:
        # st.error("Nome de usuário ou senha incorretos.")
    # elif authentication_status is None:
        # st.warning("Por favor, faça login.")

