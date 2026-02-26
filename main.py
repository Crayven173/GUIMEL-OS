import streamlit as st
import requests
import os
import json

# 1. Configuração de Interface (ÁPICE ESTÉTICO)
st.set_page_config(page_title="G.U.I.M.E.L. OS", page_icon="logo.png", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #000000; }
    .title-container { text-align: center; margin-top: -30px; }
    .title-guimel {
        font-family: 'Orbitron', sans-serif; font-size: 45px; font-weight: 700;
        background: linear-gradient(to right, #FF4B2B, #FFB100, #FFFFFF);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-transform: uppercase; letter-spacing: 6px;
    }
    .subtitle {
        font-family: 'Orbitron', sans-serif; color: #FFB100; font-size: 14px;
        text-transform: uppercase; letter-spacing: 3px; opacity: 0.8;
    }
    [data-testid="stImage"] img { border: none !important; background-color: transparent !important; }
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

# 4. MOTOR DE CONEXÃO DIRETA (PROTOCOLO DE EMERGÊNCIA)
def call_gemini_direct(key, message):
    # Usando a URL da versão estável V1 diretamente, sem passar pela biblioteca 'beta'
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={key}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{"parts": [{"text": message}]}]
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"ERRO DE NÚCLEO: {response.status_code} - {response.text}"

if api_key:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(f"<span style='font-family:Orbitron; color:#eee;'>{msg['content'].upper()}</span>", unsafe_allow_html=True)

    if prompt := st.chat_input("COMANDO, SENHOR?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt.upper())
        
        with st.spinner("PROCESSANDO..."):
            try:
                answer = call_gemini_direct(api_key, prompt)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                with st.chat_message("assistant"):
                    st.markdown(answer.upper())
            except Exception as e:
                st.error(f"FALHA CRÍTICA: {e}")
else:
    st.markdown("<br><center><p style='color:#333; font-family:Orbitron; font-size:10px;'>INSIRA A CHAVE PARA DESPERTAR O SISTEMA.</p></center>", unsafe_allow_html=True)
