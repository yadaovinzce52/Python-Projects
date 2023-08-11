class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        curr_question = self.q_list[self.q_num]
        self.q_num += 1
        choice = input(f'Q.{self.q_num}: {curr_question.text} (True/False)?: ')
        self.check_answer(choice, curr_question.answer)

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def check_answer(self, choice, answer):
        if choice.lower() == answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('That\'s wrong.')
            print(f"The correct answer is {answer}.")
        print(f"Your current score is: {self.score}/{self.q_num}\n\n")
