import tkinter as tk
import subprocess
import pyttsx3
import speech_recognition as sr

# Tạo AI
friday = pyttsx3.init()
voice = friday.getProperty("voices")
friday.setProperty('voice', voice[1].id)

def speak(audio):
    print("BOTGAME : " + audio)
    friday.say(audio)
    friday.runAndWait()

def comand():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language="en")
        print("User: " + query)
        return query
    except sr.UnknownValueError:
        print("Please repeat or type the command")
        return input("Your order is: ")

# Khởi tạo
name = str.lower(input("Enter your name: "))
age = int(input("Enter your age: "))

# Xác minh độ tuổi
def policy():
    if age < 18:
        speak("You are not allowed to participate in the game.")
        not_age()
    else:
        speak("You are allowed to participate in the game.")
        speak_er()
        subprocess.run(["c:/Users/LENOVO/pyvision/env/Scripts/python.exe", "gamesnack.py"])

# Nếu không đủ tuổi, có thể tham gia trò chơi cho trẻ em
def not_age():
    speak("Do you want to participate in the game for the children?")
    speak("Thank you for using my service.")
    speak("If you don't play the game, would you like to listen to music?")
    option_two = str.lower(input("Enter your option Yes/No: "))
    if option_two == "yes":
        subprocess.run(["c:/Users/LENOVO/pyvision/env/Scripts/python.exe", "music.py"])
    else:
        speak("Goodbye and see you again.")
def speak_er():
    speak("no no no ")        
   

policy()
