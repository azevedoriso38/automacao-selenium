import streamlit as st

st.set_page_config(page_title="Abrir WhatsApp Web", page_icon="📱")

st.title("Abrir WhatsApp Web")
st.write("Clique no botão abaixo para abrir o WhatsApp Web automaticamente:")

if st.button("Abrir WhatsApp Web"):
    # link que abre WhatsApp Web
    st.markdown('<a href="https://web.whatsapp.com" target="_blank">Abrir WhatsApp Web</a>', unsafe_allow_html=True)
