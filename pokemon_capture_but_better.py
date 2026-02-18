import random
from Legendary_Encounter import *
from Epic_Encounter import *
from Rare_Encounter import *
from Common_Encounter import *
from pokemon_dictionary import *
from pokemon_data import *


POKEMON = random.randint(1, 1000)

if POKEMON == Encounter_rates["Legendary"]:
    legendary = (legendaryEncounter(Catch_rate, pokemon_caught, len_legendary_list, wild_pkmnList))
    print(str(Pokemon_dict[legendary.lower()])+"\n")

    nature = random.randint(0, len(nature_list))

    nature = nature_list[nature]
    print(nature+" nature:")
    nature = natures[nature]
    print(str(nature) +"\n")

elif POKEMON <= Encounter_rates["Epic"] and POKEMON > Encounter_rates["Legendary"]:
    epic = (epicEncounter(Catch_rate, pokemon_caught, len_epic_list, wild_pkmnList))
    print(str(Pokemon_dict[epic.lower()])+"\n")

    nature = random.randint(0, len(nature_list))

    nature = nature_list[nature]
    print(nature+" nature:")
    nature = natures[nature]
    print(str(nature) +"\n")

elif POKEMON <= Encounter_rates["Rare"]and POKEMON > Encounter_rates["Epic"]:
    rare = (rareEncounter(Catch_rate, pokemon_caught, len_rare_list, wild_pkmnList))
    print(str(Pokemon_dict[rare.lower()])+"\n")

    nature = random.randint(0, len(nature_list))

    nature = nature_list[nature]
    print(nature+" nature:")
    nature = natures[nature]
    print(str(nature) +"\n")

elif POKEMON > Encounter_rates["Rare"]:
    common = (commonEncounter(Catch_rate, pokemon_caught, len_common_list, wild_pkmnList))
    print(str(Pokemon_dict[common.lower()])+"\n")

    nature = random.randint(0, len(nature_list))

    nature = nature_list[nature]
    print(nature+" nature:")
    nature = natures[nature]
    print(str(nature) +"\n")

else:
    print("Confusion.")