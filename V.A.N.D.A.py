import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")
    else:
        speak("Good Evening! Sir")

    speak("I WANDA is always present for your assistance sir, Command me ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"Sir said: {query}\n")

    except Exception as e:
        print("Sir please repeat that again!...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sanidhyamishra2005@gmail.com', 'your-password')
    server.sendmail('sanidhyamishra2005@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
       query = takeCommand().lower()

       if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)

       elif 'open youtube' in query:
           webbrowser.open("youtube.com")

       elif 'open google' in query:
           webbrowser.open("google.com")

       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")

       elif 'play music' in query:
           music_dir = 'D:\\Non Critical\\songs'
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir, songs[0]))

       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir, the time is {strTime}")

       elif 'open code' in query:
           codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)

       elif 'email to Sanidhya' in query:
           try:
               speak("What should I say?")
               content = takeCommand()
               to = "sanidhyamishra1808@gmail.com"
               sendEmail(to, content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("Sorry looks like. I am not able to send an e-mail at the moment")