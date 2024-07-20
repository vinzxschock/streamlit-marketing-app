import streamlit as st
import zielgruppe
import unternehmen
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
    "AI": ai_images,
}

st.sidebar.title('Navigation')

# Initialisieren der aktuellen Seite im session_state, falls noch nicht gesetzt
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Anleitung"

# Erstellen der Buttons für jede Seite
for page_name in PAGES.keys():
    if st.sidebar.button(page_name):
        st.session_state.current_page = page_name

# Anzeigen der aktuellen Seite
current_page = PAGES[st.session_state.current_page]
current_page.app()