# Deep MOL
# Author: Stanlywog
# Date: 20 February 2024

print("What is the answer to the Great Question of Life, the Universe and Everything?")
MOL = input()
mol = MOL.lower()

if MOL == "42":
    print("Yes")
elif mol == "forty-two" or mol == "forty two":
    print("Yes")
else:
    print("No")