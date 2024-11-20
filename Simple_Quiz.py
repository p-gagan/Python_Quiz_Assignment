quiz_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who developed the theory of relativity?", "answer": "Einstein"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"}
]

score = 0

for question in quiz_questions:
    user_answer = input(question["question"] + " ")

    if(user_answer.strip().lower() == question["answer"].lower()):
        print("Congratulation!, You're answer is right.")
        score+=1

    else:
        print(f"OOPS!, You're answer is wrong.\n The correct answer is : {question['answer']}")


print(f"\n You scored {score} out of {len(quiz_questions)}.")