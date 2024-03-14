# String method
# Author:question 
#  asdfghjkl

# Ask the user what is the weather like
weather = input("What is the weather like?\n")
# If they reply rainy
    #bring an umbrella
if weather.lower().strip("!_-+={[}]|\:;'!@#$%^&}<>?,./   6")  == "rainy":
    print("You'll need an umbrella!")
else:
    print(f"Sorry, I don't understand {weather}.")