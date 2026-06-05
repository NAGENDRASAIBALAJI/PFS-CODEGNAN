import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runandwait()
def take_command():
    recognizer.list = sr.recognizer()

    with sr.microphone() as source:
        print("Listiening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        print("Sorry, please say that again.")
        return ""
def wish_user(text):
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good moring")
    elif hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
        speak("I am your virtual assistence")

while True:
    command = take_command()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M:%P")
        speak(f"The time is {time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.google.com")
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("Goodbye")
        break





        
        

