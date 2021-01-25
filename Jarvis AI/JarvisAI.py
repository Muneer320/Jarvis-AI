import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Jarvis your Personal A ssistant. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 700
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('muneer.alam320@gmail.com', 'mob.publications1@gmail.com')
    server.sendmail('muneer.alam320@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wiki' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            print("Opening Gmail...")
            speak("Opening Gmail")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/?gl=IN&tab=r1")
            print("Opening YouTube...")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("https://google.com/")
            print("Opening Google...")
            speak("Opening Google")

        elif 'open facebook' in query:
            webbrowser.open("https://facebook.com/")
            print("Opening FaceBook...")
            speak("Opening FaceBook")

        elif 'open instagram' in query:
            webbrowser.open("https://instagram.com/")
            print("Opening InstaGram...")
            speak("Opening InstaGram")

        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com/")
            print("Opening Twitter...")
            speak("Opening Twitter")

        elif 'open saavn' in query:
            webbrowser.open("https://jiosaavn.com/")
            print("Opening Jiosaavn...")
            speak("Opening Saavn")

        elif 'open spotify' in query:
            webbrowser.open("https://spotify.com/")
            print("Opening Spotify...")
            speak("Opening Spotify")

        elif 'open amazon' in query:
            webbrowser.open("https://amazon.com/")
            print("Opening Amazon...")
            speak("Opening Amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://flipkart.com/")
            print("Opening Flipkart...")
            speak("Opening Flipkart")

        elif 'open flipcart' in query:
            webbrowser.open("https://flipkart.com/")
            print("Opening Flipkart...")
            speak("Opening Flipkart")

        elif 'open snapdeal' in query:
            webbrowser.open("https://snapdeal.com/")
            print("Opening Snapdeal...")
            speak("Opening Snapdeal")

        elif 'open nykaa' in query:
            webbrowser.open("https://nykaa.com/")
            print("Opening Flipkart...")
            speak("Opening Flipkart")

        elif 'open myntra' in query:
            webbrowser.open("https://myntra.com/")
            print("Opening Myntra...")
            speak("Opening Myntra")

        #elif 'play music' in query:
            #print('No music found')
            #speak('No music found')
            #music_dir = 'E:\MP3\Lata'
            #songs = os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print("The time is: " + datetime.datetime.now().strftime("%H:%M:%S"))

        elif 'open code' in query:
            codePath = "C:\\Users\\munee\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening code")
            print("Opneing Code...")
            break

        elif 'open minecraft' in query:
            codePath = "C:\\Users\\munee\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(codePath)
            speak("Opening Minecraft")
            print("Opneing MineCraft...")
            break

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
            speak("Opening Chrome")
            print("Opneing Chrome...")
            break

        # elif 'open earth' in query:
            # earthPath = "C:\\Program Files (x86)\\Google\\Google Earth Pro\\client\\googleearth.exe"
            # os.startfile(earthPath)
            # speak("Opening Google earth")
            # print("Opneing Google Earth...")

        # elif 'open firefox' in query:
            # firefoxPath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
            # os.startfile(firefoxPath)
            # speak("Opening FireFox")
            # print("Opneing FireFox...")

        # elif 'open opera' in query:
            # operaPath = "C:\\Program Files (x86)\\Opera\\launcher.exe"
            # os.startfile(operaPath)
            # speak("Opening opera")
            # print("Opneing Opera...")

        elif 'mail to mahi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mahpara.kausar786@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email at the moment.")

        elif 'mail to papa' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mukhtar.alam72@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email at the moment.")

        elif 'mail to Muneer' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mob.publications1@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email at the moment.")

        elif 'exit' in query:
            speak('Ok sir have a nice day.')
            print('Bye Bye...\n')
            break