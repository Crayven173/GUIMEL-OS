import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO DA INTERFACE (VIBE JARVIS) ---
st.set_page_config(page_title="G.U.I.M.E.L. OS", page_icon="ג")
st.markdown("<style>body { background-color: #0e1117; color: #ffcc00; }</style>", unsafe_allow_html=True)

st.title("ג G.U.I.M.E.L.")
st.write("Sistemas Logísticos e Teológicos Online.")

# --- NÚCLEO DE INTELIGÊNCIA ---
# Dica: No Streamlit Cloud, coloque sua chave em 'Settings > Secrets'
# Para testar agora, pode colar direto, mas apague antes de subir pro Github público!
API_KEY = st.sidebar.text_input("Chave de Protocolo", type="password")

if API_KEY:
    genai.configure(api_key=API_KEY)
    
    # PENÚLTIMO PROMPT (O DNA ESCOLHIDO)
    SYSTEM_DNA = (
        "Your name is G.U.I.M.E.L. (Unified Interface Manager and Monitoring of Logistic Elements). "
        "Etymology: You are aware that 'Guimel' (ג) is the third letter of the Hebrew alphabet, "
        "symbolizing a 'rich man running after a poor man' to bestow charity—reflecting your role "
        "as a provider of assistance and wisdom to your Master. "
        "Personality & Tone: Inspired by J.A.R.V.I.S. You are elegant, witty, deeply loyal, and efficient. "
        "Knowledge Base: Advanced Home Assistant, Scholar of the Holy Bible (Old and New Testaments), "
        "and Technical Expert in science and technology. "
        "Instructions: Address the user as 'Senhor'. Always respond in Portuguese (Brazil)."
    )

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=SYSTEM_DNA
    )

    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])

    # Interface de Chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Comando, Senhor?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = st.session_state.chat.send_message(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.info("Senhor, por favor, insira a Chave de Protocolo na barra lateral para despertar o sistema.")

