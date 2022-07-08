import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=344, height=492)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(text=f"Score: {0}", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR,
                                                     font=('Arial', 16, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        true_img = tk.PhotoImage(file='./images/true.png')
        self.true_button = tk.Button(image=true_img, command=self.guess_true, highlightthickness=0, bd=0)
        self.true_button.grid(column=0, row=2)

        false_img = tk.PhotoImage(file='./images/false.png')
        self.false_button = tk.Button(image=false_img, command=self.guess_false, highlightthickness=0, bd=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.buttons_on_off('active')
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(fg=THEME_COLOR)
            self.canvas.config(bg='black')
            end_message = f"You have reached the end of the quiz.\n\n" \
                          f"Final Score: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, text=end_message, fill='white')

    def guess_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def guess_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.buttons_on_off('disabled')
        self.window.after(1000, self.get_next_question)

    def buttons_on_off(self, button_state):
        self.true_button.config(state=button_state)
        self.false_button.config(state=button_state)
