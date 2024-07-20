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
        st.session_state['data_available'] = False
    elif missing_groups:
        st.warning(f"Es fehlen noch Daten von den Seiten: {', '.join(missing_groups)}.")
        st.session_state['data_available'] = False
    else:
        st.success("Alle erforderlichen Daten wurden angegeben.")
        st.session_state['data_available'] = True

    if st.session_state['data_available']:
        st.session_state["prompt_bild"] = generate_prompt_bild(available_data)
        st.session_state["prompt_text"] = generate_prompt_text(available_data)
    else:
        # Löschen der Prompts, falls vorhanden
        if "prompt_bild" in st.session_state:
            del st.session_state["prompt_bild"]
        if "prompt_text" in st.session_state:
            del st.session_state["prompt_text"]

    return available_data



# Prompt Engineering --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def generate_prompt_bild(available_data):
    prompt_bild = ""

    # Unternehmensinformationen hinzufügen
    if available_data['A_Logo']:
         prompt_bild += (
            f"Erstelle ein Firmenlogo für ein Unternehmen mit den folgenden Unternehmensinformationen, Zielgruppeninformationen und Auftragsinformationen."
            f"\n\n"
            f"  <unternehmensinformationen>"
            f"\n\n"
            f"      <unternehmensname>{st.session_state['U_Daten']['unternehmensname']}</unternehmensname>"
            f"\n\n"
            f"      <branche>{st.session_state['U_Daten']['branche']}</branche>"
            f"\n\n"
            f"      <unternehmensgröße>{st.session_state['U_Daten']['groesse']}</unternehmensgröße>"
            f"\n\n"
            f"      <markenpersönlichkeit>{st.session_state['U_Daten']['markenpersoenlichkeit']}</markenpersönlichkeit>"
            f"\n\n"
            f"      <tonalität>{st.session_state['U_Daten']['tonalitaet']}</tonalität>"
            f"\n\n"
            f"  </unternehmensinformationen>."
            f"\n\n"
            f"\n\n"
        )
         
    if available_data['A_Produkt']:
        prompt_bild +=(
            f"Erstelle ein Logo für ein Produkt, dass aus einem Unternehmen mit folgenden Unternehmensinformationen stammt, folgende Zielgruppe bestehend aus folgenden Zielgruppeninformationen hat, und folgende Produktinformationen hat:"
            f"\n\n"
            f"  <unternehmensinformationen>"
            f"\n\n"
            f"      <unternehmensname>{st.session_state['U_Daten']['unternehmensname']}</unternehmensname>"
            f"\n\n"
            f"      <branche>{st.session_state['U_Daten']['branche']}</branche>"
            f"\n\n"
            f"      <unternehmensgröße>{st.session_state['U_Daten']['groesse']}</unternehmensgröße>"
            f"\n\n"
            f"      <markenpersönlichkeit_und_werte>{st.session_state['U_Daten']['markenpersoenlichkeit']}</markenpersönlichkeit_und_werte>"
            f"\n\n"
            f"      <tonalität>{st.session_state['U_Daten']['tonalitaet']}</tonalität>"
            f"\n\n"
            f"  </unternehmensinformationen>."
            f"\n\n"
            f"\n\n"
        )
    
    # Zielgruppeninformationen hinzufügen
    prompt_bild += "  <zielgruppeninformationen>\n\n"
    if available_data['Z_Personas']:
        for persona in st.session_state['Z_Personas']:
            prompt_bild += (
                f"      <user_persona id='{persona['id']}'>\n\n"
                f"          <name>{persona['name']}</name>\n\n"
                f"          <alter>{persona['alter']}</alter>\n\n"
                f"          <geschlecht>{persona['geschlecht']}</geschlecht>\n\n"
                f"          <einkaufsgewohnheiten>{persona['einkaufsgewohnheiten']}</einkaufsgewohnheiten>\n\n"
                f"          <soziale_medien_plattform_und_taegliche_nutzungsdauer>{persona['soziale_medien']}</soziale_medien_plattform_und_taegliche_nutzungsdauer>\n\n"
                f"          <interessen>{persona['interessen']}</interessen>\n\n"
                f"          <werte>{persona['werte']}</werte>\n\n"
                f"          <markenpraferenz>{persona['markenpraferenz']}</markenpraferenz>\n\n"
                f"          <einkommen_jährlich>{persona['einkommen']}</einkommen_jährlich>\n\n"
                f"      </user_persona>\n\n"
            )
    
    if available_data['Z_Zielgruppe']:
        for zielgruppe in st.session_state['Z_Zielgruppe']:
            prompt_bild += (
                f"      <zielgruppe id='{zielgruppe['id']}'>\n\n"
                f"          <altersrange>{zielgruppe['altersrange']}</altersrange>\n\n"
                f"          <geschlecht>{zielgruppe['geschlecht']}</geschlecht>\n\n"
                f"          <zielgruppengroesse>{zielgruppe['size']}</zielgruppengroesse>\n\n"
                f"          <einkommensrange_jährlich>{zielgruppe['einkommensrange']}</einkommensrange_jährlich>\n\n"
                f"          <gemeinsame_interessen>{zielgruppe['gemeinsame_interessen']}</gemeinsame_interessen>\n\n"
                f"          <werte>{zielgruppe['werte']}</werte>\n\n"
                f"          <kaufverhalten>{zielgruppe['kaufverhalten']}</kaufverhalten>\n\n"
                f"          <nutzungsverhalten>{zielgruppe['nutzungsverhalten']}</nutzungsverhalten>\n\n"
                f"          <markenloyalitaet>{zielgruppe['markenloyalitaet']}</markenloyalitaet>\n\n"
                f"      </zielgruppe>\n\n"
            )

    prompt_bild += f"  </zielgruppeninformationen>.\n\n"

    # Auftragsinformationen hinzufügen

    if available_data['A_Logo']:
        prompt_bild += (
            f"\n\n"
            f"  <auftragsinformationen>"
            f"\n\n"
            f"      <auftragsname>Firmenlogo</auftragsname>"
            f"\n\n"
            f"      <extra_informationen>{st.session_state['A_Logo']['extras_firma']}</extra_informationen>"
            f"\n\n"
            f"  </auftragsinformationen>."
            f"\n\n"
        )

    if available_data['A_Produkt']:
        prompt_bild += (
            f"\n\n"
            f"  <produktinformationen>"
            f"\n\n"
            f"      <auftragsname>Produktlogo</auftragsname>"
            f"\n\n"
            f"      <produktbezeichnung>{st.session_state['A_Produkt']['produktbez']}</produktbezeichnung>"
            f"\n\n"
            f"      <beschreibung>{st.session_state['A_Produkt']['beschreibung']}</beschreibung>"
            f"\n\n"
            f"      <preis>{st.session_state['A_Produkt']['preis']}</preis>"
            f"\n\n"
            f"      <usp>{st.session_state['A_Produkt']['usp']}</usp>"
            f"\n\n"
            f"      <tonalität>{st.session_state['A_Produkt']['tonalitaet']}</tonalität>"
            f"\n\n"
            f"      <extra_informationen>{st.session_state['A_Produkt']['extras_produkt']}</extra_informationen>"
            f"\n\n"
            f"  </produktinformationen>."
            f"\n\n"
        )



    return prompt_bild



def generate_prompt_text(available_data):
    prompt_text = ""
    if st.session_state['A_Logo']:
        prompt_text += f"Erstellen Sie eine Launchkampagne für das neue Firmenlogo."
    if st.session_state['A_Produkt']:
        prompt_text += f"Erstellen Sie eine Launchkampagne für das Produkt {st.session_state['A_Produkt']['produktbez']}."

    return prompt_text


# Prompt Engineering Ende ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------



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
    if st.button('Exportieren als PDF'):
        pdf_path = 'data_overview.pdf'
        # Pfad zu wkhtmltopdf - aktualisieren Sie diesen Pfad entsprechend Ihrer Installation
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

        # Verwenden Sie die Konfiguration beim Erstellen des PDFs
        pdfkit.from_string(html_content, pdf_path, configuration=config)
        st.success('PDF erfolgreich erstellt.')
        with open(pdf_path, "rb") as f:
            st.download_button("Download PDF", f, file_name="data_overview.pdf")

    if st.session_state['data_available']:
        st.markdown("## Generierte Prompts")
        st.markdown(f"**Prompt für Bild:** {st.session_state['prompt_bild']}")
        st.markdown(f"**Prompt für Text:** {st.session_state['prompt_text']}")