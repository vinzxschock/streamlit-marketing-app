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

st.sidebar.markdown("<h1 style='text-align: center; color: #ff613d; font-size: 50px;'>LogoMatch</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center; font-size: 35px;'>Navigation</h2>", unsafe_allow_html=True)

# Anpassen der Radio-Buttons für die Navigation mit einem zugänglichen Label
page_selection = st.sidebar.radio("Seitennavigation", list(PAGES.keys()), label_visibility='collapsed')

# Anzeigen der aktuellen Seite basierend auf der Auswahl
PAGES[page_selection].app()