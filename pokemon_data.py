pokemon_caught = False

wild_pkmnList = [
    ["Miraidon", "Zygarde"],
    ["Slither_Wing", "Thundurus"],
    ["Feebas", "Gible"],
    ["Pidgey", "Tandemaus"]
]

Encounter_rates = {
    "Common" : 860,
    "Rare" : 120,
    "Epic" : 19,
    "Legendary" : 1
}

Catch_rate = {
    "Common" : {
        "Pokeball" : 280,
        "Greatball" : 420,
        "Ultraball" : 624,
        "Masterball" :1000
    },
    "Rare" : {
        "Pokeball" : 280,
        "Greatball" : 420,
        "Ultraball" : 624,
        "Masterball" :1000
    },
    "Epic" : {
        "Pokeball" : 280,
        "Greatball" : 420,
        "Ultraball" : 624,
        "Masterball" :1000
    },
    "Legendary" : {
        "Pokeball" : 8,
        "Greatball" : 8,
        "Ultraball" : 16,
        "Masterball" :1000
    }
}

len_legendary_list = len(wild_pkmnList[0])
len_epic_list = len(wild_pkmnList[0])
len_rare_list = len(wild_pkmnList[0])
len_common_list = len(wild_pkmnList[0])