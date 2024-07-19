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
    



def generate_image_prompt():
    # Beispiel für eine einfache Prompt-Generierung
    return "Erstelle ein Bild von: " + st.session_state.user_description + ";biete 2 Bilder zur Auswahl an."




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
        st.session_state.user_description = "Gib eine Beschreibung ein"

    # Eingabefeld für die Bildbeschreibung
    user_description = st.text_input("Beschreibung des Bildes:", st.session_state.user_description)
    st.session_state.user_description = user_description

    if st.button("Bild generieren"):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Verwenden Sie das entsprechende Modell für Textgenerierung
            messages=[
                {"role": "system", "content": "Du bist ein hilfsbereiter Assistent."},
                {"role": "user", "content": generate_image_prompt()}
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

# Führe die App-Funktion aus, wenn das Skript direkt aufgerufen wird
if __name__ == "__main__":
    app()