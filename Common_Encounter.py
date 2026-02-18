import random
from pokemon_data import *


def commonEncounter(Catch_rate, pokemon_caught, len_common_list, wild_pkmnList):
    rarity = Catch_rate["Common"]
    random_pkmn = random.randint(0, len_common_list-1)
    random_pkmn = wild_pkmnList[3][random_pkmn]
    print("You have encountered a Common Pokemon.")
    print(random_pkmn)

    while not pokemon_caught:
        ball = input("What pokeball will you use: ")
        ball = ball.capitalize()

        if ball == "Pokeball":
            capture = random.randint(1, 1000)
            if capture <= rarity["Pokeball"]:
                print("You have caught "+random_pkmn)
                break

            else:
                print(random_pkmn+" was not caught.")

        elif ball == "Greatball":
            capture = random.randint(1, 1000)
            if capture <= rarity["Greatball"]:
                print("You have caught " + random_pkmn)
                break

            else:
                print(random_pkmn + " was not caught.")

        elif ball == "Ultraball":
            capture = random.randint(1, 1000)
            if capture <= rarity["Ultraball"]:
                print("You have caught " + random_pkmn)
                break

            else:
                print(random_pkmn + " was not caught.")

        elif ball == "Masterball":
            capture = random.randint(1, 1000)
            if capture <= rarity["Masterball"]:
                print("You have caught " + random_pkmn)
                break


        elif ball != "Pokeball" and ball != "Greatball" and ball != "Ultraball" and ball != "Masterball":
            print("INVALID")

    return random_pkmn