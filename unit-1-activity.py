# Unit 1 activity(subsequentunlimitedsituationsimulator)
# author: stanleywong
# march 4

import random, time

global money
money = 0
shankval = 0
equippedweapon = 0
ewn = "nothing"
bronze_sword = 3
wolf_fang = 4

bs = "bronze sword"
wf = "wolf fang"

ed = False
turncount = 0
# give a background for a fantasy world and print it
def print_iab(input: str):
    print(
        f"Your name is {input}. You are an adventurer, who woke up in the middle of a forest. You have probably been here for a while considering the state of the grass you're on."
    )
    # time.sleep(3)
    print(
        f"Looking around you, you can find a pouch of ten gold and a bronze sword next to the vaguely {input} shaped patch on the ground. You pick all of the items up. You feel like if you ever lose all your money,you will die. (reflective like real life!)"
    )
    # time.sleep(3)


def rerand():
    global money, equippedweapon, ewn
    renum = random.randint(0,6)
    if renum == 5:
        re5()
    elif renum == 4:
        re4()
    elif renum == 3:
        re3()
    elif renum == 2:
        re2()
    elif renum == 1:
        if ed == False:
            re1()
        elif ed == True:
            print("You see a blacksmith's shop, but it is unoccupied, and the blinds are shut.")
    elif renum == 6:
        re6()
    else:
        print("You kept walking into the unknown.")
    # time.sleep(2)

def ri():
    return random.randint(1,5)

def re6():
    global money
    print(
        f"You have {money} gold in your pocket, which does not seem like a lot, but it adds up."
    )
    print(
        f"You have a {ewn} in your hand, which does {equippedweapon} damage.")
    gamblingyn = input("You walk into a casino, the dealer shows you cards and 3 shufflers subsequently. He says that he will give you a number from 0 to 42 and he also the same. Whoever is closest to 21 wins 50% of your current money. Wanna gamble? (y/n)")
    if gamblingyn == "y":
        ynum = random.randint(0,42)
        hnum = random.randint(0,42)
        if abs(ynum-21) < abs(hnum-21):
            money = money + money//2
            print(f"You were closer to 21! You win. Your money is now {money} dongs. You hit {ynum} and your opponent hit {hnum}.")
        else:
            money = money//2
            print(f"Damn, he took half of your money. Never trust these scammers! Gambling is fun though, you have {money} zlotys left. You hit {ynum} and your opponent hit {hnum}.")
    elif gamblingyn == "n":
        print("You walk out, controlling your urges to throw your money away.")










#blacksmith encounter
def re1():
    global money, equippedweapon, ewn, ed
    print(
        f"You have {money} gold in your pocket, which does not seem like a lot, but it adds up."
    )
    print(
        f"You have a {ewn} in your hand, which does {equippedweapon} damage.")
    # time.sleep(2)
    buysword = input(f"You see a blacksmith's shop in the distance. When you knock, he humbly walks out with a giant sword the size of a door, which does 5 damage. He offers it to you for 50% of your dollaradoos, which is {int(money)/2}. Would you like to buy it? (y/n)").lower()

    if buysword == "y":
        bwn = input("He pulls out a marker and asks you to name it personally, and he collects your money. (insert name here)")
        money = int(money) // 2
        ewn = bwn
        equippedweapon = 5
        print(f"You have a {ewn} in your hand, which does {equippedweapon} damage.")
        print(f"You have {money} gold in your pocket after this encounter, which does not seem like a lot, but it adds up.")
        ed = True
    elif buysword == "n":
        print("He goes back inside his little hut, and he looks sad")
        ed = True

# encounter 5: big dog goes funny dead and gives you a small upgrade or dollars
def re5():
    global money, equippedweapon, ewn, bs, wf, wolf_fang
    print(
        f"You have {money} gold in your pocket, which does not seem like a lot, but it adds up."
    )
    print(
        f"You have a {ewn} in your hand, which does {equippedweapon} damage.")
    # time.sleep(2)
    re5resp = input("You see a wolf. Do you want to fight it? (y/n)").lower()
    if re5resp == "y":
        print("You fight the wolf.")
        # time.sleep(3)
        wolfdollar = random.randint(3, 5)
        print(
            f"You have a {ewn} in your hand. The wolf extends a bag with {wolfdollar} dollars in it. He has equipped his two paw mitt hands, which would do {wolfdollar} damage to you if your weapon damage didn't exceed {wolfdollar}."
        )
        if equippedweapon >= wolfdollar:
            print(
                f"You show your {ewn} to the wolf. He falls over. You have killed the wolf. You gained {wolfdollar} gold."
            )
            # time.sleep(4)
            money = money + wolfdollar
            if ewn == "wolf fang":
                equippedweapon = equippedweapon
                ewn = ewn
            else:
                print(
                    f"After the encounter, you feel barbaric. You scrounge for anything to gain other than wealth. You find a wolf fang."
                )
                wrespose = input(f"The wolf fang does {wolf_fang} damage, now you have {ewn} equipped, which does {equippedweapon} damage. Would you like to equip it? (y/n)").lower()
                if wrespose == "y":
                    equippedweapon = int(wolf_fang)
                    ewn = str(wf)
                elif wrespose == "n":
                    equippedweapon = equippedweapon
                    ewn = ewn

        elif equippedweapon <= wolfdollar:
            print(
                f"You show your {ewn} to the wolf. He laughs at you. He takes {wolfdollar} gold from you and leaves you feeling ridiculed."
            )
            money = money - wolfdollar
    elif re5resp == "n":
        print(
            "You walk away, content with your decision and choice to not box a dog canine."
        )


# encounter 4: you find merchant and he scams you (or gives you money)
def re4():
    global money, equippedweapon, damage, ewn, bs, wf, bronze_sword
    print(
        f"You have {money} gold in your pocket, which does not seem like a lot, but it adds up."
    )
    print(
        f"You have a {ewn} in your hand, which does {equippedweapon} damage.")
    # time.sleep(2)
    re4resp = input(
        "You see a merchant sitting next to the road. Do you want to talk to him? (y/n)"
    ).lower()
    if re4resp == "y":
        got = ri()
        defactor = random.randint(1, 2)
        if defactor == 1:
            print(
                f"The merchant says, 'I'm going to die of starvation. Just have my remaining {got} gold.'"
            )
            money = money + got
        else:
            print(
                f"Haha you thought you could talk to me? I'm a wizard and a scammer. I'm going to take {got} dollars from you and leave."
            )
            money = money - got
            # time.sleep(2)
            print(
                f"A wizard AND a scammer? Damn thats unlucky. You have {money} left."
            )
    elif re4resp == "n":
        print("You leave the merchant flabbergastered, wondering why you ignored him.")

# encounter 3: stealing dog


def re3():
    global money, equippedweapon, damage, ewn, bs, wf, bronze_sword
    print(
        f"You have {money} gold in your pocket, which does not seem like a lot, but it adds up."
    )
    print(
        f"You have a {ewn} in your hand, which does {equippedweapon} damage.")
    # time.sleep(2)
    re3money = ri()
    addorlose = random.randint(1, 2)
    if addorlose == 1:
        money = money + re3money
        print(
            f"You found a satchel with a whole {re3money}! You have {money} now!"
        )
    elif addorlose == 2:
        money = money - re3money
        print(
            f"You tripped and lost {re3money} gold, unlucky! You have {money} left."
        )


def re2():
    global money, equippedweapon, damage, ewn, bs, wf, bronze_sword, shankval
    print(
        f"You have {money} gold in your pocket, which does not seem like a lot, but it adds up."
    )
    print(
        f"You have a {ewn} in your hand, which does {equippedweapon} damage.")
    # time.sleep(2)
    print(
        f"You see a dog with a tophat. You can't tell if its really a dog. You can't tell. It walks up to you, offering two boxes. He shows the content of the boxes. The first one contains a chunk of depleted uranium, and the second one contains 10 dollars. He shufles the boxes around."
    )
    uorshank = random.randint(1, 2)
    dogresp = input(f"Do you want to take a box? (y/n)").lower()
    if dogresp == "y":
        print(f"You pick up one of the boxes and open it.")
        if uorshank == 1:
            money = money - 4
            print(
                f"You found a chunk of the uranium. You feel a bit sick and you lose 4 dollars due to wobbling around. You have {money} gold left."
            )
        elif uorshank == 2:
            money = money + 10
            print(
                f"You found a whole 10 dollars. You feel richer and revitalized!"
            )
    elif dogresp == "n":
        print(
            f"You walk away, confused at why the dog has riches or a chunk of uranium and two giftboxes or a tophat at all."
        )


name = input("Hello mysterious entity, what is your name?")
print_iab(name)
money = money + 10

if input(f"The bronze sword does {bronze_sword} damage, now you have {ewn} equipped, which does {equippedweapon} damage. Would you like to equip it? (y/n)").lower() == "y":
    equippedweapon = bronze_sword
    ewn = str(bs)
else:
    equippedweapon = equippedweapon
    ewn = ewn

while True:
    if money >= 42:
        print(
            f"You see a divine light shine down from the heavens. It beckons you towards a shining gateway that leads to paradise. You have successfully accquired more than 42 gold, and conquered the infinite loop of the SUSS. Your final dollar count is {money} and you went for {turncount} turns. Thanks for playing!"
        )
        break
    elif money > 0:
        time.sleep(1.5)
        rerand()
        turncount = turncount + 1
    elif money <= 0:
        print(f"You have became broke and died. Game over! You lasted {turncount} turns.")
        break
