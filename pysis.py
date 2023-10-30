import speech_recognition as sr
from datetime import datetime
import time
import webbrowser
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("I can't understand :(")
        except sr.RequestError:
            speak("System doesn't work.")
        return voice

def response(voice):
    if 'how are you' in voice:
        speak("Thank you, I'm good")
    if 'say hello' in voice:
        speak("Hello Muhammed Hossein")
    if 'who are you' in voice:
        speak("I am Asif's assistant, pysis")
    if "what time is it" in voice:
        time_str = datetime.now().strftime('%H:%M:%S')
        speak("Time is: " + time_str)  # Corrected this line
    if 'search' in voice:
        search = record("What do you want to search?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('For ' + search + ', I found')  # Corrected these lines
    if 'quit' in voice:
        speak('Ok')
        exit()
    if 'completed' in voice:  # Corrected this line
        speak('Ok')
        exit()
    if 'goodbye' in voice:
        speak('Ok')
        exit()
    

def speak(string):
   tts = gTTS(string,lang='en')
   rand = random.randint(1,10000)
   file = 'audio-'+str(rand)+'.mp3'  
   tts.save(file)
   playsound(file)
   os.remove(file)

speak("How can I help you today?")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
    

