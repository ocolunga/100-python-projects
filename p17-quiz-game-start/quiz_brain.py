class QuizBrain:
    def __init__(self, q_list: list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.exit_check = False

    def still_has_questions(self):
        if self.exit_check:
            print("You have exited the quiz.")
            return False
        if self.question_number == len(self.question_list):
            print(
                f"You've completed the quiz. Final score: {self.score}/{self.question_number}"
            )
            return False
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        correct_answer = current_question.answer
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )
        if user_answer.lower() == "exit":
            self.exit_check = True
        else:
            self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Incorrect answer")
        print(f"The correct answer was: {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")
