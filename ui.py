from tkinter import *
from typing import Collection

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self) -> None:
        self.window = Tk()
        # self in the class means it is the attribute of this class OBJECT

        self.window.title("My Quizzler")
        # TITLE of the APP Interface
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # set up the interface

        self.scroe_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.scroe_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.canvas_text = self.canvas.create_text(
            150,
            125,  # center of the window
            text="Some Question text",
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        # Using image as button

        false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=false_image, highlightthickness=0)
        self.true_button.grid(row=2, column=1)

        self.window.mainloop()
        # Keep updating the window
