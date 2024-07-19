#------------------------------------------------------------------------------------------
# Zusammenfassung der Dateninputs
#------------------------------------------------------------------------------------------





import streamlit as st
import pdfkit
from tempfile import NamedTemporaryFile



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

    html_content = "<!DOCTYPE html><html><head><meta charset='UTF-8'><style>h2 { color: #ff613d; }</style></head><body>"
    html_content += "<h1>Gesammelte Daten Übersicht</h1>"

    # Auftragsdaten
    if available_data['A_Logo']:
        st.markdown(f"<h2 style='color: #ff613d;'>Auftragsdaten für Firmenlogo</h2>", unsafe_allow_html=True)
        html_content += "<h2>Auftragsdaten für Firmenlogo</h2><ul>"
        for key, value in st.session_state['A_Logo'].items():
            st.write(f"{key}: {value}")
            html_content += f"<li>{key}: {value}</li>"
        html_content += "</ul>"

    if available_data['A_Produkt']:
        st.markdown(f"<h2 style='color: #ff613d;'>Auftragsdaten für Produktlogo</h2>", unsafe_allow_html=True)
        html_content += "<h2>Auftragsdaten für Produktlogo</h2><ul>"
        for key, value in st.session_state['A_Produkt'].items():
            st.write(f"{key}: {value}")
            html_content += f"<li>{key}: {value}</li>"
        html_content += "</ul>"

    # Unternehmensdaten
    if available_data['U_Daten']:
        st.markdown(f"<h2 style='color: #ff613d;'>Unternehmensdaten</h2>", unsafe_allow_html=True)
        u_daten = st.session_state['U_Daten']
        html_content += "<h2>Unternehmensdaten</h2><ul>"
        for key, value in u_daten.items():
            st.write(f"{key}: {value}")
            html_content += f"<li>{key}: {value}</li>"
        html_content += "</ul>"

    # Zielgruppendaten
    if available_data['Z_Personas']:
        st.markdown(f"<h2 style='color: #ff613d;'>Zielgruppe</h2>", unsafe_allow_html=True)
        html_content += "<h2>Zielgruppe</h2>"
        for persona in st.session_state['Z_Personas']:
            st.subheader(f"User Persona {persona['id']}")
            html_content += f"<h3>User Persona {persona['id']}</h3><ul>"
            for key, value in persona.items():
                st.write(f"{key}: {value}")
                html_content += f"<li>{key}: {value}</li>"
            html_content += "</ul>"
            st.write("---")

    if available_data['Z_Zielgruppe']:
        st.markdown(f"<h2 style='color: #ff613d;'>Zielgruppe</h2>", unsafe_allow_html=True)
        html_content += "<h2>Zielgruppe</h2>"
        for zielgruppe in st.session_state['Z_Zielgruppe']:
            st.subheader(f"Zielgruppe {zielgruppe['id']}")
            html_content += f"<h3>Zielgruppe {zielgruppe['id']}</h3><ul>"
            for key, value in zielgruppe.items():
                st.write(f"{key}: {value}")
                html_content += f"<li>{key}: {value}</li>"
            html_content += "</ul>"
            st.write("---")

    html_content += "</body></html>"

    return html_content



def app():
    available_data = check_data_availability()
    html_content = display_data(available_data)

    # Button zum Exportieren der Daten als PDF
    if st.button('Export as PDF'):
        pdf_path = 'data_overview.pdf'
        # Pfad zu wkhtmltopdf - aktualisieren Sie diesen Pfad entsprechend Ihrer Installation
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

        # Verwenden Sie die Konfiguration beim Erstellen des PDFs
        pdfkit.from_string(html_content, pdf_path, configuration=config)
        st.success('PDF erfolgreich erstellt.')
        with open(pdf_path, "rb") as f:
            st.download_button("Download PDF", f, file_name="data_overview.pdf")