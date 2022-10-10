from cmath import phase
from email.mime import audio
import imp
from mimetypes import init
from socket import timeout
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
#import pywhatkit as kit
import sys
import pyjokes


engine = pyttsx3.init('sapi5')
Voices = engine.getProperty('voices')

engine.setProperty('voices', Voices[1].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"user said: {query}")

    except Exception as e:
        speak ("Say that again please....")
        return "none"
    return query


#wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning, ")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon, ")
    else:
        speak("Good Evening,")
    speak("I am Xclipse, please tell me how can i help you")

if __name__ == "__main__":
    wish()
    while True:
    #if 1:
       query = takecommand().lower() 

       #logic building

       if "open cmd" in query:
           os.system("start cmd")


       elif "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

       elif "open camera" in query:
           cap = cv2.VideoCapture(0)
           while True:
               ret, img = cap.read()
               cv2.imshow('webcam', img)
               k = cv2.waitKey(50)
               if k == 27:
                   break;
           cap.release()    
           cv2.destroyAllWindows()

       elif "play music" in query:
           music_dir= "D:\\Music"
           songs = os.listdir(music_dir)
           #rd = random.choice(songs)
           for song in songs:
               if song.endswith('.mp3'):
                   os.startfile(os.path.join(music_dir, song))

       elif "ip address" in query:
           ip = get('https://api.ipify.org').text
           speak(f"Your IP address is {ip}")


       elif "wikipedia" in query:
           speak("searching wikipedia...")
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("according to wikipedia")
           speak(results)
           #print(results)

       elif "open youtube" in query:
           webbrowser.open("www.youtube.com")


       elif "open facebook" in query:
           webbrowser.open("www.facebook.com")


       elif "open instagram" in query:
           webbrowser.open("www.instagram.com")


       elif "open google" in query:
           speak("what should i search on google")
           cm = takecommand().lower()
           webbrowser.open(f"{cm}")

   
       #elif "send message" in query:
         #  kit.sendwhatmsg("+918--1534290", "Hello this is Xclipse",2,25)


       elif "no thanks" in query:
           speak("thanks for using me, have a good day")
           sys.exit()



       elif "close notepad" in query:
           speak("okay, closing notepad")
           os.system("taskkill/f /im notepad.exe")

















       speak("Do you have any other work") 

       











