# Function to fetch question from the file
def load_questions(filename):
    questions = []
    try:
        with open(filename,'r') as file:
            for line in file:
                question,answer = line.strip().split(";")
                questions.append({
                    "question":question,
                    "answer": answer
                })

    except FileNotFoundError:
        print("Questions file is not found!")

    return questions

# Fuction to save score in file
def save_score(filename,score,total):
    with open(filename,'a') as file:
        file.write(f"Score: {score}/{total}\n")


questions_file = 'questions.txt'
# Load questions
questions = load_questions(questions_file)

if not questions:
    print("No questions available for the quiz.")

else:
    # Start the quiz
    score = 0

    for q in questions:
        user_answer = input(q["question"] + ' ')

        if(user_answer.strip().lower() == q["answer"].lower()):
            score+=1
            print("Congratulation!, You're answer is right.")

        else:
            print(f"OOPS!, You're answer is wrong.\n The correct answer is : {q['answer']}")

    print(f"\n You scored {score} out of {len(questions)}.")

    # save the final score in file
    score_file = "score.txt"
    save_score(score_file,score,len(questions))
    print("Your score has been saved")


