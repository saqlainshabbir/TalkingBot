import speech_recognition as sr
from gtts import gTTS
import pyttsx3

engine = pyttsx3.init()

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)
    data = recognizer.recognize_sphinx(audio)
    engine.say(data)
    engine.runAndWait()
    print(data)