import pyttsx3

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 125)
    print(voices)
    engine.say(text)
    engine.runAndWait()

speak("I love Vietnam, my name is Le Hoang Bao Phuc")
