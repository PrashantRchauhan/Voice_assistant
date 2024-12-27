from pickle import TRUE
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser 
import os
import pywhatkit as kit
import smtplib
import tkinter as tk
import calendar
import pyjokes
import psutil
from pywikihow import WikiHow, search_wikihow
import speedtest

paths={ 
    "notepad" : "C:\\Windows\\notepad.exe",
    "wordpad" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Wordpad.lnk",
    "chrome"  : "C:\\Users\\Public\\Desktop\\Google Chrome.lnk",       
    "turboc"  : "C:\\Users\\Public\\Desktop\\Turbo C++.lnk",
}

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning sir!")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I am Jarvis , how may I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listnening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

def notepad():
    os.startfile(paths["notepad"])
def chrome():
    os.startfile(paths["chrome"])
def wordpad():
    os.startfile(paths["wordpad"])
def turboc():
    os.startfile(paths["turboc"])
def send_whatsapp_message(number,message):
    kit.sendwhatmsg_instantly(f"+91{number}",message)
def play_on_youtube(video):
    kit.playonyt(video)
def search_on_google(text):
    kit.search(text)
def search_wikihow(query,max_results=10,lang='en'):
    return list(WikiHow.search(query,max_results,lang))

if __name__ == "__main__":
    wishMe()

    #while True:
    query=takeCommand().lower()
    if 1:
        if 'open google' in query:
            speak("openning google")
            webbrowser.open("google.com")

        elif 'open chrome' in query:
            speak("opening")
            chrome()
        elif 'open notepad' in query:
            speak("opening")
            notepad()
        elif 'open wordpad' in query:
            speak("opening")
            wordpad()
        elif 'open turbo c' in query:
            speak("opening")
            turboc()
        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)
        elif 'the date' in query: 
            datetime = datetime.datetime.now().strftime("%D%M%Y")
            print(datetime)
            speak(datetime)
        elif "send whatsapp message" in query or "send message on whatsapp" in query or "message on whatsapp" in query or "whatsapp message" in query or "send message" in query or "message" in query:
            speak("on what number you want to send message sir? please tell the number:")
            number=takeCommand().lower()
            speak("what is the message sir!")
            message=takeCommand().lower()
            send_whatsapp_message(number,message)
            speak("sent successfully!")
        elif 'play video on youtube' in query:
            speak("what do you want to play sir!")
            video = takeCommand().lower()
            play_on_youtube(video)
        elif 'search on google' in query:
            speak("what you want to search")
            text = takeCommand().lower()
            search_on_google(text)

        elif 'check battery percentage' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have{percentage} percent battery")
        
        
        elif 'how to ' in query:
            speak("how to do mode is activated !")
            while True:
                speak("what do you want to know sir !")
                how=takeCommand()
                try:
                    if 'exit' in how or 'close' in how or 'quit' in how or 'leave' in how:
                        speak("ok sir! The how to do mode is closed")
                    else:
                        how=takeCommand()
                        max_results = 1
                        how_to= search_wikihow(how, max_results)
                        assert len(how_to)==1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir ! i am not able to find this")

        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            d1 = st.download()
            up = st.upload()
            speak(f"sir we have {d1} bit per second downloading speed and {up} bit per second uploading speed")

        elif ' tell jokes ' or 'jokes' in query:
            joke = pyjokes.get_joke()
            print(joke)
            joke = pyjokes.get_joke(language='de')
            print(joke)
            joke = pyjokes.get_joke(category='neutral')
            print(joke)
        '''while True:
    command = input("Type 'joke' for a programming joke or 'exit' to quit: ").strip().lower()
    if command == 'joke':
        print(pyjokes.get_joke())
    elif command == 'exit':
        break
    else:
        print("Unknown command. Try 'joke' or 'exit'.")'''

        

        

        
        
 
