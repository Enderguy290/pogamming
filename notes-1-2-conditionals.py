# Conditionals
# Author: Ubial (MEE)
# Feb 15

x = 1_000_000
y = -5.7

# if x is less than y, say so
# if x is greater than y, say so
# if x is equal to y print so

# if x < y:
#     print("x is less than y")
# if x > y:                                                            
#     print("y is less than x")
# if x == y:
#     print("they're equal dingus")

# if x < y:
#     print("x is less than y")
# elif x > y:                                                            
#     print("y is less than x")
# elif  x == y:
#     print("they're equal dingus")
    
# if x < y:
#     print("x is less than y")
# elif x > y:                                                            
#     print("y is less than x")
# else:
#     print("they're equal dingus")
foo = int(input())

if foo < -1 or foo == 0:
    print("Foo is less than 1, or it is equal")
elif foo > 1 or foo < 1000:
    print("Foo is range 2-999")
else:
    print("outside of range!")