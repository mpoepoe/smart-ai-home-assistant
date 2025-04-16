import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)  # Words per minute
    engine.setProperty('volume', 1.0)  # Max volume
    engine.say(text)
    engine.runAndWait()
