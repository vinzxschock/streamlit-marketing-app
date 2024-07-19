# company_info.py
import streamlit as st

def app():
    st.title('Unternehmensinformationen')

    # Eingabefelder für Unternehmensdaten
    with st.form(key='company_info_form'):
        unternehmensname = st.text_input("Unternehmensname")
        branche = st.text_input("Branche")
        groesse = st.selectbox("Unternehmensgröße", ["Kleinunternehmen", "Mittelständisch", "Großunternehmen"])

        # Informationen zur Markenpersönlichkeit
        markenpersoenlichkeit = st.text_area("Markenpersönlichkeit und -werte")
        tonalitaet = st.text_area("Tonalität der Marke")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Unternehmensdaten speichern")

        if submit_button:
            # Speichern der Unternehmensdaten im session_state
            st.session_state['U_Daten'] = {
                "unternehmensname": unternehmensname,
                "branche": branche,
                "groesse": groesse,
                "markenpersoenlichkeit": markenpersoenlichkeit,
                "tonalitaet": tonalitaet
            }

            st.success("Unternehmensdaten erfolgreich gespeichert!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()