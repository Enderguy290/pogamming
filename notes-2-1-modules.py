import random

# random.random()
# random = 0, 1.0
heads = 0
tails = 0
other = 0
def coinflip():
    global heads, tails, other
    #  Return head til or oother
    # heads -- [0 - 0.5]
    #tails -- [0.5, 0.999999]
    result = random.random()

    if result < 0.5:
        heads = heads + 1

        return "heads"
    elif result < 0.99999:
        tails = tails + 1

        return "tails"
    else:
        other = other + 1

        return "other"

    
def main():
    print(coinflip())
    


for i in range(100000):
    main()
print(f"{heads} {tails} {other}")    
