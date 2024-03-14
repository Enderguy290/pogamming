# FUNCTIONS
# AUTHOR: STANLEY
# 26 FEB 2024


def say_hello():
    print("Hello!")

def say_hello_params(name: str):

    print(f"Hello!, {name}!")

# create a fucntion called say_hello_params
#Create a function called how_big
    # takes a number ad returns howbig iut is

def howbig(num):
    if num < 0:
           return"Very Small"
    if num < 10:
         return"Pretty Small"
    if num < 100:
           return "Small"
    if num < 1000:
             return "Pretty Big"
    return "Really big big boy"


print(howbig(9))
print(howbig(97))
print(howbig(976))
print(howbig(97696))
print(howbig(976967))
# say_hello_params("ewewe")
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()

# function called adder accepts 2 inuts
def adder(x: int,y: int):
      return x + y

print(adder(4,5))