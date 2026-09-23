import speech_recognition as sr
import pyttsx3

from commands import process_command
from actions import open_chrome, search_youtube


# Create speech recognizer
recognizer = sr.Recognizer()

# Create text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("JARVIS: I am listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""


# JARVIS starts
speak("Hello, I am JARVIS. How can I help you?")

command = listen()

if command:
    action = process_command(command)

    if action == "open_chrome":

        open_chrome()
        speak("Chrome is open.")

    elif action == "search_youtube":

        query = command.lower().replace("search youtube", "").strip()

        if query:
            search_youtube(query)
            speak("I searched YouTube for " + query)

        else:
            speak("What would you like me to search for on YouTube?")

    else:

        speak("I don't know how to do that yet.")