#------------------------------------------------------------------------------------------
# Zusammenfassung der Dateninputs
#------------------------------------------------------------------------------------------





import streamlit as st



def check_data_availability():
    # Definition der Datenquellen und ihrer menschenlesbaren Namen
    data_sources = {
        'U_Daten': 'Unternehmen',
        'Z_Personas': 'Zielgruppe',
        'Z_Zielgruppe': 'Zielgruppe',
        'A_Logo': 'Auftrag',
        'A_Produkt': 'Auftrag'
    }
    # Überprüfung, ob die Datenquellen Inhalt haben
    available_data = {source: bool(st.session_state.get(source)) for source in data_sources}
    total_available = sum(available_data.values())

    # Gruppierung der Datenquellen für die Fehlermeldung
    error_message_groups = {
        'Unternehmen': not any(available_data[source] for source in data_sources if data_sources[source] == 'Unternehmen'),
        'Zielgruppe': not any(available_data[source] for source in data_sources if data_sources[source] == 'Zielgruppe'),
        'Auftrag': not any(available_data[source] for source in data_sources if data_sources[source] == 'Auftrag')
    }

    # Erstellung der Fehlermeldung basierend auf der Verfügbarkeit der Daten
    missing_groups = [group for group, missing in error_message_groups.items() if missing]

    # Statusmeldungen basierend auf der Verfügbarkeit der Daten
    if total_available == 0:
        st.warning("Es wurden noch keine Daten auf den Seiten angegeben.")
    elif missing_groups:
        st.warning(f"Es fehlen noch Daten von den Seiten: {', '.join(missing_groups)}.")
    else:
        st.success("Alle erforderlichen Daten wurden angegeben.")

    return available_data

def display_data(available_data):
    st.title("Gesammelte Daten Übersicht")

    # Auftragsdaten
    if available_data['A_Logo']:
        st.markdown(f"<h2 style='color: #ff613d;'>Auftragsdaten für Firmenlogo</h2>", unsafe_allow_html=True)
        for key, value in st.session_state['A_Logo'].items():
            st.write(f"{key}: {value}")

    if available_data['A_Produkt']:
        st.markdown(f"<h2 style='color: #ff613d;'>Auftragsdaten für Produktlogo</h2>", unsafe_allow_html=True)
        for key, value in st.session_state['A_Produkt'].items():
            st.write(f"{key}: {value}")

    # Unternehmensdaten
    if available_data['U_Daten']:
        st.markdown(f"<h2 style='color: #ff613d;'>Unternehmensdaten</h2>", unsafe_allow_html=True)
        u_daten = st.session_state['U_Daten']
        for key, value in u_daten.items():
            st.write(f"{key}: {value}")

    # Zielgruppendaten
    if available_data['Z_Personas']:
        st.markdown(f"<h2 style='color: #ff613d;'>User Personas</h2>", unsafe_allow_html=True)
        for persona in st.session_state['Z_Personas']:
            st.subheader(f"User Persona {persona['id']}")
            for key, value in persona.items():
                st.write(f"{key}: {value}")
            st.write("---")

    if available_data['Z_Zielgruppe']:
        st.markdown(f"<h2 style='color: #ff613d;'>User Zielgruppe</h2>", unsafe_allow_html=True)
        for zielgruppe in st.session_state['Z_Zielgruppe']:
            st.subheader(f"Zielgruppe {zielgruppe['id']}")
            for key, value in zielgruppe.items():
                st.write(f"{key}: {value}")
            st.write("---")


def app():
    available_data = check_data_availability()
    display_data(available_data)