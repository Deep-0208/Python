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

# ====== Load API Key from .env ======
load_dotenv()
groq_api = os.getenv("GROQ_API_KEY")

# ====== Setup Groq Client ======
client = OpenAI(
    api_key=groq_api,
    base_url="https://api.groq.com/openai/v1"
)

# ====== Global Flag for Stopping ======
exit_flag = False

# ====== Hotkey to Stop Bot ======
def stop_bot():
    global exit_flag
    print("🛑 Ctrl + X pressed. Stopping bot...")
    exit_flag = True

keyboard.add_hotkey('ctrl+x', stop_bot)

# ====== Ask Groq for Reply ======
def ask_groq(chat_history):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You're chatting as a normal person on WhatsApp. Keep replies casual, natural, and short. Never mention you're a bot."},
                {"role": "user", "content": chat_history}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Groq API Error:", e)
        return "Sorry, I couldn't get a response from Groq."

# ====== Check If Reply Is Needed ======
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

# ====== Show GUI Popup Countdown ======
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
        for seconds in range(15, -1, -1):
            countdown_label.config(text=f"⏳ Loading WhatsApp: {seconds}s")
            phase_label.config(text="Please wait while WhatsApp Web loads...")
            popup.update()
            time.sleep(1)

        label.config(text="📌 Please select a chat in WhatsApp!")
        for seconds in range(5, -1, -1):
            countdown_label.config(text=f"⏳ Bot starting in: {seconds}s")
            phase_label.config(text="Make sure a chat is selected.")
            popup.update()
            time.sleep(1)

        popup.destroy()

    Thread(target=full_countdown, daemon=True).start()
    popup.mainloop()

# ====== Copy Chat with Retry ======
def try_copy_chat():
    pyperclip.copy("")  # clear clipboard before first attempt
    time.sleep(0.3)

    pyautogui.moveTo(687, 215)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(1895, 941, duration=1)
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    chat_text = pyperclip.paste().strip()

    if chat_text:
        return chat_text

    print("⚠️ First copy failed. Retrying...")
    pyperclip.copy("")
    time.sleep(0.3)

    pyautogui.moveTo(700, 200)
    pyautogui.mouseDown()
    pyautogui.moveTo(1300, 950, duration=1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    chat_text = pyperclip.paste().strip()

    if chat_text:
        return chat_text

    print("❌ Retry also failed. Skipping...")
    return ""

# ====== MAIN BOT FUNCTION ======
def run_bot():
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(2)
    show_full_popup()

    last_chat = ""

    while not exit_flag:
        try:
            pyautogui.click(670, 334)  # focus WhatsApp window
            time.sleep(0.5)

            chat_history = try_copy_chat()

            if not chat_history:
                time.sleep(2)
                continue

            if chat_history == last_chat:
                print("⏳ No new message. Waiting...")
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

            pyautogui.click(1370, 970)  # focus message box
            time.sleep(0.3)
            pyperclip.copy(reply)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(random.uniform(1, 3))
            pyautogui.press('enter')

            last_chat = chat_history + "\n" + reply
            time.sleep(3)

        except Exception as e:
            print("💥 Error occurred:", e)
            with open("error_log.txt", "a") as log:
                log.write(f"{time.ctime()} - {e}\n")
            time.sleep(2)

    print("✅ Bot exited successfully.")

# ====== RUN ENTRY POINT ======
if __name__ == "__main__":
    run_bot()
