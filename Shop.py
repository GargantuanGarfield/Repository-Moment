# ship shop
import random
import Items

print("* CURRENT ITEMS *")
print("-----------------")

# list of current items in the shop + randomly chooses items to put
stock = []
stock_slots = 0  # Amount of items in the shop
while stock_slots != 5:
    rand_item = random.choice(list(Items.all_items))
    if rand_item in stock:
        pass
    else:
        stock.append(rand_item)
        stock_slots += 1

# Structure for shop GUI
item_number = 0
for item in stock:
    item_number += 1
    if item['name'] == '200 Ok Medium Roast Coffee':
        print(f"{item_number}.", item['name'] + ':', item['hp'], item['effect'], '💔')
    elif item['effect'] == 'HEALTH BUFF':
        print(f"{item_number}.", item['name'] + ':', f"+{item['hp']}", item['effect'], '💖')
    elif item['effect'] == 'DAMAGE':
        print(f"{item_number}.", item['name'] + ':', f"+{item['atk']}", item['effect'], '💥')
    elif item['effect'] == 'ARMOR':
        print(f"{item_number}.", item['name'] + ':', f"+{item['armor']}", item['effect'], '👔')

print("-----------------")

# Shop mechanism to allow a player to get 1 free item :)
print("\n☕ Welcome to NetworkChuck's Swap Shop! ☕\n")
while True:
    try:
        purchase = input(
            "Choose your one *FREE* item number from the cloud to FTP to your Neuralink™! :)\n(type 'pass' to skip) ")

        if purchase.lower() == 'pass':
            print("\n... ☕ All NetworkChuck coffee is roasted fresh and at the highest quality ☕ ...")
            break

        purchase_number = int(purchase) - 1
        if 0 <= purchase_number < len(stock):
            bought_item = stock[purchase_number]
            # inventory.append(bought_item)  # TODO: Make this line work later whenever an inventory is implemented :)

            if bought_item['name'] == '200 Ok Medium Roast Coffee':
                print("\n... Wh- What have you done? ...")
                break
            else:
                print(f"\n... ☕ Enjoy your '{bought_item['name']}'! NetworkChuck creates IT Training on YouTube and on "
                      f"NetworkChuck Academy! ☕ ...")
                break

        else:
            print("\nHey MAN... that's not a real item ... Don't waste our bandwidth ...")

    except ValueError:
        print("\nWoah MAN... that's not very 00111010 00110011 of you... ")
        print("(did you mean to type the item number?)\n")
