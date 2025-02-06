import pygame
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import subprocess

# Tạo AI 
friday=pyttsx3.init()
voice=friday.getProperty("voices")
friday.setProperty('voice',voice[1].id)

def speak(audio):
    print("SUPPER MUSIC : "+audio)
    friday.say(audio)
    friday.runAndWait()

def comand():
    c=sr.Recognizer()
    with sr.Microphone() as source :
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language="en") 
        print("User: "+ query)  
    except sr.UnknownValueError :
        print ("please repeat or typing the comment") 
        query=str(input("Your order is : "))   
    return query

# lựa chọn topic 
def topic_music():
    speak("happy or sad ")
    c=str(input("Enter your choose : "))
    if c == "happy" :
        speak("ok")
        speak("i have 2 music 'I do' or 'Diva troll' , chosse one ")
        speak("If there is no song you like, you can go back to YouTube ")
        subprocess.run(["c:/Users/LENOVO/pyvision/env/Scripts/python.exe", "file_music.py"])             
    elif c=="sad" :
        speak("ok")
        speak("i have 2 music 'See you again' or 'We don't talk anymore' , chosse one") 
        speak("If there is no song you like, you can go back to YouTube ") 
        subprocess.run(["c:/Users/LENOVO/pyvision/env/Scripts/python.exe", "file_music.py"])      

#Tạo khung chọn lựa 
if __name__ == "__main__":
     speak("You want lisen to music at here or youtube")
     while True:
        query = comand().lower()
        if "youtube" in query:
            speak("OK see you again ")
            wb.open("https://www.youtube.com/")  # Mở trình duyệt và chuyển hướng đến YouTube
            break  
        elif "one" in query:
            topic_music()
            break  # Thoát khỏi vòng lặp sau khi phát nhạc
        else :
            speak("Ok cook")


            