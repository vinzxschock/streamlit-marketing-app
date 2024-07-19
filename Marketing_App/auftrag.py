#------------------------------------------------------------------------------------------
# Auftrag-Daten-Input
#------------------------------------------------------------------------------------------





import streamlit as st



def app():
    st.title("Auftrag definieren")

    

    # Auswahl der Variante
    variante = st.radio("Wählen Sie die Variante:", ("Erstellung eines Logos für die Firma", "Erstellung eines Logos für eine Produktreihe"))

    # Variante Firmenlogo
    if variante == "Erstellung eines Logos für die Firma":
        extras_firma = st.text_input("Zusätzliche Anforderungen für das Firmenlogo:")
        if st.button("Auftrag für Firmenlogo einreichen"):
            # Löschen des Produkt-Dictionaries, falls vorhanden
            st.session_state['A_Produkt'] = {}
            # Hinzufügen der Daten zum Logo-Dictionary
            st.session_state['A_Logo'] = {'extras_firma': extras_firma}
            st.success("Ihr Auftrag für ein Firmenlogo wurde eingereicht und gespeichert.")

    # Variante Produktlogo
    elif variante == "Erstellung eines Logos für eine Produktreihe":
        produktbez = st.text_input("Produktbezeichnung:")
        beschreibung = st.text_area("Produktbeschreibung:")
        preis = st.number_input("Verkaufspreis pro Stück:", min_value=0.0, format="%.2f")
        usp = st.text_input("USPs des Produkts:")
        tonalitaet = st.text_area("Tonalität des Produkts:")
        extras_produkt = st.text_input("Zusätzliche Anforderungen für das Produktlogo:")
        if st.button("Auftrag für Produktlogo einreichen"):
            # Löschen des Logo-Dictionaries, falls vorhanden
            st.session_state['A_Logo'] = {}
            # Hinzufügen der Daten zum Produkt-Dictionary
            st.session_state['A_Produkt'] = {
                'produktbez': produktbez,
                'beschreibung': beschreibung,
                'preis': preis,
                'usp': usp,
                'extras_produkt': extras_produkt,
                'tonalitaet': tonalitaet
            }
            st.success("Ihr Auftrag für ein Produktlogo wurde eingereicht und gespeichert.")