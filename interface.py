import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb

friday=pyttsx3.init()
voice=friday.getProperty("voices")
friday.setProperty('voice',voice[1].id)

def speak(audio):
    print("SUPPER AL7702 : "+audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak(Time)
time()
def welcome():
    hour= datetime.datetime.now().hour
    if hour>=6 and hour<12 :
        speak("good morning sir")
    elif hour>=12 and hour<18 :
        speak("good afternoon sir")  
    elif hour>=18 and hour<24 :
        speak("good night sir") 
    speak("how can i help you")

def comand():
    c=sr.Recognizer()
    with sr.Microphone() as source :
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language="en") 
        print("User: "+ query)  
    except sr.UnknownValueError :
        speak ("please repeat or typing the comment") 
        query=str(input("Your order is : "))   
    return query    

if __name__ == "__main__":
    welcome()
    while True :
        query = comand().lower()
        if "i want to listen to music" in query:
            speak("ok welcome to the music")
            import subprocess
            subprocess.run(["c:/Users/LENOVO/pyvision/env/Scripts/python.exe", "music.py"]) 
        if "i want to play game" in query:
            speak("Welcome to the game enviroment.")
            speak("Please fill infomation about you for me")
            import subprocess
            subprocess.run(["c:/Users/LENOVO/pyvision/env/Scripts/python.exe", "game.py"])         
         

            
            
