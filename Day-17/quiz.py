from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"],question["answer"] ))
    

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.new_question()

print(f"You have completed the quiz. Your final score is {quiz.score}/{len(quiz.question_list)}")


