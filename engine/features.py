import os
import re
import eel
import sqlite3
import webbrowser
import pywhatkit as kit
from playsound import playsound
from engine.commands import *
from engine.configs import *

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

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'

    # Use re.search to find the match in the comment
    match = re.search(pattern, command, re.IGNORECASE)

    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None
