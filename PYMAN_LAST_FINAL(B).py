from tkinter import *
from textblob import TextBlob
from PIL import ImageTk 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wk
import subprocess
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Audio_process():
    
    
    def take_Audio():
        global request1
        r = sr.Recognizer()
        intro()
        with sr.Microphone() as source:
            try:
                text_var.set('Listening....')
                r.pause_threshold=1
                audio = r.listen(source)
                text_var.set('Recognizing....')
                request1 = r.recognize_google(audio)
                
            except:
                pass
        return request1
   
    while True:
        
        Audio_rec = take_Audio().lower()
        print(Audio_rec)
        if "time" in Audio_rec:
            time()
            break
        
        elif "date" in Audio_rec:
            date()
            break
            
        elif "check" in Audio_rec:
            def check():
                giv_word = e.get()
                cor_word = TextBlob(giv_word)
                corrected_text = Label(root, text=str(cor_word.correct()))
                corrected_text.pack()

            root = Tk()
            root.title('SpellCheck')
            root.geometry('400x200')

            head = Label(root, text='SpellCheck',font=('helvetica', 14 , 'bold'))
            head.pack()
            e = Entry(root, width=200,borderwidth=5)
            e.pack()
            b = Button(root, text = 'Check', font=('helvetica', 8 , 'bold'), fg = 'white', bg = 'brown', command = check)
            b.pack()
            root.mainloop()
                    
            break
        
        elif "microsoft edge" in Audio_rec:
            def app():
                subprocess.call("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe")
            app()
            break

        elif "wikipedia" in Audio_rec:
            speak("Searching....")
            Audio_rec = Audio_rec.replace("wikipedia", " ")
            result = wk.summary(Audio_rec, sentences=2)
            speak(result)
            break
        elif "chrome" in Audio_rec:
            subprocess.call("C://Program Files//Google//Chrome//Application//chrome.exe")
            break
        elif "remember" in Audio_rec:
            speak("what should i remember?")
            data = take_Audio()
            speak("you said me to remember" + data)
            remember = open("data1.txt", "w")
            remember.write(data)
            remember.close()


        elif "do you know anything" in Audio_rec:
            remember = open("data1.txt", "r")
            speak("you said me to remember that " + remember.read())
            break


        elif "calculator" in Audio_rec:
            subprocess.call("C://Windows//System32//calc.exe")
            break
        elif "pycharm" in Audio_rec:
            subprocess.call("C://Program Files//JetBrains//PyCharm Community Edition 2021.1.2//bin//pycharm64.exe")
            break
        elif "close chrome" in Audio_rec:
            os.system("taskkill /f /im  chrome.exe")
            break
        elif "close browser" in Audio_rec:
            os.system("taskkill /f /im msedge.exe")
        

        elif "turn off" in Audio_rec:
            quit()

def time():
    time_outp = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time_outp)
    
def date():
    year_outp = int(datetime.datetime.now().year)
    month_outp = int(datetime.datetime.now().month)
    date_outp = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date_outp)
    speak(month_outp)
    speak(year_outp)

def intro():
    speak("hello sir")
    hour = datetime.datetime.now().hour

    if 6 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    elif 18 <= hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("How can I help you?")
    
root = Tk()
mic_window = Toplevel()
mic_window.geometry('800x450')
mic_window.title("Mini Voice Assistant")
mic_window.iconbitmap('icon.ico')
mic_window.config(bg='lightgrey')
mic_window.resizable(0, 0)
operator = ""
text_input = StringVar()
text_var = StringVar()

mic_window.bg = ImageTk.PhotoImage(file='back.jpg')
mic_window.bg_image = Label(mic_window, image=mic_window.bg).place(x=0, y=0, relwidth=1, relheight=1)

canvas = Canvas(mic_window, width=399, height=120)
canvas.place(x=190, y=6)
photoi = PhotoImage(file='logo.png')
canvas.create_image(0, 0, anchor=NW, image=photoi)

canvas1 = Canvas(mic_window, width=397, height=171)
canvas1.place(x=190, y=260)
photoi1 = PhotoImage(file='commands1.png')
canvas1.create_image(0, 0, anchor=NW, image=photoi1)

queryLabel = Label(mic_window, text='SPEAK', font=('helvetica', 12, 'bold'), bg='#f7f732')
queryLabel.place(x=360, y=150)

text_var.set('')
lbl_var = Label(mic_window, textvariable=text_var, font='helvetica 10 bold', bg='lightgrey')
lbl_var.place(x=320, y=225, width=150)

micImage = PhotoImage(file='mic.png')
micButton = Button(mic_window, image=micImage, command=Audio_process, bg='lightgrey', bd=0, cursor='hand2',
                   activebackground='lightgrey')
micButton.place(x=375, y=184)

root.withdraw()
root.mainloop()
