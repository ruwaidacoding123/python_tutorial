import random

# Sample question pool
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Leo Tolstoy"],
        "answer": "C"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A) Vincent Van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) O2", "B) H2O", "C) CO2", "D) NaCl"],
        "answer": "B"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["A) 1905", "B) 1912", "C) 1920", "D) 1930"],
        "answer": "B"
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["A) China", "B) Brazil", "C) Russia", "D) USA"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 1", "B) 2", "C) 3", "D) 5"],
        "answer": "B"
    }
]

def add_question():
    question = input("Enter the question: ")
    options = []
    for i in range(4):
        option = input(f"Enter option {chr(65+i)}: ")
        options.append(f"{chr(65+i)}) {option}")
    answer = input("Enter the correct answer (A, B, C, or D): ").upper()
    
    new_question = {
        "question": question,
        "options": options,
        "answer": answer
    }
    
    questions.append(new_question)
    print("Question added successfully!")

def edit_question(index):
    if 0 <= index < len(questions):
        question = questions[index]
        print(f"Editing Question {index + 1}: {question['question']}")
        new_question = input("Enter the new question (leave blank to keep current): ")
        if new_question:
            question["question"] = new_question
        
        for i, option in enumerate(question["options"]):
            new_option = input(f"Enter new option {chr(65+i)} (leave blank to keep current): ")
            if new_option:
                question["options"][i] = f"{chr(65+i)}) {new_option}"
        
        new_answer = input("Enter the correct answer (A, B, C, or D) (leave blank to keep current): ").upper()
        if new_answer:
            question["answer"] = new_answer
        
        print("Question updated successfully!")
    else:
        print("Invalid question number.")

def remove_question(index):
    if 0 <= index < len(questions):
        removed_question = questions.pop(index)
        print(f"Removed Question: {removed_question['question']}")
    else:
        print("Invalid question number.")

def quiz():
    score = 0
    selected_questions = random.sample(questions, 10)
    
    for i, question in enumerate(selected_questions):
        print(f"\nQuestion {i + 1}: {question['question']}")
        for option in question["options"]:
            print(option)
        
        answer = input("Your answer: ").upper()
        
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {question['answer']}.")
    
    print(f"\nYou scored {score} out of 10!")

def main():
    while True:
        print("\n--- Quiz App Menu ---")
        print("1. Start Quiz")
        print("2. Add Question")
        print("3. Edit Question")
        print("4. Remove Question")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            quiz()
        elif choice == "2":
            add_question()
        elif choice == "3":
            index = int(input("Enter the question number to edit: ")) - 1
            edit_question(index)
        elif choice == "4":
            index = int(input("Enter the question number to remove: ")) - 1
            remove_question(index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
