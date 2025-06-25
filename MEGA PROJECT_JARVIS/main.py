import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import wikipedia
import os
import requests
from openai import OpenAI

# API key
news_api = "035d6ef16452412c8dc967e07639b082"
client = OpenAI(api_key="sk-dd57b609c68e4fb38b62e51bcaecc097",
                base_url="https://api.deepseek.com")

# Initialize recognizer and voice engine
recognize = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)


def Speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)

    try:
        print("Recognizing...")
        query = recognize.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except:
        return ""


# === MAIN PROGRAM ===
if __name__ == "__main__":
    Speak("Initializing Jarvis...")

    # Wake word
    while True:
        wake = take_command()
        if "jarvis" in wake:
            Speak("Yes sir, I am listening.")
            break

    # Command loop
    while True:
        command = take_command().strip()

        if not command:
            continue

        # === PREDEFINED COMMANDS ===
        if "open youtube" in command:
            Speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            Speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "open vscode" in command or "open code" in command or "open vs code" in command:
            Speak("Opening Visual Studio Code")
            code_path = "C:\\Users\\panch\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "open notepad" in command:
            Speak("Opening Notepad")
            os.startfile("C:\\Windows\\system32\\notepad.exe")

        elif "open chrome" in command:
            Speak("Opening Chrome")
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif "wikipedia" in command:
            Speak("Searching Wikipedia...")
            try:
                topic = command.replace("wikipedia", "")
                result = wikipedia.summary(topic, sentences=2)
                Speak("According to Wikipedia")
                Speak(result)
            except:
                Speak("Sorry, I couldn't find that on Wikipedia.")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"The time is {current_time}")

        elif "news" in command:
            Speak("Fetching the latest news from India.")
            try:
                r = requests.get(
                    f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
                if r.status_code == 200:
                    data = r.json()
                    articles = data.get('articles', [])
                    if not articles:
                        Speak("Sorry, I couldn't find any news at the moment.")
                    else:
                        for i, article in enumerate(articles[:5], 1):
                            title = article.get('title')
                            if title:
                                Speak(f"News {i}: {title}")
                else:
                    Speak("Failed to fetch news from the server.")
            except Exception as e:
                Speak("An error occurred while fetching news.")
                print("News API Error:", e)

        elif "exit" in command or "quit" in command or "bye" in command:
            Speak("Goodbye, sir. see you soon")
            break

        # === DEFAULT TO CHATGPT IF NO MATCH ===
        else:
            Speak("Let me think...")
            try:
                response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "system", "content": "You are a helpful assistant"},
                        {"role": "user", "content": command}],)
                stream=False
                answer=response.choices[0].message.content
                print("ChatGPT:", answer)
                Speak(answer)
            except Exception as e:
                Speak("Sorry, I couldn't connect to OpenAI.")
                Speak("Come With Your Own api")
                print("OpenAI Error:", e)
