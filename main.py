import pyaudio
import speech_recognition as sr
import subprocess
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import time
import smtplib
import os
from os import system
from googlesearch import search
def speak(text):
    system("say {}".format(text))

def wishMe():
   hour = int(datetime.datetime.now().hour)
   if(hour>=0 and hour<=12):
       speak("Good Morning!")
   elif hour>=12 and hour<17:
       speak("Good Afternoon")
   else:
       speak("Good Evening")

   speak("I am JARVIS, sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print("User said: ",query)

        except Exception as e:
            #print(e)
            print("Say that again please...")
            return "None"

        return query

def sendEmail(to,emailContent):
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.connect("smtp.gmail.com",587)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login("youremail@gmail.com", "yourpassword")
      server.sendmail("youremail@gmail.com", to, emailContent)
      server.quit()

def sendWhatsappMsg(to,msg,hr,min):
      pywhatkit.sendwhatmsg(to,msg,hr,min)
      
def searchGoogle(search_query):
      for i in search(search_query,tld='co.in',lang='en',num=20,stop=20,pause=2.0):
          print(i)

def tellJoke(text):
    speak(text)

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        contacts = {'Varun':'+91XXXXXXXXXX','Abhi':'+91XXXXXXXXXX', 'Rohan':'+91XXXXXXXXXX','Aman':'+91XXXXXXXXXX'} # Contact-List
        #Code for automating tasks based on query/user's command
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.get(chrome_path).open('https://www.youtube.com')

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.get(chrome_path).open('https://www.google.com')

        elif 'open stackoverflow' in query:
            speak("Opening StackOverflow")
            webbrowser.get(chrome_path).open('https://www.stackoverflow.com')

        #elif 'play music' in query:
        #    music_dir = 'Path Location'
        #    songs = os.listdir(music_dir)
        #    print(songs)
        #   os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code")
            os.system('open /Applications/Visual\ Studio\ Code.app')

        elif 'open android studio' in query:
            speak("Opening Android Studio")
            os.system('open /Applications/Android\ Studio.app')

        elif 'email to Rohan' in query:
            try:
                speak("What should i send?")
                emailContent = takeCommand()
                to = "rohan123@gmail.com"
                sendEmail(to,emailContent)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry sir, Not able to send the email at this moment")

        elif 'created you' in query:
            speak("Hello I am JARVIS and I am a virtual assistant. I have been created by Trishit")

        elif 'who are you' in query:
            speak("Hello I am JARVIS and I am a virtual assistant. I have been created by Trishit")
        
        elif 'whatsapp' in query:
            speak('To whom should I send the message?')
            receiver = takeCommand().lower()
            speak('What should I send?')
            message = takeCommand()
            speak('When should i send? Please mention the hour')
            hour = int(takeCommand())
            speak('Please mention the minute')
            minute = int(takeCommand())
            h = int(datetime.datetime.now().hour)
            m = int(datetime.datetime.now().minute)
            rem_hour = hour-h
            rem_min = minute-m
            speak(f"Your message will be sent in {rem_hour} hours {rem_min} minutes")
            sendWhatsappMsg(contacts[receiver],message,hour,minute)

        elif 'search' in query:
            speak('What do you want to search?')
            subject = takeCommand()
            speak('Searching in Google')
            speak('These are the results I have found related to your search')
            searchGoogle(subject)

        elif 'joke' in query:
            joke = pyjokes.get_joke(language="en",category="all")
            print(joke)
            tellJoke(joke)

        elif 'reminder' in query:
            speak("What shall I remind you about?")
            reminder = takeCommand()
            speak("In how many minutes should I remind you Sir?")
            reminder_time = int(takeCommand())
            reminder_time = reminder_time * 60
            speak(f"Setting reminder for {reminder_time} seconds from now")
            time.sleep(reminder_time)
            reminder = reminder.replace("I","You")
            reminder = reminder.replace("my","your")
            speak(f"Sir, This is a reminder for you. {reminder}")

    
        elif 'play my favourite song' in query:
            speak("Playing your favourite song, Sir")
            webbrowser.get(chrome_path).open('https://www.youtube.com/watch?v=hoNb6HuNmU0')

        elif 'thank you' in query:
            speak('Not a problem sir!')

        elif 'quit' in query:
            speak("GoodBye Sir. Have a nice day")
            exit()

            
