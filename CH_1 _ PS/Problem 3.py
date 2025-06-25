import pyttsx3

engine = pyttsx3.init()
engine.say("HEY")
engine.runAndWait()  # Only call once, after all .say()
