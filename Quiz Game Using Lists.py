# Quiz game using lists in Python

# List of questions
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the largest ocean on Earth?",
    "Which element has the chemical symbol 'O'?"
]
options = [["A. London", "B. California", "C. Paris", "D. Bangkok"],
           ["A. Mars", "B. Mercury", "C. Neptune", "D. Venus"],
           ["A. Stephen Spielberg", "B. Harper Lee", "C. James Cameroon", "D. Sheldon Cooper"],
           ["A. Pacific", "B. Indian", "C. Arctic", "D. Atlantic"],
           ["A. Hydrogen", "B. Chloride", "C. Steel", "D. Oxygen"]]
# Corresponding list of answers
answers = [
    "C",
    "A",
    "B",
    "A",
    "D"
]


# Function to run the quiz
def quiz_game():
    score = 0
    total_questions = len(questions)

    for i in range(total_questions):
        print(f"Question {i + 1}: {questions[i]}")
        for option in options[i]:
            print(option)
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == answers[i].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answers[i]}\n")

    # Calculate score as percentage
    percentage_score = (score / total_questions) * 100

    # Display final score
    print("----------------RESULTS--------------------")
    print(f"Your got {score}/{total_questions} correct answer(s).")
    print(f"Your score in percentage: {percentage_score:.2f}%")

    if score == total_questions:
        print("Congratulations! You got all answers correct!")
    elif score > total_questions // 2:
        print("Good job!")
    else:
        print("Better luck next time.")


# Run the quiz game
quiz_game()