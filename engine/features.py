import eel
from playsound import playsound

# Playing Assistant Sound
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\magic.wav"
    playsound(music_dir)
