import random

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "text": "What is the capital of Peru?",
                "options": ["Lima", "Madrid", "Santiago", "Bogota"],
                "answer": "Lima"
            },
            {
                "text": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Earth", "Jupiter"],
                "answer": "Mars"
            },
            {
                "text": "What is the largest mammal?",
                "options": ["Blue Whale", "Elephant", "Giraffe", "Hippopotamus"],
                "answer": "Blue Whale"
            },
            {
                "text": "Who wrote 'To Kill a Mockingbird'?",
                "options": ["J.K. Rowling", "Harper Lee", "George Orwell", "F. Scott Fitzgerald"],
                "answer": "Harper Lee"
            }
        ]
        self.score = 0

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def ask_question(self):
        if not self.questions:
            return "Quiz over!"

        question = self.questions.pop(0)
        print(question["text"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")

        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            user_answer = question["options"][int(user_answer) - 1]
            if user_answer == question["answer"]:
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer is {question['answer']}.")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

        return self.ask_question()

    def start(self):
        print("Welcome to the Quiz Game!")
        self.shuffle_questions()
        result = self.ask_question()
        print(f"Quiz over! Your score is {self.score}/{len(self.questions)}.")

if __name__ == "__main__":
    game = QuizGame()
    game.start()