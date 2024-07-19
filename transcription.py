from gtts import gTTS
import os

# Ouvrir le fichier texte en mode lecture
with open("text.txt", "r") as fichier:
  # Lire le contenu du fichier
  contenu = fichier.read()
  # fonction pour executer la transcription

def convertir_texte_audio(texte):
    # Créer un objet gTTS
    audio = gTTS(texte, lang='fr-fr')
    # Enregistrer l'audio dans un fichier
    audio.save("audio.mp3")
    # Lire l'audio
    os.system("audio.mp3")
    
convertir_texte_audio(contenu)
                  