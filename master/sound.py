import pydub
import numpy as np
import sounddevice as sd
import os


def read():
    filename = os.path.abspath('bad.wav')
    a = pydub.AudioSegment.from_mp3(filename)
    y = np.array(a.get_array_of_samples())
    return y


def playsound():
    sd.play(read(), 90100)
