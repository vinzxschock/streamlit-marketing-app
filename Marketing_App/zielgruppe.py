#------------------------------------------------------------------------------------------
# Zielgruppen-Daten-Input
#------------------------------------------------------------------------------------------

import streamlit as st

# Initialisieren Sie die Session State-Variablen
if "personas" not in st.session_state:
    st.session_state['personas'] = []

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
                padding: 10px;
                margin: 10px 0;
            }
                    
            .rounded-box-klein {
                border: 2px solid #26ff55;
                border-radius: 10px;
                padding: 2px;
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
                "name": name,
                "alter": age,
                "geschlecht": geschlecht,
                "einkaufsgewohnheiten": einkaufsgewohnheiten,
                "soziale_medien": [(st.session_state[f"up-{key}-sm-platform-{sm}"], st.session_state[f"up-{key}-sm-time-{sm}"]) for sm in range(social_media_count)],
                "interessen": interests,
                "werte": werte,
                "markenpraferenz": markenpraferenz
            }
            st.session_state.personas.append(current_persona)

        st.markdown("</div>", unsafe_allow_html=True)



# Funktion zum Hinzufügen von allgemeinen Zielgruppendaten Eingabefeldern
def add_general_target_group_form(key):
    with st.container():
        st.markdown(f"<h2 style='color: #ff613d;'>Zielgruppe {key}</h4>", unsafe_allow_html=True)

        # Demographische Daten
        st.markdown("### Demographische Daten")
        demographic = st.text_input("Demographie", key=f"{key}-demographic")
        size = st.number_input("Größe der Zielgruppe", min_value=1, key=f"{key}-size")

        # Psychografische Daten
        st.markdown("### Psychografische Daten")
        gemeinsame_interessen = st.text_area("Gemeinsame Interessen", key=f"{key}-gemeinsame-interessen")
        werte = st.text_area("Werte", key=f"{key}-werte")

        # Verhaltensdaten
        st.markdown("### Verhaltensdaten")
        kaufverhalten = st.text_area("Kaufverhalten", key=f"{key}-kaufverhalten")
        nutzungsverhalten = st.text_area("Nutzungsverhalten von Medien", key=f"{key}-nutzungsverhalten")
        markenloyalitaet = st.text_area("Markenloyalität", key=f"{key}-markenloyalitaet")

        # Submit Button
        if st.button("Submit", key=f"{key}-submit"):
            st.session_state.zielgruppe = {
                "demographie": demographic,
                "groesse": size,
                "gemeinsame_interessen": gemeinsame_interessen,
                "werte": werte,
                "kaufverhalten": kaufverhalten,
                "nutzungsverhalten": nutzungsverhalten,
                "markenloyalitaet": markenloyalitaet
            }
            st.success("Zielgruppendaten gespeichert!")

# Haupt-App
def app():
    st.title("Zielgruppe")

    st.write("Füge entweder User Personas oder allgemeine Daten zur Zielgruppe hinzu.")

    tab1, tab2 = st.tabs(["User Persona", "Allgemeine Daten zur Zielgruppe"])

    with tab1:
        st.header("User Persona")
        user_persona_count = st.number_input("Anzahl der User Personas", min_value=1, value=1, step=1)
        for i in range(1, user_persona_count + 1):
            add_user_persona_form(i)
        
        if st.button("Alle Personas speichern"):
            # Hier könnten Sie die gesammelten Daten verarbeiten oder speichern
            for persona in st.session_state.personas:
                # Verarbeitung jeder Persona
                pass
            st.success(f"{len(st.session_state.personas)} Personas gespeichert!")

    with tab2:
        st.header("Allgemeine Daten zur Zielgruppe")
        target_group_count = st.number_input("Anzahl der Zielgruppen", min_value=1, value=1, step=1, key="tg_count")
        for i in range(1, target_group_count + 1):
            add_general_target_group_form(i)

# Führe die App aus
if __name__ == "__main__":
    app()