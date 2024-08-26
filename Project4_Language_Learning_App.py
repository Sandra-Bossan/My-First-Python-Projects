# LANGUAGE LEARNING APP
import random

basic_numbers = [
    {"French": "un", "English": 1},
    {"French": "deux", "English": 2},
    {"French": "trois", "English": 3},
    {"French": "quatre", "English": 4},
    {"French": "cinq", "English": 5},
    {"French": "six", "English": 6},
    {"French": "sept", "English": 7},
    {"French": "huit", "English": 8},
    {"French": "neuf", "English": 9},
    {"French": "dix", "English": 10},
]

def quiz_numbers(basic_numbers):
    random.shuffle(basic_numbers)
    score = 0

    for number in basic_numbers:
        print(f"What is the English translation of '{number['French']}'?")
        user_answer = input("Your answer (number): ").strip()
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        
        correct_answer = number["English"]

        if user_answer == correct_answer:
            print("Correct, you genius!\n")
            score += 1
        else:
            print(f"Uh oh, the correct answer is '{correct_answer}'.\n")

    print(f"Quiz complete! You scored {score}/{len(basic_numbers)} points! We are so proud of you.\n")

def quiz_articles(articles):
    random.shuffle(articles)
    score = 0

    for article in articles:
        print(f"What is the English translation of '{article['French']}'?")
        user_answer = input("Your answer: ").strip().lower()
        
        correct_answer = article["English"]

        if user_answer == correct_answer.lower():
            print("Correct, you genius!\n")
            score += 1
        else:
            print(f"Uh oh, the correct answer is '{correct_answer}'.\n")

    print(f"Quiz complete! You scored {score}/{len(articles)} points. We are so proud of you!\n")

def main():
    print("Welcome to Let's Learn French Together")
    print("Hello, it's so great having you learn French here!")
    print("Ready to Learn? Let's Go")
    input("Press Enter to Start Learning...")
    print("FUN FACT: French is often referred to as the “language of love” because of its melodious sound and romantic connotations.\n")
    print("Let's begin with a practice on numbers")
    quiz_numbers(basic_numbers)

# NOUNS AND DEFINITE ARTICLES
definite_articles1 = [
    {"French": "le", "English": "the"},
    {"French": "la", "English": "the"},
    {"French": "l'", "English": "the"},
    {"French": "les", "English": "the"},
]

nouns_with_articles = [
    {"French": "la chaise", "English": "the chair"},
    {"French": "le professeur", "English": "the teacher"},
    {"French": "l’étudiant", "English": "the student"},
]

def main2():
    print("Now let's learn about Nouns and Articles in French")
    print("Ready to Learn? Let's Go")
    
    while True:
        print('1. Start Learning')
        print('2. Exit')
        choice = input('Enter your choice (1/2): ').strip()
        
        if choice == '1':
            quiz_articles(definite_articles1)
            break
        elif choice == '2':
            print("\nAre you sure you want to exit Let's Learn French Together?")
            print('1. Yes')
            print('2. No')
            ur_choice = input('Enter your choice (1/2): ').strip()
            if ur_choice == '1':
                print('Thank you for learning with us. Goodbye!')
                return
        else:
            print('Invalid choice, please choose again.')
    
    print("A definite article is specific; it defines the number and gender of the noun it corresponds to. In English, the only definite article is 'the', whereas in French there are four: la, le, l’, and les.\n")
    print(f"{definite_articles1}\n")
    print("Take a short quiz to test your knowledge on French articles")
    input("Press Enter to take quiz...")
    quiz_articles(definite_articles1)

    print("Important Note: 'Le' and 'la' both become 'l’' when they come before a noun beginning with a vowel or a silent 'h'. Examples: l’homme, l’université.\nWhen 'les' is followed by a word starting with a vowel, the normally silent final 's' of 'les' is pronounced, making a /z/ sound.")
    
    print("Take a short quiz to test your knowledge on Nouns with Definite Articles")
    input("Press Enter to take quiz...")
    quiz_articles(nouns_with_articles)

if __name__ == "__main__":
    main()
    main2()