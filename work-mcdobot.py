# McDonalds Bot (minimum wage worker)
# Author: Stanlywog
# Date: 22 February 2024

while True:
    mcd = input("DO YOU WANT FRIES WITH YO MEAL (im not paid enough to be happy)?").lower().strip("!_-+={[}]|\:;'!@#$%^&}<>?,./   6")
    MCD = mcd.upper()
    if mcd == "yes":
            print("OK I WILL ADD FRIES TO YOUR MEAL, HERE IT IS")
            break

    elif mcd == "no":
            print("OK NO FRIES THEN, HERE IT IS")
            break

    else:
            print(f"WHATS A {MCD}??? I DONT UNDERSTAND")