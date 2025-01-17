from question_model import Question
import random

ADDITION = '+'
SUBTRACTION = '-'
MULTIPLICATION = '*'
DIVISION = '/'
OPERATORS = [ADDITION, SUBTRACTION, MULTIPLICATION]
NUMBER_OF_QUESTION = 65


class QuickMath():
    def __init__(self, number_of_questions) -> None:
        self.score = 0
        self.question_number = 0
        self.question_list = self.question_generator(number_of_questions)
        self.wrong_answer_lists = []


    def question_generator(self, number_of_questions: str):
        """
        Create questions according to the number of requests 
        
        Parameters
        ----------
        number_of_questions: str
        
        Return
        ------
        list
            List of questions
        
        """
        question_list = []
        if not number_of_questions.isnumeric():
            number_of_questions = NUMBER_OF_QUESTION
        else:
            number_of_questions = int(number_of_questions)

        while number_of_questions > 0:
            number_of_questions -= 1
            arithmetic_operator = random.choice(OPERATORS)
            number_a = random.randint(0, 30)
            number_b = random.randint(0, number_a)
            text = f"{number_a} {arithmetic_operator} {number_b}"
            if arithmetic_operator == MULTIPLICATION:
                number_a = random.randint(0, 10)
                number_b = random.randint(0, 10)
                answer = number_a * number_b
                text = f"{number_a} {arithmetic_operator} {number_b}"
            elif arithmetic_operator == ADDITION:
                answer = number_a + number_b
            elif arithmetic_operator == SUBTRACTION:
                answer = number_a - number_b

            question_list.append(
                Question(text, answer))

        return question_list

    def has_next_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{current_question.text} = ")
        return self.check_answer(user_answer, current_question)

    def check_answer(self, answer, question):
        if answer.isnumeric() and int(answer) == int(question.answer):
            self.score += 1
        else:
            question.user_answer = answer
            self.wrong_answer_lists.append(question)
