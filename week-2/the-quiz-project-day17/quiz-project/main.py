# python3 week-2/the-quiz-project-day17/quiz-project/main.py

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# loop through each question in question_data and creat an instance of the question in the question bank
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
quiz.print_score()    