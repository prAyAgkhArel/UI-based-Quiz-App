from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import UserInterface



quiz = QuizBrain(question_data)
# here question_data is the list of Question objects which has q_text and q_answer
# and the list of question ojects are passed in __init__ (constructor) which is held
# by the variable q_list in qui_brain.py


userinterface = UserInterface(quiz)
# Since quiz is a QuizBrain object, here Quizbrain object is being passed in constructor of
# UserInterface class , now we can use this quiz in ui.py to get access of QuizBrain methods

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
