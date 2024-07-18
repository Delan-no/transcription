from gtts import gTTS
import os

# Définir le texte à convertir en audio
texte = "Bonjour, comment allez-vous ? je suis délanno kotcho un programmeur des applications web et mobile."

# fonction pour executer la transcription

def convertir_texte_audio(texte):
    # Créer un objet gTTS
    audio = gTTS(texte, lang='fr-fr')
    # Enregistrer l'audio dans un fichier
    audio.save("audio.mp3")
    # Lire l'audio
    os.system("audio.mp3")
    
convertir_texte_audio(texte)
                  