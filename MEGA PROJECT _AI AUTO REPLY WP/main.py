import pyautogui
import pyperclip
import time
from dotenv import load_dotenv
import os
from openai import OpenAI
import webbrowser
import keyboard
import random
import tkinter as tk
from threading import Thread

# Load environment variables
load_dotenv()
groq_api = os.getenv("GROQ_API_KEY")

# Setup Groq client
client = OpenAI(
    api_key=groq_api,
    base_url="https://api.groq.com/openai/v1"
)

# Global exit flag
exit_flag = False

# Function to stop the bot when Ctrl + X is pressed
def stop_bot():
    global exit_flag
    print("🛑 Ctrl + X pressed. Stopping bot...")
    exit_flag = True

# Register the Ctrl + X hotkey
keyboard.add_hotkey('ctrl+x', stop_bot)

# Function to get response from Groq
def ask_groq(chat_history):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You're chatting as a normal person on WhatsApp. Keep replies casual, natural, and short. Never mention you're a bot."},
                {"role": "user", "content": chat_history}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        print("Groq API Error:", e)
        return "Sorry, I couldn't get a response from Groq."

# Function to check if last message is NOT from you
def should_reply(chat, your_names=["Deep Panchal", "You"]):
    lines = chat.strip().splitlines()
    if not lines:
        return False
    last_line = lines[-1]
    print("Last Line:", last_line)
    for name in your_names:
        if name + ":" in last_line:
            return False
    return True

# Function to show GUI popup with 15s + 5s countdown
def show_full_popup():
    popup = tk.Tk()
    popup.title("WhatsApp Bot")
    popup.geometry("400x180")
    popup.resizable(False, False)

    label = tk.Label(popup, text="💬 WhatsApp Web is loading...", font=("Arial", 12))
    label.pack(pady=10)

    countdown_label = tk.Label(popup, text="", font=("Arial", 20, "bold"))
    countdown_label.pack(pady=5)

    phase_label = tk.Label(popup, text="", font=("Arial", 11))
    phase_label.pack(pady=5)

    def full_countdown():
        # Phase 1: 15s WhatsApp loading
        seconds = 15
        while seconds >= 0:
            countdown_label.config(text=f"⏳ Loading WhatsApp: {seconds}s")
            phase_label.config(text="Please wait while WhatsApp Web loads...")
            popup.update()
            time.sleep(1)
            seconds -= 1

        # Phase 2: 5s chat selection
        label.config(text="📌 Please select a chat in WhatsApp!")
        seconds = 5
        while seconds >= 0:
            countdown_label.config(text=f"⏳ Bot starting in: {seconds}s")
            phase_label.config(text="Make sure a chat is selected.")
            popup.update()
            time.sleep(1)
            seconds -= 1

        popup.destroy()

    Thread(target=full_countdown, daemon=True).start()
    popup.mainloop()

# Step 1: Open WhatsApp Web and show countdowns
webbrowser.open("https://web.whatsapp.com")
show_full_popup()

# Step 2: Start bot loop
last_chat = ""

while not exit_flag:
    pyautogui.click(670, 334)
    time.sleep(0.5)

    pyautogui.moveTo(687, 215)
    pyautogui.mouseDown(button='left')
    time.sleep(0.1)
    pyautogui.moveTo(1895, 941, duration=1)
    pyautogui.mouseUp(button='left')
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    chat_history = pyperclip.paste().strip()
    pyautogui.click(1895, 941)

    if chat_history == "":
        print("⚠️ Nothing copied. Skipping this round.")
        time.sleep(2)
        continue

    if chat_history == last_chat:
        print("⏳ No new message. Waiting...")
        pyautogui.click(670, 334)
        time.sleep(3)
        continue

    if not should_reply(chat_history, your_names=["Deep Panchal", "You"]):
        print("⛔ Last message is from you. Skipping...")
        last_chat = chat_history
        time.sleep(3)
        continue

    print("📩 New chat detected. Asking Groq...")
    reply = ask_groq(chat_history)
    print("✅ Reply:", reply)

    pyautogui.click(1370, 970)
    time.sleep(0.3)
    pyperclip.copy(reply)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(random.uniform(1, 3.0))
    pyautogui.press('enter')

    last_chat = chat_history + "\n" + reply
    time.sleep(3)

print("Bot exited successfully.")
