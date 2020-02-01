# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import speech_recognition as sr

sr.__version__

harvard = sr.AudioFile('harvard.wav')
r = sr.Recognizer()
with harvard as source:
    audio = r.record(source) #audio = r.record(source, duration=4)
    print(type(audio))


r.recognize_google(audio)
