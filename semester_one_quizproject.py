#semester one project
#basically a random trivia game.
#may include riddles
import random
import time
user_points = 0
question_bucket = [
    {"prompt": "It is physically impossible for pigs to look up at the sky.", "correct_ans": "true"}, 
    {"prompt": "When humans take a breath, they replace only 12 percent of the air in their lungs with fresh air.", "correct_ans": "false"}, 
    {"prompt": "People who work at soda fountains were called soda jerks.","correct_ans": "true"}, 
    {"prompt": "In ancient Greece, killing a horse could be punishable by death.", "correct_ans": "false"}, 
    {"prompt": "According to Egyptian folklore, the god Osiris was the very first mummy.", "correct_ans": "true"},
    {"prompt": "A cat has 34 muscles in each of their ears.", "correct_ans": "false"},
    {"prompt": "Sharks are older than trees and Saturn's rings.", "correct_ans": "true"},
    {"prompt": "Fleas can jump 200 times their body length.", "correct_ans": "false"},
    {"prompt": "The Empire State Building is struck by lightning around 20 times per year.", "correct_ans": "true"},
    {"prompt": "Earthworms have seven pairs of structures that are sort of like a heart.", "correct_ans": "false"}]


def welcome():
    print(" ")
    print("------------ ⋆⋅☆⋅⋆ ------------")
    print("      totally not jeopardy     ")
    print("------------ ⋆⋅☆⋅⋆ ------------")
    print(" ")
    print("Welcome, welcome, welcome to totally not jeopardy!")
    print(" ")
    print("This is a random triva game with several different fact topics.")
    print(" ")
    print("I hope you have fun!")
    print(" ")
    print("------------ ⋆⋅☆⋅⋆ ------------")
    print(" ")
    print(" ")

welcome()

time.sleep(0.5)

while True:
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice == "yes":
        print(" ")
        print("Excellent! The rules are simple: answer the questions, get points, and have fun!")
        print(" ")
        print(" ")
        break
    elif choice == "no":
        print(" ")
        print(".")
        print(" ")
        print(".")
        print(" ")
        print(".")
        print(" ")

while question_bucket:
    current_question = random.choice(question_bucket)
    question = current_question["prompt"]
    correct_answer = current_question["correct_ans"]
    user_answer = input(f"{question} (True/False): ").strip().lower()
    if user_answer == correct_answer:
        print(" ")
        print("Yay! You got it right! +10 points")
        print(" ")
        user_points += 10
    else :
        print(" ")
        print("Nope. Wrong answer!")
        print(" ")
    question_bucket.remove(current_question)

print("· · ─ ·✶· ─ · ·")
print("   game over   ")
print("· · ─ ·✶· ─ · ·")
print(" ")
print(" ")
print("Your score was: ")
print(user_points, "/ 100")
print(" ")