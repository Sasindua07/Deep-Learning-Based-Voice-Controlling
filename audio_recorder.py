import sounddevice as sd 
import numpy as np
from scipy.io.wavfile import write

i=0

for i in range(40,50):
    category = "red"
    file_name = "red_" + str(i)
    duration = 1
    fs = 22050
    print("Speak Now -> " , category, i)
    sd.default.device = 0
    audio_rec = sd.rec (int(duration * fs), samplerate = fs, channels = 1)

    sd.wait()
    int_audio = (np.clip(audio_rec, -32768,32767)) * 32767

    write("data/" + category + "/" + file_name + ".wav", fs, int_audio.astype(np.int16))

    print("Recorded ->")
