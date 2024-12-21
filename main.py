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
        elif 'joke' in query:
            speak("ok")
            tell_joke()


        
        
 