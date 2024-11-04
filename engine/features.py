import os
import eel
import time
import struct
import pyaudio
import sqlite3
import webbrowser
import pvporcupine
import pywhatkit as kit
from playsound import playsound
from engine.commands import speak
from engine.configs import ASSISTANT_NAME
from engine.helper import extract_yt_term

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# Playing Assistant Sound
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\magic.wav"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute("SELECT path FROM sys_command WHERE name IN (?)", (app_name,))
            result = cursor.fetchall()

            if len(result) != 0:
                speak("Opening " + query)
                os.startfile(result[0][0])
            
            elif len(result) == 0:
                cursor.execute("SELECT url FROM web_command WHERE name IN (?)", (app_name,))
                result = cursor.fetchall()

                if len(result) != 0:
                    speak("Opening " + query)
                    webbrowser.open(result[0][0])

                else:
                    speak("Opening " + query)
                    try:
                        os.system("start " + query)
                    except:
                        speak("Not found!")
        except:
            speak("Something went wrong!")

def playYouTube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + str(search_term) + " on Youtube")
    kit.playonyt(search_term)

def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        # Pre-Trained Keywords
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)

        # Loop for streaming
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h"*porcupine.frame_length, keyword)

            # Processing keyword comes form mic
            keyword_index = porcupine.process(keyword)

            # Checking first keyword detected for not
            if keyword_index >= 0:
                print("Hotword detected")

                # Pressing shortcut key win + j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press('j')
                time.sleep(2)
                autogui.keyUp("win")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
