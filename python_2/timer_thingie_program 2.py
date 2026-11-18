#This is the start of my one semester long project.
student_name = "Joshitha"
aura_points = 0
is_staff = False
stawp = "no thanks bro. im good. hehehe"
print (student_name, "has", aura_points, "aura points currently.")

print("-----------------------")
print("    story generator   ")
print("-----------------------")
print("Welcome, welcome, welcome to the story generator!")
print("")

user_name = input("Enter a name: ")

if user_name == "easter egg":
    print("11")

print("Hello, " + user_name.title(), "!")
print(" ")
    
print("pretend this is the entire rest of the code and everything is finished lol...")

import time
def typewriter_effect(text, delay=0.06):
    for char in text:
        typing_effect(char, end='', flush=True)
        time.sleep(delay)
    typing_effect()

typewriter_effect("HIYA! This is me trying out the typewriter effect...")
import time
import random
def typing_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.02, 0.15))
    print()

typing_effect("pretend this is the entire rest of the code and everything is finished lol...")
