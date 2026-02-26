import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração da Página e Fontes Digitais
st.set_page_config(page_title="G.U.I.M.E.L. OS", page_icon="ג", layout="centered")

# CSS Avançado para Cores e Estilo
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');

    .stApp {
        background-color: #050505;
    }
    
    /* Título G.U.I.M.E.L com degradê Laranja/Amarelo/Branco */
    .title-guimel {
        font-family: 'Orbitron', sans-serif;
        font-size: 55px;
        font-weight: bold;
        background: linear-gradient(to right, #FF4B2B, #FFB100, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: -10px;
        letter-spacing: 5px;
    }

    /* Subtítulo com fonte tecnológica */
    .subtitle {
        font-family: 'Rajdhani', sans-serif;
        color: #FFB100;
        text-align: center;
        font-size: 20px;
        font-weight: 300;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Estilização das mensagens e inputs */
    .stChatMessage {
        border-radius: 15px;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Área do Logo (Removendo molduras da imagem)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists("logo.png"):
        # O parâmetro 'use_container_width' mantém a proporção original
        st.image("logo.png", use_container_width=True)
    
    # Texto do Logo com as cores solicitadas
    st.markdown('<p class="title-guimel">ג G.U.I.M.E.L.</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sistemas Logísticos e Teológicos Online</p>', unsafe_allow_html=True)

# 3. Barra Lateral
with st.sidebar:
    st.markdown("<h2 style='color:#FFB100; font-family:Orbitron;'>TERMINAL</h2>", unsafe_allow_html=True)
    api_key = st.text_input("Chave de Protocolo", type="password")
    st.info("Aguardando autorização do servidor central...")

# 4. Lógica da IA (Mantendo o modelo estável)
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.0-pro")
        
        if "chat" not in st.session_state:
            st.session_state.chat = model.start_chat(history=[])
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Comando, Senhor?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
    except Exception as e:
        st.error(f"STATUS: Protocolo negado pelo google, aguarde o prazo de segurança. (Erro: {e})")
else:
    st.warning("Senhor, conecte a chave para iniciar.")
    
