import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração da Página
st.set_page_config(page_title="g.u.i.m.e.l. os", page_icon="favicon.png", layout="centered")

# CSS para camuflagem total e tipografia futurista
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    /* Preto absoluto para camuflar a foto */
    .stApp {
        background-color: #000000;
    }
    
    /* Estilo futurista para o texto */
    .title-futurista {
        font-family: 'Orbitron', sans-serif;
        font-size: 42px;
        color: #FFCC00; /* Amarelo Mostarda sólido */
        text-align: center;
        text-transform: lowercase;
        letter-spacing: 4px;
        margin-top: -20px;
    }

    .subtitle-futurista {
        font-family: 'Orbitron', sans-serif;
        color: #FFCC00;
        text-align: center;
        font-size: 14px;
        text-transform: lowercase;
        letter-spacing: 2px;
        opacity: 0.7;
    }

    /* Remove qualquer moldura das imagens */
    [data-testid="stImage"] {
        background-color: transparent !important;
        border: none !important;
        padding: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Brasão Central (Favicon para camuflagem)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists("favicon.png"):
        st.image("favicon.png", use_container_width=True)

st.markdown('<p class="title-futurista">λ g.u.i.m.e.l.</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-futurista">sistemas logísticos e teológicos online</p>', unsafe_allow_html=True)

# 3. Sidebar (Terminal)
with st.sidebar:
    st.markdown("<h2 style='color:#FFCC00; font-family:Orbitron; font-size:18px;'>terminal</h2>", unsafe_allow_html=True)
    api_key = st.text_input("chave de protocolo", type="password")

# 4. Lógica de IA
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
        st.error(f"sistema em espera: {e}")
else:
    st.markdown("<br><center><p style='color:#333; font-family:Orbitron; font-size:10px;'>conecte a chave para iniciar o protocolo.</p></center>", unsafe_allow_html=True)
