class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        length_of_list = len(self.question_list)

        return self.question_number < length_of_list
        # the above and below are the same.
        # if self.question_number < length_of_list:
        #     return True
        # else:
        #     return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False)?: ")
        self.check_answer(user_answer, current_question.answer) # here we are calling the method

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower() or user_answer[0].lower() == correct_answer[0].lower(): # this user_answer[0] == correct_answer[0] is to make the answer's first letter as answer (i.e) eg: True - t or False - f
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is:{self.score}/{self.question_number}")
        print("\n")