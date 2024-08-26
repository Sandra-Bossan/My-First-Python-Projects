#QUIZ GAME
questions = [
    {
        "prompt": "Which country is known for its Maple Leaf flag?",
        "options": ["A. Australia", "B. Germany", "C. Vietnam", "D. Canada"],
        "answer": "D"
    },
    {
        "prompt": "Oh no! My sugar's finished. What do I add to sweeten my coffee?",
        "options": ["A. Sugar", "B. Molases", "C. Corn starch", "D. Cocoa powder"],
        "answer": "B"
    },
    {
        "prompt": "Which Scottish explorer is well known for his expenditions of the River Niger in Africa?",
        "options": ["A. Mungo Park", "B. Mary Slessor", "C. Ngugi wa Thiong'o", "D. Wole Soyinka"],
        "answer": "A"
    },
    {
        "prompt": "Who are the founders of Microsoft?",
        "options": ["A. Bill Gates and Paul Allen", "B. Mark Twain and Paul Allen", "C.Bill Gates, Mark Zukerberg", "D. Bill Gates, Elon Musk"],
        "answer": "A"
    },
    {
        "prompt": "What country colonized Germany?",
        "options": ["A. France", "B. Great Britain", "C. It was never colonized", "D. Spain"],
        "answer": "C"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer(A, B, C or D): ").upper()
        if answer == question['answer']:
            print("Well done!d")
            score += 2
        else:
            print("Wrong!! :( The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {2 * len(questions)} answers correct.")

print (run_quiz(questions))