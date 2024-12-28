from pickle import TRUE
import speech_recognition as sr
import pyttsx3
import requests 
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
import sys
from gtts import gTTS

from fastapi import FastAPI



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
    speak("I am Makki , how may I help you?")

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
def get_weather(city):
    api_key = "60780f2ca3d954588691968b80e4145d"  # Replace with your API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        weather_info = f"The current temperature in {city} is {temperature}°C with {description}."
        return weather_info
    else:
        return "Sorry, I couldn't fetch the weather information. Please check the city name."
try:
    def check_internet_speed():
        st = speedtest.Speedtest()

        print("Finding best server...")
        st.get_best_server()

        print("Measuring download speed...")
        download_speed = st.download() / 1_000_000  # Convert from bits to Mbps

        print("Measuring upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert from bits to Mbps

        print("Measuring ping...")
        ping = st.results.ping

        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping:.2f} ms")
except Exception as e:
    speak("try again")




if __name__ == "__main__":
    wishMe()

    while True:
    #if 1:
        query=takeCommand().lower()
    
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
            while True:
                how=takeCommand()
                try:
                    if 'exit' in how or 'close' in how or 'quit' in how or 'leave' in how:
                        speak("ok sir! The how to do mode is closed")
                        sys.close()
                    else:
                        how=takeCommand()
                        max_results = 1
                        how_to= search_wikihow(how, max_results,lang='en')
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
            speak(joke)
            if 'exit' in query:
                sys.close()
            
            

        elif 'tell weather ' in query:
            speak("the current weather is ")
            w=get_weather()
            print(w)
            speak(w)

        elif 'inernet speed ' in query:
            i = check_internet_speed()
            speak(i)

        elif 'why' or 'what' or 'where' or 'who' or 'when' in query:
            w5 = search_on_google()
            print(w5)
            speak(w5)


'''def set_alarm():
    # Ask the user for the alarm time in HH:MM format
    alarm_time = input("Enter the alarm time (HH:MM, 24-hour format): ")

    try:
        # Parse the alarm time
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        print(f"Alarm is set for {alarm_hour:02d}:{alarm_minute:02d}.")

        while True:
            # Get the current time
            now = datetime.now()
            current_hour = now.hour
            current_minute = now.minute

            # Check if it's time for the alarm
            if current_hour == alarm_hour and current_minute == alarm_minute:
                print("Wake up! It's time!")
                speak("Wake up! It's time!")
                
                # Play an alarm sound (Optional)
                playsound("alarm.mp3")  # Replace "alarm.mp3" with your sound file
                break
            
            # Sleep for 30 seconds before checking again
            time.sleep(30)

    except ValueError:
        print("Invalid time format. Please enter in HH:MM format.")
        speak("Invalid time format. Please enter in HH:MM format.")

if __name__ == "__main__":
    set_alarm()'''
        

        

        
        
 
