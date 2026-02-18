import random
from pokemon_data import *


def rareEncounter(Catch_rate, pokemon_caught, len_rare_list, wild_pkmnList):
    rarity = Catch_rate["Rare"]
    random_pkmn = random.randint(0, len_rare_list-1)
    random_pkmn = wild_pkmnList[2][random_pkmn]
    print("You have encountered a Rare Pokemon.")
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

        if ball == "Greatball":
            capture = random.randint(1, 1000)
            if capture <= rarity["Greatball"]:
                print("You have caught " + random_pkmn)
                break

            else:
                print(random_pkmn + " was not caught.")

        if ball == "Ultraball":
            capture = random.randint(1, 1000)
            if capture <= rarity["Ultraball"]:
                print("You have caught " + random_pkmn)
                break

            else:
                print(random_pkmn + " was not caught.")

        if ball == "Masterball":
            capture = random.randint(1, 1000)
            if capture <= rarity["Masterball"]:
                print("You have caught " + random_pkmn)
                break


        elif ball != "Pokeball" and ball != "Greatball" and ball != "Ultraball" and ball != "Masterball":
            print("INVALID")

    return random_pkmn