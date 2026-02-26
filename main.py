import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração da Página
st.set_page_config(page_title="G.U.I.M.E.L. OS", page_icon="logo.png", layout="centered")

# CSS: Camuflagem Total, Fonte Futurista e Letras MAIÚSCULAS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    .stApp {
        background-color: #000000;
    }
    
    .title-container {
        text-align: center;
        margin-top: -30px;
    }

    .title-guimel {
        font-family: 'Orbitron', sans-serif;
        font-size: 45px;
        font-weight: 700;
        background: linear-gradient(to right, #FF4B2B, #FFB100, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: uppercase;
        letter-spacing: 6px;
        margin-bottom: 0px;
    }

    .subtitle {
        font-family: 'Orbitron', sans-serif;
        color: #FFB100;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 3px;
        opacity: 0.8;
    }

    [data-testid="stImage"] img {
        border: none !important;
        box-shadow: none !important;
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Brasão Central
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)

st.markdown("""
    <div class="title-container">
        <p class="title-guimel">λ G.U.I.M.E.L.</p>
        <p class="subtitle">SISTEMAS LOGÍSTICOS E TEOLÓGICOS ONLINE</p>
    </div>
    """, unsafe_allow_html=True)

# 3. Terminal na Sidebar
with st.sidebar:
    st.markdown("<h2 style='color:#FFB100; font-family:Orbitron; font-size:18px;'>TERMINAL</h2>", unsafe_allow_html=True)
    api_key = st.text_input("CHAVE DE PROTOCOLO", type="password")

# 4. Motor de IA: Protocolo de Segurança Gemini-Pro
if api_key:
    try:
        genai.configure(api_key=api_key)
        # Trocando para o gemini-pro que possui maior compatibilidade
        model = genai.GenerativeModel("gemini-pro")
        
        if "chat" not in st.session_state:
            st.session_state.chat = model.start_chat(history=[])
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(f"<span style='font-family:Orbitron; color:#eee;'>{msg['content'].upper()}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("COMANDO, SENHOR?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt.upper())
            
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text.upper())
                
    except Exception as e:
        st.error(f"SISTEMA EM STANDBY: FALHA DE AUTENTICAÇÃO NO NÚCLEO. (ERRO: {e})")
else:
    st.markdown("<br><center><p style='color:#333; font-family:Orbitron; font-size:10px;'>INSIRA A CHAVE PARA DESPERTAR O SISTEMA.</p></center>", unsafe_allow_html=True)
