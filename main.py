import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração da Página
st.set_page_config(page_title="G.U.I.M.E.L. OS", page_icon="ג", layout="centered")

# Estilo J.A.R.V.I.S.
st.markdown("<style>.stApp { background-color: #0e1117; color: #ffcc00; }</style>", unsafe_allow_html=True)

# 2. Carregamento do Logotipo (Forçado)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.title("ג G.U.I.M.E.L.")

st.subheader("Sistemas Logísticos e Teológicos Online.")

# 3. Barra Lateral e Chave
with st.sidebar:
    st.title("Configurações")
    api_key = st.text_input("Chave de Protocolo", type="password")

# 4. Lógica da IA (Modelo Estável)
if api_key:
    try:
        genai.configure(api_key=api_key)
        # Usando o modelo mais compatível do mundo
        model = genai.GenerativeModel("gemini-1.0-pro")
        
        if "chat" not in st.session_state:
            st.session_state.chat = model.start_chat(history=[])
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Mostrar mensagens
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Input do Senhor
        if prompt := st.chat_input("Comando, Senhor?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Resposta da IA
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
    except Exception as e:
        st.error(f"Erro de Conexão: O Google ainda não liberou o acesso. Aguarde o prazo de 5 horas. (Detalhe: {e})")
else:
    st.info("Senhor, por favor, insira a Chave de Protocolo na barra lateral.")
