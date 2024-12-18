import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import datetime
import os

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am ASCII. Please tell me how may I help you")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}\n")
    except Exception as e:
        print("Sorry, Say that again please...")
        return "None"
    return text


def wikipedia_summary(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    try:
        summary = wikipedia.summary(query, sentences=2)
        print(summary)
        speak("According to wikipedia")
        speak(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation Error: {e.options}")
    except wikipedia.exceptions.PageError:
        print("***The page does not exist.***")
        speak("Sorry, The page does not exist.")


wish_me()
while True:
    query = recognize_speech().lower()
    if "exit" in query:
        break
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir, the time is {strTime}")
        speak(f"Sir, the time is {strTime}")
    elif "open" in query and "file" in query:
        speak("what is the path?")
        path = input("what is the path? ")
        os.startfile(path)
    elif "open" in query:
        query = query.replace("open ", "")
        speak(f"Opening {query}...")
        time.sleep(0.9)
        webbrowser.open(f"{query}.com")
    elif "wikipedia" in query:
        wikipedia_summary(query)
