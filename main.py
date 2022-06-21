from question_model import Question
from data import question_data, question_trivia
from quiz_brain import QuizBrain
import html
question_bank=[]
#print(question_trivia)
for question in question_trivia:
  if question_trivia[question] == 0:
    pass
  else:
    for trivia in question_trivia[question]:
      #print(trivia)
      q = Question(html.unescape(trivia['question']),trivia['correct_answer'])
      question_bank.append(q)
    #print(f"question list: {question_trivia[question]}")
  #q = Question(question[0]["results"], question[0]["results"])
  #question_bank.append(q)

#print(question_bank)

qb = QuizBrain(question_bank)


while qb.still_has_questions():
  qb.next_question()

print("You completed the quiz")
print(f"your final score is {qb.score}/{qb.question_number}")