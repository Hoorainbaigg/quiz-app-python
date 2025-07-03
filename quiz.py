questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Quetta"],
        "answer": "Islamabad"
    },
    {
        "question": "Who developed Python?",
        "options": ["Dennis Ritchie", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which year was C++ released?",
        "options": ["1972", "1985", "1991", "2000"],
        "answer": "1985"
    }
]

score = 0

print("🔸 Welcome to the Quiz App 🔸\n")

for idx, q in enumerate(questions, 1):
    print(f"Q{idx}: {q['question']}")
    for i, opt in enumerate(q['options'], 1):
        print(f"  {i}. {opt}")
    user_choice = input("Enter option number: ")

    if user_choice.isdigit() and int(user_choice) in range(1, len(q['options']) + 1):
        selected = q['options'][int(user_choice) - 1]
        if selected.lower() == q['answer'].lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")
    else:
        print("⚠️ Invalid input. Skipping question.\n")

print(f"🎯 Final Score: {score}/{len(questions)}")
