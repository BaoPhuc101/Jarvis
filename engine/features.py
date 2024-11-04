import os
import re
import eel
import pywhatkit as kit
from playsound import playsound
from engine.commands import *
from engine.configs import *

# Playing Assistant Sound
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\magic.wav"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speak("Opening " + query)
        os.system("start " + query)
    else:
        speak("Not Found")

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
