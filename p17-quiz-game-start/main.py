from question_model import Question
from data import question_data, open_trivia_data
from quiz_brain import QuizBrain

question_bank: list = []

database_choice = input("Which database would you like to use? Type '1' for question_data or '2' for open_trivia_data: ")

if database_choice == "1":
    question_data = question_data
elif database_choice == "2":
    question_data = open_trivia_data

for question_item in question_data:
    question_bank.append(Question(question_item["question"], question_item["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()
