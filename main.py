from jarvisgui3 import Ui_MainWindow 
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
from os import listdir
from os.path import isfile, join
import shutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

#alarm
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    with open("alarm.py", 'r') as file:
        python_code =file.read()
        exec(python_code)
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")
    
wishMe()

speak("I am Jarvis mam. Please tell me how may I help you")


class MainThread(QThread):
    
    def _init_(self):
        super(MainThread, self).__init()

    def run(self):
        self.Task_Gui()

    def takeCommand(self):
        # It takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return self.query

    def Task_Gui(self):
        
        while True:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'shutdown' in self.query:
                os.system("shutdown/s /t 1")
            
            elif 'open youtube' in self.query:
                speak("launching mam")
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                speak("launching mam")
                webbrowser.open("google.com")

            elif 'open stack overflow' in self.query:
                speak("launching mam")
                webbrowser.open("stackoverflow.com")   

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f",Mam the time is {strTime}")

            elif 'open code' in self.query:
                codePath = "C:\jarvis2.0\jarvisgui3.py"
                os.startfile(codePath)

            elif 'hello ' in self.query:
                    speak("Hello sir, how are you ?")
            elif "i am fine" or "i am good" in self.query:
                speak("that's great, mam")
            elif "how are you" in self.query:
                speak("Perfect, mam")
            elif "thank you" in self.query:
                speak("you are welcome, mam")

            elif 'quit' in self.query:
                speak("bye mam, I hope you have a nice day. If you need me I am right here")

            elif 'good' in self.query:
                speak("Thank you mam, I am glad I could help")

            elif 'suggest me some songs' in self.query:
                speak("ok mam here are some newly launched songs")
                webbrowser.open("https://bit.ly/3UXwqg2")

            elif 'wish me' in self.query:
                 
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    speak("Good Morning mam. Its nice to see you.")

                elif hour>=12 and hour<18:
                    speak("Good Afternoon mam. Its nice to see you")   

                else:
                    speak("Good Evening mam. Its nice to see you")

            elif 'can you sing' in self.query:
                speak("Haha, no mam i can't.But i can suggest you som songs if you want.")
 
            elif "set an alarm" in self.query:
                print("input time example:- 10 and 10 and 10")
                speak("Set the time")
                a = input("Please tell the time :- ")
                alarm(a)
                speak("Done,sir")

            elif "play a game" in self.query:
                    from game import game_play
                    game_play()
             
            elif "folder" in self.query:
                speak("Opening")
                with open("sorting.py", 'r') as file:
                    sort_code =file.read()
                    exec(sort_code)

               

startFunction = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        self.jarvis_ui.movies_2 = QtGui.QMovie("C:\jarvis2.0\GUI_jarvis\Iron_Template_1.gif")
        self.jarvis_ui.iron_man.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_2 = QtGui.QMovie("C:\jarvis2.0\GUI_jarvis\Siri_1.gif")
        self.jarvis_ui.voice_rec.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_2 = QtGui.QMovie("C:\jarvis2.0\GUI_jarvis\initial.gif")
        self.jarvis_ui.initial.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_2 = QtGui.QMovie("C:\jarvis2.0\GUI_jarvis\B.G_Template_1.gif")
        self.jarvis_ui.code1.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_2 = QtGui.QMovie("C:\jarvis2.0\GUI_jarvis\Health_Template.gif")
        self.jarvis_ui.human.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_2 = QtGui.QMovie("C:\jarvis2.0\GUI_jarvis\Code_Template.gif")
        self.jarvis_ui.label_7.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        startFunction.start()


Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())