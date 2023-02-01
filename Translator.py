import speech_recognition as sr
from googletrans import Translator

# Transcribing the audio to text
r = sr.Recognizer()
with sr.AudioFile("AudioFiles/Bangla_Voice_01.wav") as source:
    audio_text = r.listen(source)
    text = r.recognize_google(audio_text, language="bn-BD")

# Translating the text to English
translator = Translator(service_urls=["translate.google.com"])
english_text = translator.translate(text, dest="en").text

print(english_text)