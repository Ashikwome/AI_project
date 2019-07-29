import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int (datetime.datetime.now().hour)

    if hour >= 0 and hour<= 12:
        speak("good Morning")

    elif hour >= 12 and hour<= 18:
        speak ("Good Afternoon")

    else:
        speak ("Good Evening")

    speak("I am your Jarvis sir please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and output will be string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print (f"User said:{query}\n")

    except Exception as e:
        print(e)
        print ("Say that aganin please....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ashikintalha@gmail.com', 'pythonforjarvis')
    server.sendmail('ashikintalha@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for excuting the task
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'G:\\Music World\\Mp3\\Random'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'who are you' in query:
            speak ('Sir,  I am Jarvis I was Made by AShikin Talha Wome , Mehreen Rahman abonty')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'code' in query:
            codePath = "C:\\Users\\talha\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "ashikwome6@gmail.com"
                sendEmail(to,content)
                speak("Email hasbeen sent")
            except Exception as e:
                print(e)
                speak("I am unable to send the mail")

        elif 'exit' in query:
            speak('Bye Sir , See you soon')
            break

        elif 'shutdown' in query:
            speak('Bye Sir , See you soon')
            break