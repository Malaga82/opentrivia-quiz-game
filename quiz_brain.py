class QuizBrain:
  def __init__(self, question_bank):
    self.question_number = 0
    self.question_list = question_bank
    self.score = 0

  def still_has_questions(self):
    #print(len(self.question_list))
    while (self.question_number != len(self.question_list)):
      return True
    #return False

  def next_question(self):
    #number = self.question_number
    current_question = self.question_list[self.question_number]
    self.question_number = self.question_number + 1
    choice = input(f'Q.{self.question_number}: {current_question.text} (True/False)?: ')
    self.check_answer(choice, current_question.answer)

  def check_answer(self, choice, current_answer):
    if (choice.lower() == current_answer.lower()):
      self.score += 1
      print("You got i right!")
    else:
      print("That's wrong dude!!!")
    print(f'The correct answer is: {current_answer}.')
    print(f"Your score is: {self.score}/{self.question_number}")
    print("\n")
