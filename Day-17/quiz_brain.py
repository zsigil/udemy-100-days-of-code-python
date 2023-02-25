class QuizBrain:

    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def new_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q{self.question_number+1} :{current_question.text} True/False?: ")
        self.question_number += 1
        self.check_answer(current_question, answer)


    def still_has_questions(self):
        return len(self.question_list)>self.question_number


    def check_answer(self, question, answer):
        if question.answer.lower() == answer.lower():
            self.score += 1
            print('You got it right')
        else:
            print('No, you are wrong.')

        print(f"The correct answer is: {question.answer.lower()}.")
        print(f"Current score is {self.score}/{self.question_number}\n")
