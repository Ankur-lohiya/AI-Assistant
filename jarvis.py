import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)


def date():
    year=int(datetime.datetime.now().year)
    mon=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(date)
    speak(mon)
    speak(year)


def wishMe():
    speak("Welcome back sir!")
    speak("the current time is")
    time()
    speak("the today's date is")
    date()
    speak("How can i help you?")

# wishMe()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language="en-in")
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again")
        return "Home"

    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('chutiyapagooogle.782@gmail.com','sxaiuvkeynfcporp')
    server.sendmail('chutiyapagooogle.782@gmail.com',to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save('G:\jarvis-python\ss.png')

def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery=psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__=="__main__":
    # wishMe()
    while True:
        query=takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should I send")
                content=takeCommand()
                to='deepankur1002.cse18@chitkara.edu.in'
                sendEmail(to,content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'search in chrome' in query:
            speak('what should I search')
            chromepath='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        
        elif 'logout' in query:
            os.system('shutdown -1')

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        elif 'play songs' in query:
            songs=os.listdir('G:\music')
            os.startfile(os.path.join('G:\music',songs[0]))

        elif 'remember that' in query:
            speak('What should I remember?')
            data=takeCommand()
            speak('you said me to remember'+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you remember anything' in query:
            remember=open('data.txt','r')
            speak(remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak('screenchot taken')

        elif 'cpu' in query:
            cpu();

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            quit()