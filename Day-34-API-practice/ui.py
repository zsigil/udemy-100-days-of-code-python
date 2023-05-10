import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(
            text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1, pady=20)

        # canvas
        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas_text = self.canvas.create_text(
            150, 125, text='canvastext', width=280, font=('Arial', 14, 'italic'), fill=THEME_COLOR)
        # buttons
        true_image = tk.PhotoImage(file='images/true.png')
        false_image = tk.PhotoImage(file='images/false.png')

        self.true_button = tk.Button(image=true_image, highlightthickness=0,
                                     border=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, pady=40)

        self.false_button = tk.Button(image=false_image, highlightthickness=0,
                                      border=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.canvas_text, text=f"You've reached the end of the quiz.\n {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
