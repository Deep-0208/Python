import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import wikipedia
import os
import requests
from openai import OpenAI
import time
from dotenv import load_dotenv

load_dotenv()  # Load .env file
groq_api = os.getenv("GROQ_API_KEY")
news_api = os.getenv("NEWS_API_KEY")

# === Initialize Groq Client ===
client = OpenAI(
    api_key=groq_api, 
    base_url="https://api.groq.com/openai/v1"
)

# === Initialize recognizer and TTS engine ===
recognize = sr.Recognizer()
engine = pyttsx3.init()


def Speak(text):
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            try:
                recognize.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognize.listen(
                    source, timeout=5, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("Timeout: No voice detected.")
                return ""
            except Exception as mic_error:
                print("Microphone Error:", mic_error)
                return ""

        print("Recognizing...")
        try:
            query = recognize.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, could not understand.")
            return ""
        except sr.RequestError:
            print("Could not connect to recognition service.")
            return ""
    except Exception as outer_error:
        print("Error accessing the microphone:", outer_error)
        return ""


def ask_groq(command):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that replies to human questions briefly."},
                {"role": "user", "content": command}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Groq API Error:", e)
        return "Sorry, I couldn't get a response from Groq."


# === MAIN PROGRAM ===
if __name__ == "__main__":
    Speak("Initializing Jarvis...")

    # Wake word
    # === Wake word with timeout ===
    wake_timeout = 60  # seconds
    start_time = time.time()

    while True:
        if time.time() - start_time > wake_timeout:
            Speak("Timeout reached. No wake word detected.")
            exit()

        wake = take_command()
        if "jarvis" in wake:
            Speak("Yes sir, I am listening.")
            break

    # Command loop
    while True:
        try:
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
                    topic = command.replace("wikipedia", "").strip()
                    result = wikipedia.summary(topic, sentences=2)
                    Speak("According to Wikipedia")
                    Speak(result)
                except Exception as e:
                    Speak("Sorry, I couldn't find that on Wikipedia.")
                    print("Wikipedia Error:", e)

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
                Speak("Goodbye, sir. See you soon.")
                break

            # === FALLBACK TO GROQ CHAT ===
            else:
                Speak("Let me think...")
                answer = ask_groq(command)
                print("Groq:", answer)
                Speak(answer)

        except Exception as main_error:
            print("Error in main loop:", main_error)
            Speak("Something went wrong. Please try again.")
