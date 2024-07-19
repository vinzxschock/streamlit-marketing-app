#------------------------------------------------------------------------------------------
# Nutzungsanleitung für die Marketing-App
#------------------------------------------------------------------------------------------





import streamlit as st


def app():
    st.title('Nutzungsanleitung')

    st.markdown("""
    ## Willkommen zur Marketing-App!

    Diese App wurde entwickelt, um Ihnen bei der Erstellung von Logos für Ihr Unternehmen oder eine bestimmte Produktreihe Ihres Unternehmens zu helfen. 
    Sie können Informationen über Ihr Unternehmen und Ihre Zielgruppe eingeben, einen Auftrag für ein Logo oder ein Produktlogo definieren und die Auftragsdaten abspeichern.
    Sie erhalten als Produkt KI-generierte Bilder und Texte für Ihre Marketingzwecke.
                
    <span style="color:#ff613d;">Hinweis:</span> Bitte geben Sie so viele Informationen wie möglich ein, um die bestmöglichen Ergebnisse zu erzielen. Die App überprüft die Vollständigkeit Ihrer Daten nur grob.

    <h4 style="color:#ff613d;">Navigation</h4>

    Verwenden Sie die Navigation auf der linken Seite, um zwischen den verschiedenen Abschnitten der App zu wechseln. 
    Klicken Sie auf die Registerkarte, die Sie interessiert, um die entsprechenden Eingabefelder und Optionen anzuzeigen.

    <h4 style="color:#ff613d;">Unternehmensinformation</h4>

    Im Abschnitt "Unternehmen" können Sie Informationen über Ihr Unternehmen eingeben, wie den Namen, die Branche und die Unternehmensgröße. 
    Sie können auch die Markenpersönlichkeit und -werte sowie die Tonalität der Marke definieren.

    <h4 style="color:#ff613d;">Zielgruppendefinition</h4>

    Im Abschnitt "Zielgruppe" können Sie die Zielgruppe für Ihre Marketingmaterialien festlegen. 
    Geben Sie demografische Daten, Interessen und Verhaltensweisen an, um die Zielgruppe genauer zu definieren.
    Sie haben die Wahl, ob sie die Zielgruppe im Format einer Persona oder einer allgemeinen Datenstruktur eingeben möchten.
    Dabei können Sie auch mehrere Personas und Zielgruppen definieren.
             
    <h4 style="color:#ff613d;">Auftrag definieren</h4>

    Im Abschnitt "Auftrag" können Sie einen Auftrag für die Erstellung eines Logos für Ihr Unternehmen oder eine Produktreihe definieren. 
    Geben Sie die erforderlichen Informationen ein und reichen Sie den Auftrag ein.

    <h4 style="color:#ff613d;">Daten überprüfen</h4>

    Im Abschnitt "Daten überprüfen" können Sie die eingegebenen Daten überprüfen und gegebenenfalls korrigieren, bevor Sie die KI-generierten Texte generieren.
    Ihnen wird auch mitgeteilt, ob alle erforderlichen Daten für ein optimales Ergebnis eingegeben wurden.

    <h4 style="color:#ff613d;">AI-Bild- und -Textgenerierung</h4>

    Im Abschnitt "AI" können Sie den für Sie erstellten Prompt in die AI eingeben und die KI-generierten Bilder und Texte erhalten.
    

    ### Viel Spaß beim Erstellen Ihrer Marketingmaterialien mit der Marketing-App!
    """, unsafe_allow_html=True)