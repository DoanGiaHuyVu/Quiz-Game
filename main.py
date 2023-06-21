from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(0, len(question_data)):
    question_text = question_data[i]["question"]
    question_answer = question_data[i]["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()
quiz.end_of_game()