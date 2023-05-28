import os
import datetime
import numpy as np
import sounddevice as sd
import wavio


#look up sounddevice to which device you want to use
sd.default.device = 1


fs = 44100
duration = 4 #seconds

print('recording...')

while True:
    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    directory = "./recordings/"
    filename = os.path.join(directory, filename + ".wav")
    wavio.write(filename, recording, fs, sampwidth=2)

    print(f"Recording saved as {filename}")