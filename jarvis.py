import  pyttsx3
import datetime
import speech_recognition as sr
import  wikipedia
import  webbrowser
import  os
import  smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good evening sir")
    print("I am Jarvis sir Please tell me how can i will help you sir")
    speak("I am Jarvis sir Please tell me how can i will help you sir")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:

        print("Say That Again Please")
        return "None"
    return  query






if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()


   #logic for execution

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'play music' in query:
            music_dir='E:\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time 'in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime} ")
        elif 'linkedin' in query:
            webbrowser.open("https://in.linkedin.com/")
        elif 'play song in youtube':

            webbrowser.open('https://youtu.be/Xtqe5i5ulp4')
        elif'shut down the system':
            os.system("shutdown /s /t 5")



