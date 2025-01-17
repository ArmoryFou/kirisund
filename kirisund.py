# Change this path to your own audio path
AUDIO_FOLDER = "your/audio/path"

# Change this value to the amount of seconds
# before playing audio after a pause
AUDIO_PLAY_DELAY = 2

## DON'T EDIT BELOW THIS LINE
import time
import random
import os
import psutil
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioMeterInformation
import pygame

pygame.mixer.init()

CURRENT_PID = os.getpid()

def is_audio_playing():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == "System Sounds":
            continue
        
        if session.Process and session.Process.pid == CURRENT_PID:
            continue
        
        volume = session._ctl.QueryInterface(IAudioMeterInformation)
        peak = volume.GetPeakValue()
        if peak > 0.01:
            return True
    return False

def play_random_audio(folder_path):
    audio_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.ogg'))]
    if not audio_files:
        print("No audio files found in the specified folder.")
        return None
    random_audio = random.choice(audio_files)
    print(f"Playing: {random_audio}")
    pygame.mixer.music.load(os.path.join(folder_path, random_audio))
    pygame.mixer.music.play()
    return random_audio

random_audio_playing = False
manual_audio_detected = False
current_audio = None
silence_start_time = None

while True:
    if is_audio_playing():
        if random_audio_playing:
            print("Manual audio detected. Pausing random audio.")
            pygame.mixer.music.pause()
            random_audio_playing = False
        manual_audio_detected = True
        silence_start_time = None
    else:
        if not manual_audio_detected:
            if silence_start_time is None:
                silence_start_time = time.time()
            
            if time.time() - silence_start_time >= AUDIO_PLAY_DELAY:
                if not random_audio_playing and not pygame.mixer.music.get_busy():
                    if current_audio and pygame.mixer.music.get_pos() > 0:
                        print("No manual audio detected. Resuming current random audio.")
                        pygame.mixer.music.unpause()
                    else:
                        print("No manual audio detected. Playing new random audio.")
                        current_audio = play_random_audio(AUDIO_FOLDER)
                    random_audio_playing = True
                elif random_audio_playing and not pygame.mixer.music.get_busy():
                    print("Random audio ended. Playing another random audio.")
                    current_audio = play_random_audio(AUDIO_FOLDER)
        else:
            manual_audio_detected = False

    time.sleep(1)
