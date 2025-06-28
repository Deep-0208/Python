import json
import random

# 1️⃣ Load questions from JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

# 2️⃣ Shuffle the questions
random.shuffle(questions)

# 3️⃣ Start score
score = 0

# 4️⃣ Ask each question
for i, q in enumerate(questions, start=1):
    print(f"\nQ{i}. {q['question']}")
    
    # Print options
    for index, option in enumerate(q["options"], start=1):
        print(f"{index}. {option}")
    
    try:
        choice = int(input("Your answer (1-4): "))
        user_answer = q["options"][choice - 1]
        
        if user_answer.lower() == q["answer"].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    
    except:
        print("⚠️ Invalid input. Skipping this question.")

# 5️⃣ Final score
print("\n🎉 Quiz finished!")
print(f"🏁 Your total score is: {score} out of {len(questions)}")
