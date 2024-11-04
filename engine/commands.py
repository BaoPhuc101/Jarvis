import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 125)
    print(voices)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="vi")
        print(f"User said: {query}")
    except Exception as e:
        return ""
    
    return query.lower()

text = take_command()

# speak("I love Vietnam, my name is Le Hoang Bao Phuc")
speak(text)
