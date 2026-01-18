import streamlit as st

st.set_page_config(page_title="Abrir WhatsApp Web", page_icon="📱")

st.title("Abrir WhatsApp Web")
st.write("Clique no botão abaixo para abrir o WhatsApp Web no navegador:")

if st.button("Abrir WhatsApp Web"):
    st.markdown("[Abrir WhatsApp Web](https://web.whatsapp.com)", unsafe_allow_html=True)
