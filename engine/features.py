import eel
from playsound import playsound

# Playing Assistant Sound
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\morning_flower.mp3"
    playsound(music_dir)
