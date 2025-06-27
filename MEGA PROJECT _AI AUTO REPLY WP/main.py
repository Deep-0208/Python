import pyautogui
import pyperclip
import time
from dotenv import load_dotenv
import os
from openai import OpenAI
import webbrowser
import keyboard
import random

# Load environment variables
load_dotenv()
groq_api = os.getenv("GROQ_API_KEY")

# Setup Groq client
client = OpenAI(
    api_key=groq_api,
    base_url="https://api.groq.com/openai/v1"
)

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
    # 1. Remove extra spaces and split chat by lines
    lines = chat.strip().splitlines()

    # 2. If chat is empty, return False
    if not lines:
        return False

    # 3. Get the last message line
    last_line = lines[-1]

    # 4. Print the last message for debugging
    print("Last Line:", last_line)

    # 5. Check if last message is from any of your names
    for name in your_names:
        if name + ":" in last_line:
            return False  # Message was sent by you

    return True  # Message was sent by someone else


#This is complicated to understand

# def is_last_message_from_other(chat, your_name="Deep Panchal"):
#     lines = chat.strip().splitlines()
#     if not lines:
#         return False
#     last_line = lines[-1]
#     print("Last Line:", last_line)
#     return your_name + ":" not in last_line  # True if NOT sent by you

# Open WhatsApp Web
webbrowser.open("https://web.whatsapp.com")
print("Waiting 10 seconds for WhatsApp Web to load...")
time.sleep(10)

last_chat = ""

while True:

    pyautogui.click(670, 334)
    time.sleep(0.5)

    # 2. Drag to select chat area (more stable)
    pyautogui.moveTo(687, 215)
    pyautogui.mouseDown(button='left')
    time.sleep(0.1)
    pyautogui.moveTo(1895, 941, duration=1)
    pyautogui.mouseUp(button='left')
    time.sleep(1)
    
    # 3. Copy selected chat
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    chat_history = pyperclip.paste().strip()
    pyautogui.click(1895, 941)  # Unselect

    # 4. Check if copy was successful
    if chat_history == "":
        print("⚠️ Nothing copied. Skipping this round.")
        time.sleep(2)
        continue

    # 5. Skip if chat is same as last time
    if chat_history == last_chat:
        print("⏳ No new message. Waiting...")
        pyautogui.click(670, 334)
        time.sleep(3)
        continue

    # 6. Skip if last message was yours
    if not should_reply(chat_history, your_names=["Deep Panchal" , "You"]):
        print("⛔ Last message is from you. Skipping...")
        last_chat = chat_history
        time.sleep(3)
        continue

    # 7. Generate reply
    print("📩 New chat detected. Asking Groq...")
    reply = ask_groq(chat_history)
    print("✅ Reply:", reply)

    # 8. Send reply
    pyautogui.click(1370, 970)  # Input box
    time.sleep(0.3)
    pyperclip.copy(reply)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(random.uniform(1, 3.0)) 
    pyautogui.press('enter')

    # 9. Save state and wait
    last_chat = chat_history + "\n" + reply
    time.sleep(3)
    
    # 10. exit from bot
    if keyboard.is_pressed("esc"):
        print("🛑 ESC pressed. Exiting loop.")
        break