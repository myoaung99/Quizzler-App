from tkinter import *
from typing import Collection
from quiz_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.window = Tk()
        # self in the class means it is the attribute of this class OBJECT
        self.quiz = quiz_brain
        self.window.title("My Quizzler")
        # TITLE of the APP Interface
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # set up the interface

        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.canvas_text = self.canvas.create_text(
            150,
            125,  # center of the window
            text="Some Question",
            width=290,
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)
        # Using image as button

        false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(
            image=false_image, highlightthickness=0, command=self.false_button)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
        # Keep updating the window

    def get_next_question(self):
        self.window.after(1000, self.canvas.config(bg="white"))
        self.score_label.config(
            text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            # If u forget () in calling function The App will display function name
            self.canvas.itemconfig(self.canvas_text, text=q_text)
            # self.button_state('active')

        else:
            self.canvas.itemconfig(self.canvas_text, text="Out of questoins.")
            # self.button_state("disabled")

    def button_state(self, state: str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)

    def true_button(self):
        # messagebox.showinfo(
        #     title="Result", message=self.quiz.check_answer("true"))
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        # messagebox.showinfo(
        #     title="Result", message=self.quiz.check_answer("false"))
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
