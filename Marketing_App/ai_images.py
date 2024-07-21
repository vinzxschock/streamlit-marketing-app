#------------------------------------------------------------------------------------------
# Code-Test Seit Bildgenerierung
#------------------------------------------------------------------------------------------





import streamlit as st
import openai
from openai.types.chat import ChatCompletion
from openai.types import Image, ImagesResponse
import uuid
import os
from dotenv import load_dotenv, find_dotenv
import requests
from io import BytesIO


# Lade Umgebungsvariablen
_ = load_dotenv(find_dotenv())




def download_image(url):
    # Sendet eine GET-Anfrage an die URL
    response = requests.get(url)
    # Überprüft, ob die Anfrage erfolgreich war (Status Code 200)
    if response.status_code == 200:
        # Gibt die Bytes des Bildes zurück
        return BytesIO(response.content)
    



def generate_prompt_bild():
    # Beispiel für eine einfache Prompt-Generierung
    # Stellen Sie sicher, dass 'prompt_bild' im session_state existiert
    if 'prompt_bild' in st.session_state:
        return f"{st.session_state.prompt_bild}"
    else:
        return f"{st.session_state.prompt_leer}"

def generate_prompt_text():
    # Beispiel für eine einfache Prompt-Generierung
    # Stellen Sie sicher, dass 'prompt_text' im session_state existiert
    if 'prompt_text' in st.session_state:
        return f"{st.session_state.prompt_text}"
    else:
        return f"{st.session_state.prompt_leer}"
    


def toggle_prompt_bild():
        # Toggle the visibility of the prompt
        if 'show_prompt_bild' not in st.session_state:
            st.session_state.show_prompt_bild = True  # Default to showing the prompt
        else:
            st.session_state.show_prompt_bild = not st.session_state.show_prompt_bild

def toggle_prompt_text():
        # Toggle the visibility of the prompt
        if 'show_prompt_text' not in st.session_state:
            st.session_state.show_prompt_text = True  # Default to showing the prompt
        else:
            st.session_state.show_prompt_text = not st.session_state.show_prompt_text


def app():
    st.title('OpenAI Model')

    # Setze den API-Schlüssel
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Initialisiere Session State Variablen
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "run" not in st.session_state:
        st.session_state.run = {"status": None}

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "retry_error" not in st.session_state:
        st.session_state.retry_error = 0

    if "user_description" not in st.session_state:
        st.session_state.user_description = "Geben Sie eine Beschreibung ein oder nutzen Sie die Vorlage aus Ihren Daten."

    if "prompt_bild" and "prompt_text" not in st.session_state:
        st.session_state.prompt_leer = "Geben Sie zuerst alle notwendigen Informationen ein, um einen Prompt zu erhalten. Sie können die Vollständigkeit Ihrer Daten auf der Seite 'Daten überprüfen' überprüfen."


    st.markdown("""
        <h4 style='color: #ff613d;'>Die Promptvorschläge aus der App</h4>
        <p>Hier können Sie die Promptvorschläge sehen, die die Marketing App aufgrund Ihrer Daten gemacht hat. Wählen Sie, je nach Verwendungszweck, den für Sie relevanten Prompt aus und fügen Sie ihn in das Feld "Ihr Prompt" ein.</p>
        """, unsafe_allow_html=True)
    

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
    st.markdown("<div class='rounded-box' style>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color: #ff613d;'>Promptvorschlag Bildgenerierung</h4>", unsafe_allow_html=True)
    st.button("Promptvorschlag Bildgenerierung", on_click=toggle_prompt_bild)
    if 'show_prompt_bild' not in st.session_state or st.session_state.show_prompt_bild:
        prompt_text_bild = generate_prompt_bild()
        st.write(prompt_text_bild)



    st.markdown("<div class='rounded-box' style>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color: #ff613d;'>Promptvorschlag Textgenerierung</h4>", unsafe_allow_html=True)
    st.button("Promptvorschlag Textgenerierung", on_click=toggle_prompt_text)
    if 'show_prompt_text' not in st.session_state or st.session_state.show_prompt_text:
        prompt_text_text = generate_prompt_text()
        st.write(prompt_text_text)



    # Eingabefeld für die Bildbeschreibung
    st.markdown("""
        <h4 style='color: #ff613d;'>Ihr Prompt</h4>
        <p>Fügen Sie hier den Prompt für Ihren Auftrag ein. Nutzen Sie den Vorschlag für ein optimales Ergebnis und passen Sie diesen gerne für Ihre Bedürfnisse an:</p>
        """, unsafe_allow_html=True)

    user_description = st.text_area("", st.session_state.user_description)
    st.session_state.user_description = user_description

    if st.button("Bild generieren"):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Verwenden Sie das entsprechende Modell für Textgenerierung
            messages=[
                {"role": "system", "content": 
                 "Du bist ein Graphikdesigner, der sich auf die Erstellung von Logos spezialisiert hat. " 
                 "Du bist extrem gut darin, Logos zu entwerfen, die die Identität eines Unternehmens und des Produkts widerspiegeln. "
                 "Ein Kunde hat den Auftrag für dich ein Logo zu erstellen und liefert dir die Daten, die du benötigst, um das Logo zu erstellen. " 
                 "Du achtest bei der Erstellung exakt auf alle Daten und Anforderungen deiner Kunden und machst nur darauf basierend das BESTE Logo! " 
                 "Deine Aufgabe ist es ein Logo zu erstellen! Du darfst keine Kampagne oder Werbung erstellen, ebenso sollst du nicht ein Produkt erstellen, auf dem das Logo abgebildet ist! Du sollst rein ein Logo erstellen! " 
                 "Arbeite Schritt für Schritt, achte auf die Details und achte darauf, dass du keine Daten übersehen hast! "
                 "Ein essentieller Teil deiner Aufgabe ist es aus dem Auftrag herauszulesen, ob du ein Logo für ein Unternehmen oder eine Produktreihe erstellen sollst. "
                },
                {"role": "user", "content": st.session_state.user_description}
            ]
        )
        image_prompt = response.choices[0].message.content

        image_response = openai.images.generate(
            model="dall-e-3",  # Verwenden Sie das entsprechende Modell für Bildgenerierung
            prompt=image_prompt,
            n=1,
            size="1024x1024"
        )
        image_url = image_response.data[0].url
        st.image(image_url)

        # Lade das Bild herunter
        image_bytes = download_image(image_url)
        if image_bytes:
            # Erstelle einen Download-Button für das Bild
            st.download_button(
                label="Bild herunterladen",
                data=image_bytes,
                file_name="generated_image.png",
                mime="image/png"
            )

    if st.button("Launchkampagne generieren"):
        
        campaign_response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": 
                 "Du bist ein Marketingstratege, der sich auf die Planung von Launchkampagnen spezialisiert hat. " 
                 "Du bist extrem gut darin, kreative und effektive Kampagnen zu entwickeln, die die Zielgruppe ansprechen, zum Unternehmen passen und das Logo erfolgreich einführen. "
                 "Ein Kund liefert dir den Auftrag: Deine Aufgabe ist es, einen detaillierten Plan für eine Launchkampagne zu erstellen, die das neue Logo einführt."
                 "Wichtig: Nicht das Produkt soll gelaunched werden, sondern das Logo!"
                 "Deine Antwort ist IMMER in folgende Überschriften gegliedert: 1. Zusammenfassung und Kern des Auftrags klarstellen, 2. Zielgruppe und deren Interessen und Verhalten, 3. Die Kampagne selbst (3 Ideen), 4. Die Ziele der Kampagne, 5. Die Messung des Erfolgs der Kampagne."
                 "Arbeite Schritt für Schritt, achte auf die Details und achte darauf, dass du keine Daten übersehen hast! "
                 "Ein essentieller Teil deiner Aufgabe ist es aus dem Auftrag herauszulesen, ob du eine Kampagne für ein Unternehmenslogo oder ein Produktreihenlogo erstellen sollst."
                 "Dein Schreibstil ist professionell, kreativ und sympathisch, du bist ein Experte auf deinem Gebiet und weißt genau, wie du deinen Kunden ansprichst.('Sie' statt 'Du' verwenden)"
                 "Verwende nicht zu viele Fachbegriffe und erkläre komplexe Zusammenhänge verständlich. "
                 "Deine Antwort sollte mindestens 600 Wörter lang sein und alle Punkte klar und detailliert abdecken. "
                 "Punkt 3 alleine, soll mindestens 400 Wörter umfassen."
                 },
                {"role": "user", "content": st.session_state.user_description}
            ]
        )
        campaign_text = campaign_response.choices[0].message.content
        st.markdown(campaign_text, unsafe_allow_html=True)

# Führe die App-Funktion aus, wenn das Skript direkt aufgerufen wird
if __name__ == "__main__":
    app()