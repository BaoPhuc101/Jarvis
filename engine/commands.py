import eel
import pyttsx3
import time
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 125)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def all_command():
    try:
        query = take_command()
        print(query)

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from engine.features import playYouTube
            playYouTube(query)
        else:
            print("Not run!")
    except:
        print("Error")

    eel.ShowHood()
