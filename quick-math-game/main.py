from quick_math import QuickMath

number_of_questions = int(input(f"How many question do you want:"))

quick_math = QuickMath(number_of_questions)

while quick_math.has_next_question():
    quick_math.next_question()
    
print(f"Your score: {quick_math.score}/{number_of_questions}")