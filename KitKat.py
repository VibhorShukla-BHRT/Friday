import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit
import pyjokes


d1 = {'vibhor':'shukla.vibhor495@gmail.com', 'rahul sir': 'rahul15.mdgr@gmail.com','didi':'bs.bhavya2003@gmail.com','mummy':'rajeshwarishukla99121@gmail.com','daddy':'gyanendrashukla0200@gmail.com','vibhor shukla':'shukla.vibhor9938@gmail.com'}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
# print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print("Good morning bosss!")
        speak("Good morning bosss!")
    elif hour>=12 and hour<=18:
        print("Good Afternoon BOss!")
        speak("Good Afternoon BOss!")
    elif hour>=18 and hour<=22:
        print("Good evening boss!")
        speak("Good evening boss!")
    else:
        print("Greeetings boss! It's midnight!.")
        speak("Greeetings boss! It's midnight!.")
    print("Howw may I help You?")
    speak("Howw may I help You?")

def closure():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print("Friday : Thank you Sir! Have a nice day!")
        speak("Thank you Sir! Have a nice day!")
    elif hour>=12 and hour<=18:
        print("Friday : Thank you sir! Have a wonderful day!")
        speak("Thank you sir! Have a wonderful day!")
    elif hour>=18 and hour<=22:
        print("Friday : Thank you sir! Good Night...See you in dreams...")
        speak("Thank you sir! Good Night...See you in dreams...")
    else:
        print("Friday : Thank you Sir...For using me...it's time to sleep...")
        speak("Thank you Sir...For using me...it's time to sleep...")
# wishme()
# if __name__ == '__main__':
#     speak("Hello Boss!, I am Friday.")

def takecommand():
   r = sr.Recognizer()
   with sr.Microphone() as sourse:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(sourse)

   try:
       print("Recognising...")
       query = r.recognize_google(audio, language='en-in')
       print(f"User Said: {query}\n ")
   except Exception as e:
       # print(e)
       print("See that again please...")
       return "None"
   return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shukla.vibhor495@gmail.com', 'vibhor!@#')
    server.sendmail('shukla.vibhor495@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching...Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open github" in query:
            webbrowser.open("github.com")


        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open typing test" in query:
            webbrowser.open("https://www.google.com/search?q=typing+test&rlz=1C1CHBF_enIN886IN886&oq=typing+&aqs=chrome.2.69i57j0i433l2j0j0i433l3j0j0i433l2.7407j0j15&sourceid=chrome&ie=UTF-8")


        elif "open geeksforgeeks" in query:
            webbrowser.open("www.geeksforgeeks.org")

        elif "play chess" in query:
            webbrowser.open("lichess.org")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif "open pycharm" in query:
            pyPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(pyPath)

        elif "open chrome" in query:
            chPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chPath)

        elif "open intellij idea" in query:
            inPath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.1\\bin\\idea64.exe"
            os.startfile(inPath)

        elif "open blender" in query:
            blPath = "C:\\Program Files\\Blender Foundation\\Blender 2.91\\blender.exe"
            os.startfile(blPath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "play music" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            x = len(songs)
            y = random.randrange(x)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[y]))

        elif "on youtube" in query:
            song0 = query.replace('play', '')
            song1 = song0.replace('on youtube', '')
            print(song1)
            speak('playing' + song1 + 'on youtube')
            pywhatkit.playonyt(song1)

        elif 'quit' in query:
            closure()
            break

        elif "email to " in query:
            if 'vibhor' in query:
                try:
                    speak("what should I say sir?")
                    content = takecommand()
                    to = d1['vibhor']
                    sendEmail(to, content)
                    print("Email has been sent!")
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Master Vibhor! I couldn't send the email!")
            elif 'didi' in query:
                try:
                    speak("what should I say sir?")
                    content = takecommand()
                    to = d1['didi']
                    sendEmail(to, content)
                    print("Email has been sent!")
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Master Vibhor! I couldn't send the email!")
            elif 'vibhor shukla' in query:
                try:
                    speak("what should I say sir?")
                    content = takecommand()
                    to = d1['vibhor shukla']
                    sendEmail(to, content)
                    print("Email has been sent!")
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Master Vibhor! I couldn't send the email!")
            elif 'daddy' in query:
                try:
                    speak("what should I say sir?")
                    content = takecommand()
                    to = d1['daddy']
                    sendEmail(to, content)
                    print("Email has been sent!")
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Master Vibhor! I couldn't send the email!")
            elif 'mummy' in query:
                try:
                    speak("what should I say sir?")
                    content = takecommand()
                    to = d1['mummy']
                    sendEmail(to, content)
                    print("Email has been sent!")
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Master Vibhor! I couldn't send the email!")
            elif 'rahul sir' in query:
                try:
                    speak("what should I say sir?")
                    content = takecommand()
                    to = d1['rahul sir']
                    sendEmail(to, content)
                    print("Email has been sent!")
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Master Vibhor! I couldn't send the email!")

        elif 'i love you' in query:
            speak("But I love only Masterr Vibhor...so Fuck off!")

        elif 'my love is friday' in query:
            speak('I love you toooo master...')

        elif 'will you marry' in query:
            speak('If I was human I would have married you...')
        elif "play my life" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[4]))


        elif "play believer" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "play immigrant" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif "play jeet" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif "play legends never die" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif "play cold" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[5]))

        elif "play destiny" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[6]))

        elif "play fight back" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[7]))

        elif "play grateful" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[8]))

        elif "play life" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[9]))

        elif "play never give up" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[10]))

        elif "play best of me" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[11]))

        elif "play pirates of caribbean" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[12]))

        elif "play radha rani" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[13]))

        elif "play rider" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[14]))

        elif "play scam" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[15]))

        elif "play tum prem ho" in query:
            music_dir = 'C:\\Users\\Rimjhim2003\\Desktop\\Vibhor\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[16]))