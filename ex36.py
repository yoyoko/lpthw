def england(): #if / elif / else
    print("We're staying local.")
    print("Where should we look?")
    choice = input("> ")
    if "london" in choice or "London" in choice:
        print("We found a boy named Theo Walcott")
        print("He can play either left or right wing")
        print("Where should we play him?")
        choice = input("> ")
        if choice == "left":
            dead("Here's a terrible left wing")
        elif choice == "right":
            print("He is a great find. You win!")
    else:
        dead(f"We looked forever and could not find anyone in {choice}.")

def spain(): #for loop practice
    spanish_players = ["Mata", "Cazorla", "Isco"]
    print("Welcome to Spain.")
    print("Here are the players we are looking at")
    for players in spanish_players:
        print(players)
    print("Is there anyone else you want to add?")
    choice = input("> ")
    spanish_players.append(choice)
    print("Here is our new list:")
    for players in spanish_players:
        print(players)

def brazil(): #not complete
    print("Welcome to Brazil")
    print("There's this kid, Neymar, that you have to look at")
    print("You see him standing there. What do you do?")
    neymar_cheap = False

    while True:
        choice = input("> ")

        if choice == "pay him":
            dead("He takes your money and runs")
        elif choice == "pay his dad" and not neymar_cheap:
            print("His dad takes the money")
        elif choice == "pay his dad" and neymar_cheap:


def start():
    print("Welcome to the club.")
    print("Let's sign some new players.")
    print("Where should we look for new players?")
    choice = input("> ")
    if "england" in choice or "England" in choice:
        england()
    elif "spain" in choice or "Spain" in choice:
        spain()
    elif "brazil" in choice or "Brazil" in choice:
        brazil()
    else:
        dead("We can't afford that.")

def dead(reason):
    print(reason, "You're fired!")
    exit(0)

start()
