#semester one project
#basically a random trivia game.
#may include riddles
from typing import Final
import random
import time
user_points = 0
VALID_TRUE_INPUTS: Final = ("true", "t", "yes", "y")
VALID_FALSE_INPUTS: Final = ("false", "no", "n", "f")
TOTAL_QUESTIONS: Final = 10
POINTS_PER_QUESTION: Final = 10
def user_score(user_points):
    percentage = (user_points/(TOTAL_QUESTIONS * POINTS_PER_QUESTION)) * 100
    return percentage

def typing_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.02, 0.15))
    print()

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
    {"prompt": "Earthworms have seven pairs of structures that are sort of like a heart.", "correct_ans": "false"},
    {"prompt": "It is impossible for most people to lick their own elbow.", "correct_ans": "true"},
    {"prompt": "Wearing headphones for just an hour can increase the bacteria in your ear by 600 times.", "correct_ans": "false"},
    {"prompt": "If you sneeze too hard, you could have fracture an rib.", "correct_ans": "true"},
    {"prompt": "If the course of an average lifetime, while sleeping you might eat around 80 assorted insects and 10 spiders, or more.", "correct_ans": "false"},
    {"prompt": "Some lipsticks contain fish scales.", "correct_ans": "true"},
    {"prompt": "There are 294 ways to make change for a dollar.", "correct_ans": "false"},
    {"prompt": "Rubber bands last longer when refrigerated.", "correct_ans": "true"},
    {"prompt": "The average person's left hand does 54 percent of the typing.", "correct_ans": "false"},
    {"prompt": "A shark is the only known fish that can blink with both eyes.", "correct_ans": "true"},
    {"prompt": "A dime has 117 ridges around the edge", "correct_ans": "false"},
    {"prompt": "In many advertisements, the time displayed on a watch is 10:10.", "correct_ans": "true"},
    {"prompt": "Most people fall asleep in eight minutes.", "correct_ans": "false"},
    {"prompt": "The giant squid has the largest eyes in the world.", "correct_ans": "true"},
    {"prompt": "Almonds are not part of the peach family.", "correct_ans": "false"},
    {"prompt": "Dreamt is the only English word that ends in the letters 'mt'.", "correct_ans": "true"},
    {"prompt": "Lobsters have purple blood.", "correct_ans": "false"},
    {"prompt": "Napolean Bonaparte was once attacked by a swarm of rabbits.", "correct_ans": "true"},
    {"prompt": "It takes roughly 550 peanuts to make a jar of peanut butter.", "correct_ans": "false"},
    {"prompt": "Lightning can turn sand into glass.", "correct_ans": "true"},
    {"prompt": "The bee hummingbird, the smallest bird in the world, drinks nectar from up to 1,600 flowers a day.", "correct_ans": "false"}]

game_questions = random.sample(question_bucket, TOTAL_QUESTIONS)

def welcome():
    typing_effect(" ")
    print("------------ ⋆⋅☆⋅⋆ ------------")
    typing_effect("      totally not jeopardy     ")
    print("------------ ⋆⋅☆⋅⋆ ------------")
    typing_effect(" ")
    typing_effect("Welcome, welcome, welcome to totally not jeopardy!")
    typing_effect(" ")
    typing_effect("This is a random triva game with several different fact topics.")
    typing_effect(" ")
    typing_effect("I hope you have fun!")
    typing_effect(" ")
    print("------------ ⋆⋅☆⋅⋆ ------------")
    typing_effect(" ")
    typing_effect(" ")

welcome()

time.sleep(0.5)

while True:
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice == "yes":
        typing_effect(" ")
        typing_effect("Excellent! The rules are simple: answer the questions, get points, and have fun!")
        typing_effect(" ")
        typing_effect(" ")
        break
    elif choice == "no":
        typing_effect(" ")
        typing_effect(".")
        typing_effect(" ")
        typing_effect(".")
        typing_effect(" ")
        typing_effect(".")
        typing_effect(" ")

for index, item in enumerate(game_questions,1):
    question = item["prompt"]
    correct_answer = item["correct_ans"]
    typing_effect(f"Question {index} of {TOTAL_QUESTIONS}")
    typing_effect(question)
    while True:
        user_answer = input(f"(True/False): ").strip().lower()
        if user_answer in VALID_TRUE_INPUTS:
            user_answer = "true"
            break
        elif user_answer in VALID_FALSE_INPUTS:
            user_answer = "false"
            break
        else:
            typing_effect(" ")
            typing_effect("Invalid answer. Please enter true or false!!")
            typing_effect(" ")
    if user_answer == correct_answer:
        typing_effect(" ")
        typing_effect("Yay! You got it right! +10 points")
        typing_effect(" ")
        user_points += POINTS_PER_QUESTION
    else:
        typing_effect(" ")
        typing_effect("Nope. Wrong answer!")
        typing_effect(" ")

print("· · ─ ·✶· ─ · ·")
typing_effect("   game over   ")
print("· · ─ ·✶· ─ · ·")
typing_effect(" ")
typing_effect(" ")
typing_effect("Your score was: ")
print(user_points, "/", TOTAL_QUESTIONS * POINTS_PER_QUESTION)
percentage = user_score(user_points)
typing_effect(f"You got {percentage:.1f}%!")
typing_effect(" ")
#saves the user's score into a text file
#"a" is for adding your previous scores into the text file
try:
    with open("previous_scores.txt", "a") as file:
        file.write(f"Score: {user_points}/100\n")
#OSError is short for "Operating System Error" and it's when you cannot
#save your text files because something went wrong when Python tried to access it
except OSError:
    typing_effect("There was an error saving your score...")
    typing_effect(":(")

else:
    typing_effect("Your score was saved successfully!!")

finally:
    typing_effect("Thank you for playing!!!")

#shows previous scores :)
try:
    with open("previous_scores.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    typing_effect("no previous scores found!!")
    typing_effect("try again later :(")