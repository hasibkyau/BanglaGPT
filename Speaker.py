import pyttsx3

# create an engine instance
engine = pyttsx3.init()

# set the voice and rate
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
engine.setProperty('rate', 150)

# input text to be converted to speech
text = "Hello, ami akti text-to-speech example."

# speak the text
engine.say(text)
engine.runAndWait()
