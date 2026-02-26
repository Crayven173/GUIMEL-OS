import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração da Página
st.set_page_config(page_title="g.u.i.m.e.l. os", page_icon="logo.png", layout="centered")

# CSS para Camuflagem Total, Fonte Futurista e Degradê Vibrante
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    /* Fundo preto absoluto para camuflar o logo.png */
    .stApp {
        background-color: #000000;
    }
    
    /* Container do Título */
    .title-container {
        text-align: center;
        margin-top: -20px;
    }

    /* Título com o degradê da penúltima tentativa */
    .title-guimel {
        font-family: 'Orbitron', sans-serif;
        font-size: 42px;
        background: linear-gradient(to right, #FF4B2B, #FFB100, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: lowercase;
        letter-spacing: 4px;
        margin-bottom: 0px;
    }

    /* Subtítulo em Amarelo/Laranja suave */
    .subtitle {
        font-family: 'Orbitron', sans-serif;
        color: #FFB100;
        font-size: 14px;
        text-transform: lowercase;
        letter-spacing: 2px;
        opacity: 0.8;
    }

    /* Limpeza total de bordas e sombras da imagem */
    [data-testid="stImage"] img {
        border: none !important;
        box-shadow: none !important;
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Centralização do Logo (logo.png)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        # Fallback caso o arquivo ainda não tenha sido processado no GitHub
        st.markdown("<h1 style='color:#FFB100; text-align:center; font-family:Orbitron;'>λ</h1>", unsafe_allow_html=True)

# Identidade Visual
st.markdown("""
    <div class="title-container">
        <p class="title-guimel">λ g.u.i.m.e.l.</p>
        <p class="subtitle">sistemas logísticos e teológicos online</p>
    </div>
    """, unsafe_allow_html=True)

# 3. Terminal na Barra Lateral
with st.sidebar:
    st.markdown("<h2 style='color:#FFB100; font-family:Orbitron; font-size:18px;'>terminal</h2>", unsafe_allow_html=True)
    api_key = st.text_input("chave de protocolo", type="password")
    st.markdown("<hr style='border: 0.5px solid #222;'>", unsafe_allow_html=True)

# 4. Processamento da Inteligência (Gemini 1.5 Flash)
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        if "chat" not in st.session_state:
            st.session_state.chat = model.start_chat(history=[])
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Renderização do Histórico
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(f"<span style='font-family:Orbitron; color:#ddd;'>{msg['content']}</span>", unsafe_allow_html=True)

        # Entrada de Comandos
        if prompt := st.chat_input("comando, senhor?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
    except Exception as e:
        st.error(f"sistema em standby: erro de conexão ({e})")
else:
    st.markdown("<br><center><p style='color:#444; font-family:Orbitron; font-size:10px;'>insira a chave para despertar o núcleo.</p></center>", unsafe_allow_html=True)
