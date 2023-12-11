import random

def generate_question():

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])
    return num1, operation, num2

def ask_question(question):
 
    num1, operation, num2 = question
    user_answer = float(input(f"{num1} {operation} {num2} "))
    return user_answer

def check_answer(question, user_answer):
 
    num1, operation, num2 = question
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        correct_answer = num1 / num2

    return user_answer == correct_answer

def math_quiz():

    print("Math Quiz!")

    score = 0
    num_questions = 5  #

    for _ in range(num_questions):
        question = generate_question()
        user_answer = ask_question(question)

        if check_answer(question, user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question[0]} {question[1]} {question[2]} = {user_answer}\n")

    print(f"Quiz complete! Your score is {score}/{num_questions}.")


math_quiz()