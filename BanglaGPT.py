import speech_recognition as s_r
from googletrans import Translator
import openai
openai.api_key = "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"


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