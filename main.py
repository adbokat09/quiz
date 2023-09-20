import json

from quiz import Quiz, Question

with open('quiz/math.json') as f:
    quiz = Quiz.create_from_dict(json.load(f))

if __name__ == '__main__':
    while True:
        quiz.show_question()
        quiz.wait_user_answer()
        if quiz.has_next_question():
            quiz.next_question()
        else:
            break
    quiz.show_result()
