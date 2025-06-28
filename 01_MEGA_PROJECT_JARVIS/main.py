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
import json
import random

load_dotenv()  # Load .env file
groq_api = os.getenv("GROQ_API_KEY")
news_api = os.getenv("NEWS_API_KEY")

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
                    if not topic:
                        Speak("Please specify a topic to search on Wikipedia.")
                        continue
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

            elif "play quiz" in command or "quiz" in command or "game" in command:
                Speak("Let's Play Quiz...")

                try:
                    with open("questions.json", "r") as file:
                        questions = json.load(file)
                except Exception as e:
                    Speak("⚠️ Could not load quiz questions.")
                    print("Quiz Load Error:", e)
                    continue

                random.shuffle(questions)
                score = 0

                number_words = {
                    "one": 1, "two": 2, "three": 3, "four": 4,
                    "1": 1, "2": 2, "3": 3, "4": 4
                }

                for i, q in enumerate(questions, start=1):
                    Speak(f"Q{i}. {q['question']}")
                    for idx, option in enumerate(q["options"], start=1):
                        Speak(f"{idx}. {option}")

                    Speak("Please say the option number like 'one', 'option two', or just '3'.")

                    choice = take_command().lower().strip()
                    num = None

                    if choice in number_words:
                        num = number_words[choice]
                    else:
                        for word in choice.split():
                            if word in number_words:
                                num = number_words[word]
                                break

                    try:
                        if num and 1 <= num <= 4:
                            user_answer = q["options"][num - 1]
                            if user_answer.strip().lower() == q["answer"].strip().lower():
                                Speak("✅ Correct!")
                                score += 1
                            else:
                                Speak(f"❌ Wrong! Correct answer was: {q['answer']}")
                        else:
                            Speak("⚠️ Please choose a number between 1 and 4.")
                    except:
                        Speak("⚠️ Couldn't understand your answer. Skipping this question.")

                Speak("🎉 Quiz finished!")
                Speak(f"🏁 Your total score is: {score} out of {len(questions)}")

            elif "what can you do" in command or "help" in command:
                Speak("I can open apps and websites, answer questions, search Wikipedia, read news, play a quiz, and chat using Groq AI.")

            elif "exit" in command or "quit" in command or "bye" in command:
                Speak("Goodbye, sir. See you soon.")
                break

            else:
                Speak("Let me think...")
                answer = ask_groq(command)
                print("Groq:", answer)
                Speak(answer)

        except KeyboardInterrupt:
            Speak("Interrupted. Goodbye.")
            break

        except Exception as main_error:
            print("Error in main loop:", main_error)
            Speak("Something went wrong. Please try again.")
