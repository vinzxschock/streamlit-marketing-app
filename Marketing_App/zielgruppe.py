#------------------------------------------------------------------------------------------
# Zielgruppen-Daten-Input
#------------------------------------------------------------------------------------------





import streamlit as st



# Funktion zum Hinzufügen von User Persona Eingabefeldern
def add_user_persona_form(key):
    with st.container():
        st.markdown("<div class='rounded-box'>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: #ff613d;'>User Persona {key}</h4>", unsafe_allow_html=True)
        st.markdown("""
            <style>
            .rounded-box {
                border: 3px solid #ff613d;
                border-radius: 10px;
                padding: 0px;
                margin: 10px 0;
            }
                    
            .rounded-box-klein {
                border: 1px solid #26ff55;
                border-radius: 10px;
                padding: 0px;
                margin: 5px 0;
            }
            </style>
            """, unsafe_allow_html=True)
        
        # Demographische Daten
        with st.container():
            st.markdown("### Demographische Daten")
            name = st.text_input("Name", key=f"up-{key}-name")
            age = st.slider("Alter", 0, 100, 30, key=f"up-{key}-age")
            geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich", "Divers"], key=f"up-{key}-geschlecht")
            einkommen = st.number_input("Jährliches Einkommen", min_value=0, key=f"up-{key}-income")

        # Psychografische Daten
        with st.container():
            st.markdown("### Psychografische Daten")
            interests = st.text_area("Interessen", key=f"up-{key}-interests")
            werte = st.text_area("Werte", key=f"up-{key}-werte")

        # Verhaltensdaten
        with st.container():
            st.markdown("### Verhaltensdaten")
            einkaufsgewohnheiten = st.text_area("Einkaufsgewohnheiten", key=f"up-{key}-einkaufsgewohnheiten")
        
            # Soziale Medien - Dynamisches Hinzufügen
            available_platforms = ["Facebook", "Instagram", "Tiktok", "Youtube", "Pinterest", "Snapchat", "LinkedIn"]
            selected_platforms = []
            social_media_count = st.number_input("Anzahl der sozialen Medien", 1, 5, key=f"up-{key}-sm-count")
            
            for sm in range(social_media_count):
                with st.container():
                    st.markdown("<div class='rounded-box-klein'>", unsafe_allow_html=True)
                    platform_options = [p for p in available_platforms if p not in selected_platforms]
                    platform = st.selectbox("Plattform", platform_options, key=f"up-{key}-sm-platform-{sm}")
                    selected_platforms.append(platform)
                    st.slider("Durchschnittliche tägliche Nutzungsdauer (Stunden)", 0, 24, key=f"up-{key}-sm-time-{sm}")
                    st.markdown("</div>", unsafe_allow_html=True)
                    
            markenpraferenz = st.text_area("Markenpräferenz", key=f"up-{key}-markenpraferenz")

            # Fügen Sie die Daten der aktuellen Persona zur Liste hinzu (nicht speichern)
            current_persona = {
                "id": key,
                "name": name,
                "alter": age,
                "geschlecht": geschlecht,
                "einkaufsgewohnheiten": einkaufsgewohnheiten,
                "soziale_medien": [(st.session_state[f"up-{key}-sm-platform-{sm}"], str(st.session_state[f"up-{key}-sm-time-{sm}"]) + " Std.") for sm in range(social_media_count)],
                "interessen": interests,
                "werte": werte,
                "markenpraferenz": markenpraferenz,
                "einkommen": einkommen
            }

            # Überprüfe, ob die ID bereits existiert
            existing_persona_key = next((key for (key, d) in enumerate(st.session_state['Pseudo_Z_Personas']) if d["id"] == current_persona["id"]), None)

            # Wenn ja, entferne die existierende Persona
            if existing_persona_key is not None:
                del st.session_state['Pseudo_Z_Personas'][existing_persona_key]

            st.session_state['Pseudo_Z_Personas'].append(current_persona)

        st.markdown("</div>", unsafe_allow_html=True)



# Funktion zum Hinzufügen von allgemeinen Zielgruppendaten Eingabefeldern
def add_general_target_group_form(key):
    with st.container():
        st.markdown("<div class='rounded-box'>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: #ff613d;'>Zielgruppe {key}</h4>", unsafe_allow_html=True)

        # Demographische Daten
        st.markdown("### Demographische Daten")
        altersrange = st.slider("Altersspanne", 0, 100, (18, 65), key=f"{key}-age-range")
        geschlecht = st.multiselect("Geschlecht", ["Männlich", "Weiblich", "Divers"], key=f"{key}-geschlecht")
        size = st.number_input("Größe der Zielgruppe", min_value=1, key=f"{key}-size")
        einkommensrange = st.slider("Jährliche Einkommensspanne", 0, 100000, (20000, 50000), key=f"{key}-income-range")

        # Psychografische Daten
        st.markdown("### Psychografische Daten")
        gemeinsame_interessen = st.text_area("Gemeinsame Interessen", key=f"{key}-gemeinsame-interessen")
        werte = st.text_area("Werte", key=f"{key}-werte")

        # Verhaltensdaten
        st.markdown("### Verhaltensdaten")
        kaufverhalten = st.text_area("Kaufverhalten", key=f"{key}-kaufverhalten")
        nutzungsverhalten = st.text_area("Nutzungsverhalten von Medien", key=f"{key}-nutzungsverhalten")
        markenloyalitaet = st.text_area("Markenloyalität", key=f"{key}-markenloyalitaet")

        current_zielgruppe = {
            "id": key,
            "altersrange": altersrange,
            "geschlecht": geschlecht,
            "size": size,
            "einkommensrange": einkommensrange,
            "gemeinsame_interessen": gemeinsame_interessen,
            "werte": werte,
            "kaufverhalten": kaufverhalten,
            "nutzungsverhalten": nutzungsverhalten,
            "markenloyalitaet": markenloyalitaet
        }
        
        # Überprüfe, ob die ID bereits existiert
        existing_zielgruppe_key = next((key for (key, d) in enumerate(st.session_state['Pseudo_Z_Zielgruppe']) if d["id"] == current_zielgruppe["id"]), None)

        # Wenn ja, entferne die existierende Zielgruppe
        if existing_zielgruppe_key is not None:
                del st.session_state['Pseudo_Z_Zielgruppe'][existing_zielgruppe_key]

        st.session_state['Pseudo_Z_Zielgruppe'].append(current_zielgruppe)

        st.markdown("</div>", unsafe_allow_html=True)

# Haupt-App
def app():


    if "Pseudo_Z_Personas" not in st.session_state:
        st.session_state['Pseudo_Z_Personas'] =[]
    if "Pseudo_Z_Zielgruppe" not in st.session_state:
        st.session_state['Pseudo_Z_Zielgruppe'] = []



    st.title("Zielgruppe")

    st.write("Füge entweder User Personas oder allgemeine Daten zur Zielgruppe hinzu.")

    tab1, tab2 = st.tabs(["User Persona", "Allgemeine Daten zur Zielgruppe"])

    with tab1:
        st.header("User Persona")
        user_persona_count = st.number_input("Anzahl der User Personas", min_value=0, value=0, step=1)
        for i in range(1, user_persona_count + 1):
            add_user_persona_form(i)
        
        if st.button("Alle Personas speichern"):
            # Lösche Zielgruppen-Liste, wenn vorhanden
            if "Z_Zielgruppe" in st.session_state:
                del st.session_state['Z_Zielgruppe']
            # Kopiere Inhalte von Pseudo_Z_Personas zu Z_Personas
            st.session_state['Z_Personas'] = st.session_state['Pseudo_Z_Personas'].copy()
            st.success(f"{len(st.session_state['Z_Personas'])} Personas gespeichert!")

    with tab2:
        st.header("Allgemeine Daten zur Zielgruppe")
        target_group_count = st.number_input("Anzahl der Zielgruppen", min_value=0, value=0, step=1, key="tg_count")
        for i in range(1, target_group_count + 1):
            add_general_target_group_form(i)

        if st.button("Alle Zielgruppen speichern"):
            # Lösche Personas-Liste, wenn vorhanden
            if "Z_Personas" in st.session_state:
                del st.session_state['Z_Personas']
            # Kopiere Inhalte von Pseudo_Z_Zielgruppe zu Z_Zielgruppe
            st.session_state['Z_Zielgruppe'] = st.session_state['Pseudo_Z_Zielgruppe'].copy()
            st.success(f"{len(st.session_state['Z_Zielgruppe'])} Zielgruppen gespeichert!")

# Führe die App aus
if __name__ == "__main__":
    app()