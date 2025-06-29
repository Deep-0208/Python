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

# === Load Environment Variables ===
load_dotenv()
groq_api = os.getenv("GROQ_API_KEY")
news_api = os.getenv("NEWS_API_KEY")
quiz_api = os.getenv("QUIZ_API_KEY")

# === Fallback for Missing API Keys ===
if not groq_api or not news_api:
    print("Missing API keys. Please check your .env file.")
    engine = pyttsx3.init()
    engine.say("Missing API keys. Please check your dot env file.")
    engine.runAndWait()
    exit()

# === Initialize Groq Client ===
client = OpenAI(
    api_key=groq_api,
    base_url="https://api.groq.com/openai/v1"
)

# === Initialize Recognizer and TTS ===
recognize = sr.Recognizer()
engine = pyttsx3.init()


def Speak(text):
    try:
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")


def take_command():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognize.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = recognize.listen(source, timeout=5, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("⏱️ Timeout: No voice detected.")
                return ""
        print("🧠 Recognizing...")
        try:
            query = recognize.recognize_google(audio, language="en-in")
            print(f"🗣️ You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand.")
            return ""
        except sr.RequestError:
            print("⚠️ Recognition service error.")
            return ""
    except Exception as e:
        print("🎙️ Microphone Error:", e)
        return ""


def ask_groq(command):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that replies to human questions briefly."},
                {"role": "user", "content": command}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print("❌ Groq API Error:", e)
        return "Sorry, I couldn't get a response from Groq."


def wait_for_wake_word():
    print("🔄 Jarvis is ready. Say 'Jarvis' to activate.")
    Speak("Jarvis is ready. Say Jarvis to activate.")
    wake_timeout = 60
    start_time = time.time()
    while True:
        if time.time() - start_time > wake_timeout:
            print("😴 Timeout. Going to sleep.")
            Speak("Timeout. Going to sleep.")
            return False
        wake = take_command()
        if "jarvis" in wake:
            Speak("Yes sir, I am listening.")
            return True
        if wake:
            start_time = time.time()


def get_news(command=""):
    categories = {
        "technology": "technology",
        "tech": "technology",
        "business": "business",
        "sports": "sports",
        "entertainment": "entertainment",
        "health": "health",
        "science": "science",
        "general": "general"
    }
    category = "general"
    for cat in categories:
        if cat in command:
            category = categories[cat]
            break

    try:
        print(f"📰 Fetching {category} news...")
        Speak(f"Fetching the latest {category} news.")
        url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={news_api}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            if not articles:
                Speak("Sorry, no news found.")
                return
            news_count = min(5, len(articles))
            Speak(f"Here are the top {news_count} news headlines:")
            for i, article in enumerate(articles[:news_count], 1):
                title = article.get('title')
                if title and title != "[Removed]":
                    print(f"{i}. {title}")
                    Speak(f"News {i}: {title}")
                    time.sleep(0.5)
        else:
            Speak("Could not fetch news.")
    except Exception as e:
        print("News Error:", e)
        Speak("An error occurred while fetching news.")


def search_wikipedia(topic):
    if not topic:
        Speak("Please say a topic to search.")
        return
    try:
        print(f"🔍 Wikipedia search: {topic}")
        Speak(f"Searching Wikipedia for {topic}")
        summary = wikipedia.summary(topic, sentences=2)
        Speak("According to Wikipedia:")
        Speak(summary)
        Speak("Would you like to know more?")
        response = take_command()
        if any(word in response for word in ["yes", "sure", "more", "continue"]):
            more = wikipedia.summary(topic, sentences=4)
            Speak(more)
    except wikipedia.exceptions.PageError:
        Speak(f"No Wikipedia page found for {topic}")
    except Exception as e:
        print("Wikipedia Error:", e)
        Speak("Wikipedia is not available right now.")


def web_opener(command):
    web_apps = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "gmail": "https://gmail.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com",
        "twitter": "https://twitter.com",
        "linkedin": "https://linkedin.com",
        "github": "https://github.com"
    }
    for app, url in web_apps.items():
        if f"open {app}" in command:
            Speak(f"Opening {app}")
            webbrowser.open(url)
            return


# === MAIN PROGRAM ===

if __name__ == "__main__":
    Speak("Initializing Jarvis...")

    while True:
        if not wait_for_wake_word():
            continue

        while True:
            command = take_command()
            if not command:
                continue

            # Predefined App Commands
            if "open vscode" in command or "open code" in command:
                Speak("Opening Visual Studio Code")
                os.startfile("C:\\Users\\panch\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

            elif "open notepad" in command:
                Speak("Opening Notepad")
                os.startfile("C:\\Windows\\system32\\notepad.exe")

            elif "open chrome" in command:
                Speak("Opening Chrome")
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

            elif "time" in command:
                now = datetime.datetime.now()
                time_str = now.strftime("%I:%M %p")
                date_str = now.strftime("%A, %B %d, %Y")
                Speak(f"The time is {time_str} and today is {date_str}")

            elif "news" in command:
                get_news(command)

            elif "wikipedia" in command or "who is" in command or "what is" in command:
                topic = command.replace("wikipedia", "").replace("who is", "").replace("what is", "").strip()
                search_wikipedia(topic)

            elif "open" in command:
                if not web_opener(command):
                    Speak("I couldn't find that website in my list.")

            elif "search for" in command:
                query = command.replace("search for", "").strip()
                Speak(f"Searching Google for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
                
            elif "what can you do" in command or "help" in command:
                Speak("I can open apps and websites, answer questions, search Wikipedia, read news, and chat with you.")

            elif "exit" in command or "quit" in command or "bye" in command:
                Speak("Goodbye, sir. See you soon.")
                exit()
                
            else:
                Speak("Let me think...")
                reply = ask_groq(command)
                print("Groq:", reply)
                Speak(reply)
