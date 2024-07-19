import streamlit as st
import zielgruppe
import unternehmen
import ai
import daten
import anleitung
import auftrag
import ai_images

# To use this app, you need an .env file with the OPENAI API
# and you need to fill in the ID in the assistant.py file

PAGES = {
    "Anleitung": anleitung,
    "Zielgruppe": zielgruppe,
    "Unternehmen": unternehmen,
    "Auftrag": auftrag,
    "Daten überprüfen": daten,
    "AI": ai,
    "AI Images": ai_images,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()