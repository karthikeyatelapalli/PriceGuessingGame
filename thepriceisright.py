
#Description



import random

def price():
    return random.randint(1000, 5000)
#a random price is generated between 1000 to 5000


prize = price()

bids = []
for i in range(1, 5):
    bid = int(input("Player {}, what is your bid? ".format(i)))
    bids.append(bid)

over = True
for bid in bids:
    if bid <= prize:
        over = False
        break
if over:
    print("Buzz! Aww... everyone has overbid!")
# if overbid then it prints overbid


exact = False
for bid in bids:
    if bid == prize:
        exact = True
        print("Ding Ding Ding! One player got it exactly right and gets $500!")
        break
# if exactly bid then prints ding ding ding


if not exact:
    closest = min(bids, key = lambda x: (x-prize)**2)
    print("Actual price is ${}! Player {}, come on up!".format(prize, bids.index(closest)+1))

#checks the closest bid by using lambda function
