import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração da Página
st.set_page_config(page_title="G.U.I.M.E.L. os", page_icon="favicon.png", layout="centered")

# CSS para Tipografia Orbitron, Letras Minúsculas e Degradê
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    .stApp {
        background-color: #050505;
    }
    
    /* Título em degradê Laranja -> Amarelo -> Branco */
    .title-guimel {
        font-family: 'Orbitron', sans-serif;
        font-size: 42px;
        background: linear-gradient(to right, #FF4B2B, #FFB100, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        text-transform: lowercase;
        letter-spacing: 4px;
        margin-top: -10px;
    }

    .subtitle {
        font-family: 'Orbitron', sans-serif;
        color: #FFB100;
        text-align: center;
        font-size: 14px;
        text-transform: lowercase;
        letter-spacing: 2px;
        opacity: 0.8;
    }

    /* Remove fundos de blocos de imagem do Streamlit */
    [data-testid="stImage"] {
        background-color: transparent !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Brasão Centralizado (Usando o favicon.png como solicitado)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if os.path.exists("favicon.png"):
        # Mostra o favicon sem legendas ou bordas
        st.image("favicon.png", use_container_width=True)

# Texto de Identidade
st.markdown('<p class="title-guimel">λ g.u.i.m.e.l.</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">sistemas logísticos e teológicos online</p>', unsafe_allow_html=True)

# 3. Terminal Lateral
with st.sidebar:
    st.markdown("<h2 style='color:#FFB100; font-family:Orbitron; font-size:18px;'>terminal</h2>", unsafe_allow_html=True)
    api_key = st.text_input("chave de protocolo", type="password")
    st.markdown("<hr style='border: 0.5px solid #333;'>", unsafe_allow_html=True)

# 4. Lógica da IA (Modelo atualizado para 1.5-flash)
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        if "chat" not in st.session_state:
            st.session_state.chat = model.start_chat(history=[])
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(f"<span style='font-family:Orbitron; color:#eee;'>{msg['content']}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("comando, senhor?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
    except Exception as e:
        # Mensagem discreta de erro de conexão
        st.error(f"sistema em espera: aguardando protocolo google. ({e})")
else:
    st.markdown("<br><center><p style='color:#444; font-family:Orbitron; font-size:12px;'>conecte a chave para despertar o g.u.i.m.e.l.</p></center>", unsafe_allow_html=True)
