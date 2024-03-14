# EMOJI REPLACER
# Author: Stanlywog
# Date: 227February 2024

# CREATE a function called translate
# accepts a string
# Replace all 100 with 💯
# Replace all noodles with 🍜
# Return the result

# main 
#prompts the user to type something in 
# use translate function on the user input
def translate(input):
    altstring = input.replace("100", "💯").replace("noodles", "🍜")
    return altstring

# Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
def main():
        qans = input("It's translating time! Give me your input.")
        print(translate(qans))

main()