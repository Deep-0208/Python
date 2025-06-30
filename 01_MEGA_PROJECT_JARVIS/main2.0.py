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


# Load environment variables
load_dotenv()
groq_api = os.getenv("GROQ_API_KEY")
news_api = os.getenv("NEWS_API_KEY")
quiz_api = os.getenv("QUIZ_API_KEY")

# === Fallback for Missing API Keys ===
if not groq_api or not news_api or not quiz_api:
    print("Missing API keys. Please check your .env file.")
    print("Required: GROQ_API_KEY, NEWS_API_KEY, QUIZ_API_KEY")
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

# === Core Functions ===
def Speak(text):
    """text-to-speech function"""
    try:
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)  # Use first available voice
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"TTS Error: {e}")

def take_command():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            try:
                recognize.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognize.listen(source, timeout=5, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("⏰ Timeout: No voice detected.")
                return ""
            except Exception as mic_error:
                print(f"🎤 Microphone Error: {mic_error}")
                return ""

        print("🧠 Recognizing...")
        try:
            query = recognize.recognize_google(audio, language="en-in")
            print(f"👤 You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, could not understand.")
            return ""
        except sr.RequestError as e:
            print(f"🌐 Could not connect to recognition service: {e}")
            return ""
    except Exception as outer_error:
        print(f"🚨 Error accessing the microphone: {outer_error}")
        return ""

def ask_groq(command):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant. Reply briefly and conversationally."},
                {"role": "user", "content": command}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"🤖 Groq API Error: {e}")
        return "Sorry, I couldn't process that request right now."

# === Wake Word Detection ===
def wait_for_wake_word():
    wake_phrases = ["jarvis", "hey jarvis", "hello jarvis", "jarvis wake up", "wake up jarvis"]
    wake_timeout = 60
    start_time = time.time()
    
    print("🔄 Jarvis is ready. Say 'Jarvis' to activate.")
    Speak("Jarvis is ready. Say Jarvis to activate.")
    
    while True:
        if time.time() - start_time > wake_timeout:
            print("😴 Going to sleep mode...")
            Speak("Going to sleep mode. Say Jarvis to wake me up.")
            return False
        
        wake = take_command()
        if wake and any(phrase in wake for phrase in wake_phrases):
            print("✅ Wake word detected!")
            Speak("Yes sir, I am listening.")
            return True
        
        # Reset timeout if any sound is detected
        if wake:
            start_time = time.time()

# === Enhanced Help Function ===
def show_help():
    """Display available commands and features"""
    help_text = """
    🤖 === JARVIS COMMAND CENTER ===
    
    🌐 WEB & APPS:
    • Open YouTube, Google, Gmail, Chrome
    • Open VS Code, Notepad
    • Open Facebook, Instagram, Twitter
    
    📚 INFORMATION:
    • Search Wikipedia for any topic
    • Get latest news (general, tech, sports, etc.)
    • Ask me any question using AI
    
    🎯 INTERACTIVE FEATURES:
    • Play quiz games with difficulty levels
    • Get current time and date
    • Weather information
    
    🔧 SYSTEM COMMANDS:
    • Say 'exit', 'quit', or 'bye' to close
    • Say 'help' for this menu
    • Say 'sleep' to go to sleep mode
    """
    
    print(help_text)
    Speak("I can open websites and apps, search information, play quiz games, get news, and answer your questions using AI. Say help anytime to see all my features.")

# === Enhanced News Function ===
def get_news(command=""):
    """Enhanced news function with categories"""
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
    
    # Check if specific category mentioned
    for cat_name, cat_code in categories.items():
        if cat_name in command:
            category = cat_code
            break
    
    try:
        print(f"📰 Fetching {category} news...")
        Speak(f"Fetching the latest {category} news from India.")
        
        url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={news_api}"
        r = requests.get(url, timeout=10)
        
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            
            if not articles:
                Speak("Sorry, I couldn't find any news at the moment.")
                return
            
            news_count = min(5, len(articles))
            Speak(f"Here are the top {news_count} {category} news headlines:")
            
            for i, article in enumerate(articles[:5], 1):
                title = article.get('title')
                if title and title != "[Removed]":
                    print(f"{i}. {title}")
                    Speak(f"News {i}: {title}")
                    time.sleep(0.5)
        else:
            Speak("Failed to fetch news from the server.")
            
    except Exception as e:
        Speak("An error occurred while fetching news.")
        print(f"📰 News API Error: {e}")

# === Enhanced Wikipedia Search ===
def search_wikipedia(topic):
    """Enhanced Wikipedia search function"""
    if not topic:
        Speak("Please specify a topic to search on Wikipedia.")
        return
    
    print(f"🔍 Searching Wikipedia for: {topic}")
    Speak(f"Searching Wikipedia for {topic}")
    
    try:
        # Try to get a summary
        result = wikipedia.summary(topic, sentences=2)
        Speak("According to Wikipedia:")
        Speak(result)
        
        # Ask if user wants more information
        Speak("Would you like to know more about this topic?")
        more_info = take_command()
        
        if more_info and any(word in more_info for word in ["yes", "sure", "more", "continue"]):
            try:
                detailed_result = wikipedia.summary(topic, sentences=4)
                Speak("Here's more information:")
                Speak(detailed_result)
            except:
                Speak("Sorry, I couldn't get more detailed information.")
                
    except wikipedia.exceptions.DisambiguationError as e:
        Speak(f"Multiple topics found for {topic}. Here are some options:")
        options = e.options[:3]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            Speak(f"Option {i}: {option}")
        
        Speak("Please be more specific about which topic you want.")
        
    except wikipedia.exceptions.PageError:
        Speak(f"Sorry, I couldn't find any Wikipedia page for {topic}.")
        
    except Exception as e:
        Speak("Sorry, I couldn't search Wikipedia right now.")
        print(f"📖 Wikipedia Error: {e}")

# === Enhanced Quiz Function using QuizAPI.io ===
def fetch_quiz_questions(difficulty="medium", category="", limit=10):
    """Fetch questions from QuizAPI.io"""
    try:
        # QuizAPI.io endpoint
        url = "https://quizapi.io/api/v1/questions"
        
        # Map difficulty levels
        difficulty_mapping = {
            "easy": "Easy",
            "medium": "Medium", 
            "hard": "Hard"
        }
        
        # Available categories in QuizAPI.io
        categories = {
            "general": "General Knowledge",
            "science": "Science",
            "sports": "Sports",
            "history": "History",
            "geography": "Geography",
            "arts": "Arts & Literature",
            "movies": "Movies",
            "music": "Music",
            "technology": "Science: Computers",
            "math": "Mathematics"
        }
        
        params = {
            "apiKey": quiz_api,
            "limit": limit,
            "difficulty": difficulty_mapping.get(difficulty, "Medium")
        }
        
        # Add category if specified
        if category and category in categories:
            params["category"] = categories[category]
        
        print(f"🌐 Fetching {limit} {difficulty} quiz questions...")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            questions_data = response.json()
            
            if not questions_data:
                return None
            
            # Convert API format to our format
            formatted_questions = []
            for q in questions_data:
                if q.get("question") and q.get("answers"):
                    # Get all non-null answers
                    answers = q["answers"]
                    options = []
                    correct_answer = None
                    
                    # Extract options and find correct answer
                    for key, value in answers.items():
                        if value:  # If answer is not null
                            options.append(value)
                            if q.get("correct_answers", {}).get(f"{key}_correct") == "true":
                                correct_answer = value
                    
                    # Only add question if we have enough options and a correct answer
                    if len(options) >= 2 and correct_answer:
                        # Pad options to 4 if needed
                        while len(options) < 4:
                            options.append(f"Option {len(options) + 1}")
                        
                        formatted_questions.append({
                            "question": q["question"],
                            "options": options[:4],  # Limit to 4 options
                            "answer": correct_answer,
                            "explanation": q.get("explanation", "")
                        })
            
            return formatted_questions
            
        else:
            print(f"❌ API Error: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"🌐 Quiz API Error: {e}")
        return None

def play_quiz():
    """Enhanced quiz function using QuizAPI.io"""
    
    MAX_QUESTIONS = 10
    TIME_LIMIT = 20  # Increased time for potentially harder questions
    DIFFICULTY_LEVELS = ["easy", "medium", "hard"]
    
    print("🎯 === DYNAMIC QUIZ GAME STARTING ===")
    Speak("Welcome to the Dynamic Quiz Game powered by Quiz API!")
    
    # Ask for difficulty level
    Speak("Choose difficulty: easy, medium, or hard?")
    difficulty_choice = take_command()
    
    difficulty = "medium"  # default
    if difficulty_choice:
        for level in DIFFICULTY_LEVELS:
            if level in difficulty_choice:
                difficulty = level
                break
    
    # Ask for category (optional)
    Speak("Choose a category: general, science, sports, history, geography, technology, or say any for random category")
    category_choice = take_command()
    
    category = ""
    categories = ["general", "science", "sports", "history", "geography", "technology", "math", "arts", "movies", "music"]
    
    if category_choice:
        for cat in categories:
            if cat in category_choice:
                category = cat
                break
    
    category_text = f"{category} " if category else "mixed "
    print(f"🎮 Starting {difficulty} level {category_text}quiz!")
    Speak(f"Starting {difficulty} level {category_text}quiz!")
    
    # Fetch questions from API
    questions = fetch_quiz_questions(difficulty, category, MAX_QUESTIONS)
    
    if not questions:
        Speak("Sorry, I couldn't fetch quiz questions right now. Please try again later.")
        return
    
    if len(questions) == 0:
        Speak("No questions available for your selection. Please try different options.")
        return
    
    # Quiz setup
    score = 0
    total_questions = len(questions)
    wrong_answers = []
    
    # Enhanced answer recognition
    answer_mapping = {
        "a": 1, "option a": 1, "first": 1, "one": 1, "1": 1,
        "b": 2, "option b": 2, "second": 2, "two": 2, "2": 2,
        "c": 3, "option c": 3, "third": 3, "three": 3, "3": 3,
        "d": 4, "option d": 4, "fourth": 4, "four": 4, "4": 4
    }
    
    Speak(f"Starting quiz with {total_questions} questions. You have {TIME_LIMIT} seconds per question.")
    time.sleep(1)
    
    # Main quiz loop
    for i, question_data in enumerate(questions, start=1):
        try:
            question = question_data.get("question", "")
            options = question_data.get("options", [])
            correct_answer = question_data.get("answer", "")
            explanation = question_data.get("explanation", "")
            
            if not question or not options or not correct_answer:
                continue
            
            print(f"\n📝 === Question {i}/{total_questions} ===")
            print(f"❓ {question}")
            Speak(f"Question {i}: {question}")
            
            # Display options
            option_labels = ["A", "B", "C", "D"]
            for idx, option in enumerate(options[:4]):
                print(f"{option_labels[idx]}. {option}")
                Speak(f"Option {option_labels[idx]}: {option}")
            
            # Get user answer
            Speak("Please say your answer: A, B, C, or D")
            
            answer_start_time = time.time()
            user_choice = None
            
            while time.time() - answer_start_time < TIME_LIMIT:
                choice = take_command()
                if not choice:
                    continue
                
                # Parse answer
                for phrase, num in answer_mapping.items():
                    if phrase in choice:
                        if 1 <= num <= len(options):
                            user_choice = num
                            break
                
                if user_choice:
                    break
                else:
                    Speak("Please say A, B, C, or D")
            
            # Check timeout
            if user_choice is None:
                print("⏰ Time's up!")
                Speak(f"Time's up! The correct answer was: {correct_answer}")
                if explanation:
                    print(f"💡 Explanation: {explanation}")
                wrong_answers.append({
                    "question": question,
                    "correct_answer": correct_answer,
                    "user_answer": "No answer (timeout)",
                    "explanation": explanation
                })
                continue
            
            # Validate answer
            user_answer = options[user_choice - 1]
            
            if user_answer.strip().lower() == correct_answer.strip().lower():
                print("✅ Correct!")
                Speak("Excellent! That's correct!")
                score += 1
                if explanation:
                    print(f"💡 {explanation}")
            else:
                print("❌ Wrong!")
                Speak(f"Sorry, that's incorrect. The correct answer was: {correct_answer}")
                if explanation:
                    print(f"💡 Explanation: {explanation}")
                    Speak(f"Here's why: {explanation}")
                wrong_answers.append({
                    "question": question,
                    "correct_answer": correct_answer,
                    "user_answer": user_answer,
                    "explanation": explanation
                })
            
            time.sleep(2)  # Longer pause for explanations
            
        except KeyboardInterrupt:
            Speak("Quiz interrupted by user.")
            break
        except Exception as e:
            print(f"Error in question {i}: {e}")
            continue
    
    # Quiz summary
    print(f"\n🏆 === QUIZ COMPLETE ===")
    percentage = (score / total_questions) * 100 if total_questions > 0 else 0
    
    Speak("Quiz finished! Here are your results:")
    Speak(f"You scored {score} out of {total_questions} questions.")
    Speak(f"That's {percentage:.1f} percent!")
    
    # Performance feedback
    if percentage >= 90:
        Speak("Outstanding performance! You're a quiz master!")
    elif percentage >= 75:
        Speak("Great job! You did very well!")
    elif percentage >= 60:
        Speak("Good work! You have solid knowledge!")
    elif percentage >= 40:
        Speak("Not bad! Keep learning and you'll improve!")
    else:
        Speak("Keep practicing! Every expert was once a beginner!")
    
    # Offer detailed review
    if wrong_answers:
        Speak("Would you like me to review the questions you missed?")
        review_choice = take_command()
        
        if review_choice and any(word in review_choice for word in ["yes", "sure", "review"]):
            Speak("Here's a quick review of missed questions:")
            for i, wrong in enumerate(wrong_answers[:3], 1):  # Limit to 3 for time
                Speak(f"Question: {wrong['question']}")
                Speak(f"Correct answer: {wrong['correct_answer']}")
                if wrong.get('explanation'):
                    Speak(f"Explanation: {wrong['explanation']}")
                time.sleep(1)
    
    # Offer to play again
    Speak("Would you like to play another quiz?")
    play_again = take_command()
    
    if play_again and any(word in play_again for word in ["yes", "sure", "again", "more"]):
        play_quiz()



# === Enhanced Command Processing ===
def process_command(command):
    """Enhanced command processing with better pattern matching"""
    
    command = command.strip().lower()
    
    if not command:
        return
    
    print(f"🔄 Processing command: {command}")
    
    # Web and App commands
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
            print(f"🌐 Opening {app.title()}...")
            Speak(f"Opening {app.title()}")
            webbrowser.open(url)
            return
    
    # Application commands
    if any(phrase in command for phrase in ["open vscode", "open code", "open vs code", "open visual studio"]):
        print("💻 Opening VS Code...")
        Speak("Opening Visual Studio Code")
        code_paths = [
            "C:\\Users\\panch\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
            "C:\\Program Files\\Microsoft VS Code\\Code.exe",
            "code"  # If in PATH
        ]
        
        for path in code_paths:
            try:
                os.startfile(path) if path.endswith('.exe') else os.system(f'start {path}')
                break
            except:
                continue
        else:
            Speak("Could not find VS Code. Please check the installation.")
        return
    
    if "open notepad" in command:
        print("📝 Opening Notepad...")
        Speak("Opening Notepad")
        os.startfile("C:\\Windows\\system32\\notepad.exe")
        return
    
    if "open chrome" in command:
        print("🌐 Opening Chrome...")
        Speak("Opening Chrome")
        chrome_paths = [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        ]
        
        for path in chrome_paths:
            try:
                os.startfile(path)
                break
            except:
                continue
        else:
            Speak("Could not find Chrome. Please check the installation.")
        return
    
    # Information commands
    if "wikipedia" in command:
        topic = command.replace("wikipedia", "").replace("search", "").strip()
        search_wikipedia(topic)
        return
    
    if any(phrase in command for phrase in ["what time", "current time", "time now"]):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        print(f"🕐 Time: {current_time} | Date: {current_date}")
        Speak(f"The time is {current_time} and today is {current_date}")
        return
    
    if "news" in command:
        get_news(command)
        return
    
    # Interactive features
    if any(phrase in command for phrase in ["play quiz", "quiz", "game", "start quiz"]):
        play_quiz()
        return
    
    if any(phrase in command for phrase in ["what can you do", "help", "commands", "features"]):
        show_help()
        return
    
    # Sleep mode
    if any(phrase in command for phrase in ["sleep", "go to sleep", "sleep mode"]):
        Speak("Going to sleep mode. Say Jarvis to wake me up.")
        wait_for_wake_word()
        return
    
    # Exit commands
    if any(phrase in command for phrase in ["exit", "quit", "bye", "goodbye", "stop", "shutdown"]):
        print("👋 Goodbye!")
        Speak("Goodbye, sir. See you soon.")
        return "exit"
    
    # Default: Use Groq AI
    print("🤖 Thinking...")
    Speak("Let me think...")
    answer = ask_groq(command)
    print(f"🤖 Jarvis: {answer}")
    Speak(answer)

# === Main Program ===
def main():
    """Main program loop with enhanced structure"""
    print("🚀 === JARVIS VOICE ASSISTANT ===")
    Speak("Initializing Jarvis...")
    
    # Display startup info
    current_time = datetime.datetime.now().strftime("%I:%M %p, %A, %B %d, %Y")
    print(f"🕐 Current time: {current_time}")
    print("🎤 Microphone ready")
    print("🤖 AI system online")
    print("📰 News service ready")
    print("🎯 Dynamic Quiz API ready")
    print("🌐 QuizAPI.io connected")
    
    # Wake word detection loop
    while True:
        if not wait_for_wake_word():
            continue
        
        # Main command loop
        while True:
            try:
                command = take_command()
                
                if not command:
                    continue
                
                result = process_command(command)
                
                if result == "exit":
                    return
                    
            except KeyboardInterrupt:
                print("\n🚨 Interrupted by user")
                Speak("Interrupted. Goodbye.")
                return
            except Exception as main_error:
                print(f"🚨 Error in main loop: {main_error}")
                Speak("Something went wrong. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"🚨 Fatal error: {e}")
        Speak("A critical error occurred. Please restart the program.")
    finally:
        print("🔄 Jarvis shutting down...")
        Speak("Jarvis shutting down. Goodbye.")