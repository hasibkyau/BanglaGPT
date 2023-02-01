import speech_recognition as s_r
from googletrans import Translator
import pyttsx3
import pygame
import openai
from gtts import gTTS

openai.api_key = "Your API KEY"


# print(s_r.__version__) # just to print the version not required
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone
    text = r.recognize_google(audio, language="bn-BD")

# print(r.recognize_google(audio)) #to print voice into text

# Translating the text to English
translator = Translator(service_urls=["translate.google.com"])
english_text = translator.translate(text, dest="en").text

print(text)
print(english_text)

# prompt = "python chatgpt code example"
prompt = english_text
model_engine = "text-davinci-002"
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)

# create an engine instance
engine = pyttsx3.init()

# set the voice and rate
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
engine.setProperty('rate', 150)

# input text to be converted to speech
text = message

# converting english to bangla
# translator = Translator(dest='bn')
bangla_text = translator.translate(text, dest="bn").text

# translated = translator.translate(text).text
print(bangla_text)

# text = "আমি বাংলা বলছি"

tts = gTTS(bangla_text, lang='bn')
tts.save("output.mp3")

# speak the text
# engine.say(text)
# engine.say(text)
# engine.runAndWait()

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.wait(100)

pygame.mixer.music.stop()
pygame.quit()
