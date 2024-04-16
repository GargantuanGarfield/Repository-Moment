# ship shop
import random

print("network chuck's swap shop")
print("______")

# list of current items in the shop + randomly chooses items to put
stock = []
stock_slots = 0
while stock_slots != 5:
    stock_slots += 1
    rand_item = random.choice(list(Items))  # TODO: make that line work later for however items is implemtned :DDD
    if rand_item in stock:
        pass
    else:
        stock.append(rand_item)

# structure for shop gui
item_number = 0
for item in stock:
    item_number += 1
    print(f"{item_number}.", Item['name'])  # TODO: make this work whenever items is implented..

print("______")

# actual shop function, choose number and get free item
purchase = input("Welcome to Network Chuck's Swap Shop! Choose your ONE free item from the cloud to FTP to your "
                 "Neuralink™ :)\n(type"
                 "'pass' to skip)")
while True:
    try:
        purchase_number = int(purchase) - 1
        if 0 < purchase_number < len(stock):
            bought_item = stock[purchase_number]
            inventory.append(bought_item)  # TODO: make work whenever inventory is plemented... placeholder
            print("")
        else:
            print("Hey MAN... that's not a real item ... Don't waste our bandwidth ...")
    except ValueError:
        print("Woah MAN... that's not very 00111010 00110011 of you...")
        break
