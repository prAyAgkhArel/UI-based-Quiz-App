THEME_COLOR = "#375362"
GREEN = "#00fe00"
RED = "#c30000"
WHITE = "#ffffff"
from tkinter import *      #for creating canvas, buttons
from quiz_brain import QuizBrain  # for tapping into QuizBrain object

class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # now this class understands that
        # quiz_brain is QuizBrain object or its type is QuizBrain so that we can use
        # its methods here
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg= THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125,
                                                     text="xyz",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)
        # now the canvas text will have width 280 if text crosses 280
        # it will be displayed in next line automatically

        image = PhotoImage(file="images/true.png")
        self.true_button = Button(image= image, command= self.true_button_pressed)
        self.true_button.grid(row=2, column=0)
        #self.true_button.config( bg=THEME_COLOR, highlightthickness=0)

        imagee = PhotoImage(file="images/false.png")
        self.false_button = Button(image= imagee, command= self.false_button_pressed)
        self.false_button.grid(row=2, column=1)
        #self.false_button.config(bg=THEME_COLOR, highlightthickness=0)

        self.score_label = Label(text="Score: {0}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column =1)
        #self.score_label.config(padx=20, pady=20, bg=THEME_COLOR, fg="white")

        #calling for next question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        #change bg to white again after 1s of pressing button
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have answered all questions! Look at the scoreboard.")
            # disabling buttons after the end
            self.true_button.config(state= "disabled")
            self.false_button.config(state= "disabled")


    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right == True:
            print("turn canvas green for a sec")
            self.canvas.config(bg = GREEN)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            print("turn canvas red for a sec")
            self.canvas.config(bg= RED)
        self.window.after(1000, self.get_next_question)



