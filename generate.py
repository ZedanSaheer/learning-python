import random

coin = random.choice(["heads", "tails"])
print(coin)

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)

number = random.randint(1,50)
print(number)