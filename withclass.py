import json
import random

class QuizGame:
    def __init__(self, questions_file):
        self.questions_file = questions_file
        self.score = 0
        self.questions = []

    def display_score(self):
        print("Your score is now:", self.score)
        if self.score == 0:
            print("This is not great!")

    def check_answer(self, possible_answers):
        user_answer = input("Your answer: ")
        exit_words = ["exit", "quit", "q", "x"]
        if user_answer.lower() in exit_words:
            exit()
        if user_answer.lower() in possible_answers:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")

    def ask_question(self, question_object):
        print(question_object["text"])
        if "wrong" in question_object.keys():
            letters = "ABCDEFG"
            options = question_object["wrong"] + [question_object["answer"][0]]
            random.shuffle(options)
            for item in zip(letters, options):
                letter = item[0]
                option = item[1]
                if option.lower() in question_object["answer"]:
                    question_object["answer"].append(letter.lower())
                option = "{}. {}".format(letter, option.capitalize())
                print(option)
        self.check_answer(question_object["answer"])
        self.display_score()

    def start_game(self):
        with open(self.questions_file, "r") as file:
            self.questions = json.load(file)

        random.shuffle(self.questions)
        for question in self.questions:
            self.ask_question(question)

        print("Game over, thanks for playing!")

if __name__ == "__main__":
    game = QuizGame("questions.json")
    game.start_game()
