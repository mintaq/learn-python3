from quick_math import QuickMath

number_of_questions = input(f"How many question do you want:")

quick_math = QuickMath(number_of_questions)

while quick_math.has_next_question():
    quick_math.next_question()

print(f"\nYour score: {quick_math.score}/{number_of_questions}")

if len(quick_math.wrong_answer_lists) > 0:
    print("Correct answers:")
    for answer in quick_math.wrong_answer_lists:
        print(f"{answer.text} = {answer.answer} ({answer.user_answer})")
        