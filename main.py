import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração da Interface (O ÁPICE)
st.set_page_config(page_title="G.U.I.M.E.L. OS", page_icon="logo.png", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #000000; }
    .title-container { text-align: center; margin-top: -30px; }
    .title-guimel {
        font-family: 'Orbitron', sans-serif;
        font-size: 45px;
        font-weight: 700;
        background: linear-gradient(to right, #FF4B2B, #FFB100, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: uppercase;
        letter-spacing: 6px;
    }
    .subtitle {
        font-family: 'Orbitron', sans-serif;
        color: #FFB100; font-size: 14px; text-transform: uppercase;
        letter-spacing: 3px; opacity: 0.8;
    }
    [data-testid="stImage"] img { border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. Identidade Visual
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

# 3. Terminal Lateral
with st.sidebar:
    st.markdown("<h2 style='color:#FFB100; font-family:Orbitron; font-size:18px;'>TERMINAL</h2>", unsafe_allow_html=True)
    api_key = st.text_input("CHAVE DE PROTOCOLO", type="password")

# 4. O NOVO MOTOR (CORREÇÃO DO ERRO 404)
if api_key:
    try:
        # FORÇANDO A VERSÃO ESTÁVEL V1
        genai.configure(api_key=api_key, transport='rest') # O 'rest' evita erros de gRPC/beta
        
        # Usamos o modelo 1.5-flash que é o mais rápido
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Histórico com visual futurista
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(f"<span style='font-family:Orbitron; color:#eee;'>{msg['content'].upper()}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("COMANDO, SENHOR?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt.upper())
            
            # Chamada direta
            response = model.generate_content(prompt)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text.upper())
                
    except Exception as e:
        st.error(f"SISTEMA EM STANDBY: ERRO DE PROTOCOLO (DETALHE: {e})")
else:
    st.markdown("<br><center><p style='color:#333; font-family:Orbitron; font-size:10px;'>AGUARDANDO CHAVE PARA DESPERTAR O NÚCLEO.</p></center>", unsafe_allow_html=True)
