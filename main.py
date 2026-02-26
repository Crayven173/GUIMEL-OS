import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração da Página (Favicon na aba do navegador)
st.set_page_config(page_title="g.u.i.m.e.l. os", page_icon="favicon.png", layout="centered")

# CSS Estilizado: Letras minúsculas, Orbitron e Degradê Vibrante
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
        margin-top: 10px;
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
    </style>
    """, unsafe_allow_html=True)

# 2. Centralização do Ícone (Usando favicon.png como logo central)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if os.path.exists("favicon.png"):
        st.image("favicon.png", use_container_width=True)
    
st.markdown('<p class="title-guimel">λ g.u.i.m.e.l.</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">sistemas logísticos e teológicos online</p>', unsafe_allow_html=True)

# 3. Terminal Lateral
with st.sidebar:
    st.markdown("<h2 style='color:#FFB100; font-family:Orbitron; font-size:18px;'>terminal</h2>", unsafe_allow_html=True)
    api_key = st.text_input("chave de protocolo", type="password")
    if not api_key:
        st.info("aguardando conexão...")

# 4. Processamento de Resposta
if api_key:
    try:
        genai.configure(api_key=api_key)
        # Usando a versão estável para evitar erros de versão
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
        st.error(f"sistema offline: aguardando liberação da chave google. (erro: {e})")
else:
    st.markdown("<br><center><p style='color:#555;'>conecte a chave para despertar o sistema.</p></center>", unsafe_allow_html=True)
