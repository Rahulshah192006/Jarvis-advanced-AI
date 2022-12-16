import speech_recognition as sr
from googletrans import Translator

def Listen():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        mic.pause_threshold = 1
        audio = mic.listen(source,0,2)

    try:
        print("Thinking .....")
        query = mic.recognize_google(audio,language="en-in")
        print(f"You said : {query}\n")
    except:
        return ""

    query = str(query).lower()
    return query
Listen()