import sys
import os
import webbrowser
import wikipedia
import datetime
import requests
import speech_recognition as sr
import pyttsx3
import threading

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea,
    QHBoxLayout, QPushButton, QFrame, QSpacerItem, QSizePolicy,
    QGraphicsOpacityEffect
)
from PyQt6.QtGui import QPixmap, QFont, QMovie
from PyQt6.QtCore import Qt, QTimer

from openai import OpenAI

# === Configuration ===
groq_api_key = "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"
news_api = "035d6ef16452412c8dc967e07639b082"

client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak_animated_parallel(label, text):
    label.setText("")
    words = text.split()

    def animate():
        for word in words:
            QTimer.singleShot(0, lambda w=word: label.setText(label.text() + w + " "))
            QTimer.singleShot(200 * words.index(word), lambda: None)

    def speak():
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=speak).start()
    threading.Thread(target=animate).start()

def speak_only(text):
    threading.Thread(target=lambda: engine.say(text) or engine.runAndWait()).start()

def take_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="en-in").lower()
    except:
        return ""

class ChatBubble(QFrame):
    def __init__(self, text, is_user):  # Fixed __init__
        super().__init__()
        self.setStyleSheet("background-color: #1E1E1E; border-radius: 12px;")
        layout = QHBoxLayout()

        avatar = QLabel()
        pixmap = QPixmap("assets/user_icon.png" if is_user else "assets/jarvis_icon.png").scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        avatar.setPixmap(pixmap)

        label = QLabel(text)
        label.setWordWrap(True)
        label.setStyleSheet(f"color: {'#00C853' if not is_user else '#FFFFFF'}; font-size: 14px;")
        label.setFont(QFont("Segoe UI", 10))

        if is_user:
            layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Expanding))
            layout.addWidget(label)
            layout.addWidget(avatar)
        else:
            layout.addWidget(avatar)
            layout.addWidget(label)
            layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Expanding))

        self.setLayout(layout)

class JarvisUI(QWidget):
    def __init__(self):  # Fixed __init__
        super().__init__()
        self.setWindowTitle("🧠 Jarvis Assistant")
        self.setGeometry(200, 100, 900, 600)
        self.setStyleSheet("background-color: #121212;")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap("assets/jarvis_bg.jpg").scaled(self.width(), self.height(), Qt.AspectRatioMode.IgnoreAspectRatio))
        self.bg.setStyleSheet("opacity: 0.3;")
        self.bg.lower()

        self.chat_area = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_content.setLayout(self.chat_area)
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setStyleSheet("background-color: transparent; border: none;")

        self.typing_label = QLabel("")
        self.typing_label.setStyleSheet("color: #00C853; font-family: Consolas; padding: 5px;")
        self.typing_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.speech_output_label = QLabel("")
        self.speech_output_label.setStyleSheet("color: #00FFAA; padding: 10px; font-size: 14px;")
        self.speech_output_label.setFont(QFont("Consolas", 10))

        self.animation_label = QLabel()
        self.movie = QMovie("assets/jarvis_anim.gif")
        self.animation_label.setMovie(self.movie)
        self.animation_label.setVisible(False)

        self.listen_button = QPushButton("🎤 Start Listening")
        self.listen_button.setStyleSheet("background-color: #00C853; color: white; padding: 10px; font-size: 14px;")
        self.listen_button.clicked.connect(self.handle_command)

        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.typing_label)
        self.layout.addWidget(self.speech_output_label)
        self.layout.addWidget(self.animation_label)
        self.layout.addWidget(self.listen_button)
        self.setLayout(self.layout)

        self.add_chat("Hello, I am Jarvis.", is_user=False)
        speak_only("Jarvis initialized and ready.")

    def add_chat(self, text, is_user):
        bubble = ChatBubble(text, is_user)
        self.chat_area.addWidget(bubble)
        QTimer.singleShot(100, lambda: self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum()))

    def show_typing_animation(self):
        self.typing_dots = [".", "..", "..."]
        self.current_dot = 0
        self.typing_timer = QTimer()
        self.typing_timer.timeout.connect(self.update_typing)
        self.typing_timer.start(500)

    def update_typing(self):
        self.typing_label.setText(f"Jarvis is typing{self.typing_dots[self.current_dot]}")
        self.current_dot = (self.current_dot + 1) % 3

    def stop_typing_animation(self):
        if hasattr(self, 'typing_timer'):
            self.typing_timer.stop()
        self.typing_label.setText("")

    def handle_command(self):
        self.movie.start()
        self.animation_label.setVisible(True)
        QTimer.singleShot(4000, lambda: self.animation_label.setVisible(False))

        command = take_command()
        if not command:
            return

        self.add_chat(command, is_user=True)

        if "open youtube" in command:
            speak_animated_parallel(self.speech_output_label, "Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            speak_animated_parallel(self.speech_output_label, "Opening Google")
            webbrowser.open("https://google.com")

        elif "open vscode" in command:
            speak_animated_parallel(self.speech_output_label, "Opening Visual Studio Code")
            os.startfile("C:\\Users\\panch\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif "open notepad" in command:
            speak_animated_parallel(self.speech_output_label, "Opening Notepad")
            os.startfile("C:\\Windows\\system32\\notepad.exe")

        elif "open chrome" in command:
            speak_animated_parallel(self.speech_output_label, "Opening Chrome")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "")
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak_animated_parallel(self.speech_output_label, result)
                self.add_chat(result, is_user=False)
            except:
                msg = "Sorry, I couldn't find that on Wikipedia."
                speak_animated_parallel(self.speech_output_label, msg)
                self.add_chat(msg, is_user=False)

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            result = f"The time is {current_time}"
            speak_animated_parallel(self.speech_output_label, result)
            self.add_chat(result, is_user=False)

        elif "news" in command:
            speak_animated_parallel(self.speech_output_label, "Fetching the latest news.")
            try:
                r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
                articles = r.json().get('articles', [])
                for i, article in enumerate(articles[:3], 1):
                    title = article.get('title')
                    if title:
                        speak_animated_parallel(self.speech_output_label, title)
                        self.add_chat(title, is_user=False)
            except Exception:
                self.add_chat("News fetch failed.", is_user=False)
        else:
            self.show_typing_animation()
            QTimer.singleShot(1500, lambda: self.generate_ai_response(command))

    def generate_ai_response(self, prompt):
        try:
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Reply briefly."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response.choices[0].message.content.strip()
            self.stop_typing_animation()
            speak_animated_parallel(self.speech_output_label, reply)
            self.add_chat(reply, is_user=False)
        except Exception as e:
            self.stop_typing_animation()
            error = f"Groq API Error: {e}"
            speak_animated_parallel(self.speech_output_label, error)
            self.add_chat(error, is_user=False)

# 🔧 Entry point fixed
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisUI()
    window.show()
    sys.exit(app.exec())
