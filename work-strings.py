# Python Introduction
# Author: Stanlywog
# Date: 13 February 2024
import time,random
name = "Stanley"

print ("Greetings!")
time.sleep(2)
print("\nWhat's your name? I am curious to find out!")
user_name = input()
# Takes Input from person and stores it as name forever
presponses = [
    f"{user_name}?",
    f"Not a bad name, {user_name}",
    f"Hm. Heard of {user_name} from somewhere.",
    f"{user_name}? Sounds pretty cool!",
    "Neat!"]
# responses to pick from
response= random.choice(presponses) 
print(response)
# random magic I did before

time.sleep(2)
print(f"How old are you {user_name}?")
inputage = input()
while True:
    try:
        age = int(inputage)
        break
    except(ValueError):
        print("You are not smart, try again.")
        inputage = input()
# test for errors (I have to rememmber hgoiw to do this)
if age < 18:
    print(f"You're very young, {user_name}!")
else:
    print(f"You're very old, {user_name}!")
# comparison of values
print(f"How was your day, {user_name}?")
daygood = input()
print(f"{daygood}???? nice!!")
time.sleep(2)

print(f"What is your favourite food, {user_name}?")
food = input()
print(f"Oh shoot! {food} is my favourite too!")
time.sleep(2)
# some responses
print("What do you feel about Alex Liang?")
hi = input()
print(f"Thats crazy, {hi}?")
time.sleep(2)

print(f"Alright, {user_name}. Good asking you questions (or interrogating you). Have a nice day!")
# bye bye!