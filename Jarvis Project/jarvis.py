import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import smtplib

 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis sir, plese tell me how may i help you")


def takeCommand():
    #It takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listen...")
        r.pause_threshold = 2
        audio = r.listen(source)
        
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tpac08600@gmail.com', 'tpac@123')
    server.sendmail('tpac08600@gmail.com', to, content)
    server.close()
    

if __name__== "__main__":
    # speak("Reena is a good girl....Hello ever yone i am reena maurya")
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #Login for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube'  in query:
            webbrowser.open("youtube.com")
            
        elif 'open google'  in query:
            webbrowser.open("google.com")
            
        elif 'open internshala'  in query:
            webbrowser.open("internshala.com")
            
        elif 'open udemy'  in query:
            webbrowser.open("udemy.com")
            
        elif 'play music' in query:
            music_dir = 'D:\\WEBSITE DEVELOPMENT course\\JS\\M6'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 
            
        elif 'email to reena' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "tpac08600@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent susseccfully !")
            except Exception as e:
                print(e)
                speak("Sorry didi. I am not ablel to send this email.")

        elif 'stop' in query:
            exit()



