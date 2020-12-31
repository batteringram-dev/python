from Question import Question

question_prompts = [
    "What colour is Apple?\n(a) Yellow\n(b) Pink\n(c) Red\n\n",
    "What colour is Orange?\n(a) Orange\n(b) Pink\n(c) Red\n\n",
    "What colour are Strawberries?\n(a) Red\n(b) Orange\n(c) Yellow\n\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)), "Correct." )

run_test(questions)
