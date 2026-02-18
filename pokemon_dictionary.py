natures = {
    "hardy" : {},
    "lonely" : {"attack" : 1.1, "defense" : 0.9},
    "adamant" : {"attack" : 1.1, "special_attack" : 0.9},
    "naughty" : {"attack" : 1.1, "special_defense" : 0.9},
    "brave" : {"attack" : 1.1, "speed" : 0.9},

    "docile" : {},
    "bold" : {"defense" : 1.1, "attack" : 0.9},
    "impish" : {"defense" : 1.1, "special_attack" : 0.9},
    "lax" : {"defense" : 1.1, "special_defense" : 0.9},
    "relaxed": {"defense": 1.1, "speed" : 0.9},

    "bashful" : {},
    "modest" : {"special_attack" : 1.1, "attack" : 0.9},
    "mild" : {"special_attack" : 1.1, "defense" : 0.9},
    "rash" : {"special_attack" : 1.1, "special_defense" : 0.9},
    "quiet" : {"special_attack" : 1.1, "speed" : 0.9},

    "quirky" : {},
    "calm" : {"special_defense" : 1.1, "attack" : 0.9},
    "gentle" : {"special_defense" : 1.1, "defense" : 0.9},
    "careful" : {"special_defense" : 1.1, "special_attack" : 0.9},
    "sassy" : {"special_defense" : 1.1, "speed" : 0.9},

    "serious" : {},
    "timid" : {"speed" : 1.1, "attack" : 0.9},
    "hasty" : {"speed" : 1.1, "defense" : 0.9},
    "jolly" : {"speed" : 1.1, "special_attack" : 0.9},
    "naive" : {"speed" : 1.1, "special_defense" : 0.9},
}

nature_list = [
    "hardy", "lonely", "adamant", "naughty", "brave",
    "docile", "bold", "impish", "lax", "relaxed",
    "bashful", "modest", "mild", "rash", "quiet",
    "quirky", "calm", "gentle", "careful", "sassy",
    "serious", "timid", "hasty", "jolly", "naive"
]

Pokemon_dict = {
    "bulbasaur": {"number": 1, "type": ["grass", "poison"]},
    "ivysaur": {"number": 2, "type": ["grass", "poison"]},
    "venusaur": {"number": 3, "type": ["grass", "poison"], "mega": True},

    "charmander": {"number": 4, "type": ["fire"]},
    "charmeleon": {"number": 5, "type": ["fire"]},
    "charizard": {"number": 6, "type": ["fire", "flying"], "mega": {"Mega_X", "Mega_Y"}},

    "squirtle": {"number": 7, "type": ["water"]},
    "wartortle": {"number": 8, "type": ["water"]},
    "blastoise": {"number": 9, "type": ["water"], "mega": True},

    "caterpie": {"number": 10, "type": ["bug"]},
    "metapod": {"number": 11, "type": ["bug"]},
    "butterfree": {"number": 12, "type": ["bug", "flying"]},

    "weedle": {"number": 13, "type": ["bug", "poison"]},
    "kakuna": {"number": 14, "type": ["bug", "poison"]},
    "beedrill": {"number": 15, "type": ["bug", "poison"], "mega": True},

    "pidgey": {"number": 16, "type": ["normal", "flying"]},
    "pidgeotto": {"number": 17, "type": ["normal", "flying"]},
    "pidgeot": {"number": 18, "type": ["normal", "flying"], "mega": True},

    "rattata": {"number": 19, "type": ["normal"]},
    "raticate": {"number": 20, "type": ["normal"]},

    "spearow": {"number": 21, "type": ["normal", "flying"]},
    "fearow": {"number": 22, "type": ["normal", "flying"]},

    "ekans": {"number": 23, "type": ["poison"]},
    "arbok": {"number": 24, "type": ["poison"]},

    "pikachu": {"number": 25, "type": ["electric"], "z_move": "catastropika"},
    "pikachu_cap": {"number": 25, "type": ["electric"], "z_move": "10,000,000 volt thunderbolt"},
    "raichu": {"number": 26, "type": ["electric"], "mega": {"Mega_X", "Mega_Y"}},
    "alolan_raichu": {"number": 26, "type": ["electric", "psychic"], "z_move": "stoked sparksurfer"},

    "sandshrew": {"number": 27, "type": ["ground"]},
    "sandslash": {"number": 28, "type": ["ground"]},

    "nidoran_f": {"number": 29, "type": ["poison"]},
    "nidorina": {"number": 30, "type": ["poison"]},
    "nidoqueen": {"number": 31, "type": ["poison", "ground"]},

    "nidoran_m": {"number": 32, "type": ["poison"]},
    "nidorino": {"number": 33, "type": ["poison"]},
    "nidoking": {"number": 34, "type": ["poison", "ground"]},

    "clefairy": {"number": 35, "type": ["fairy"]},
    "clefable": {"number": 36, "type": ["fairy"]},

    "vulpix": {"number": 37, "type": ["fire"]},
    "ninetales": {"number": 38, "type": ["fire"]},

    "jigglypuff": {"number": 39, "type": ["normal", "fairy"]},
    "wigglytuff": {"number": 40, "type": ["normal", "fairy"]},

    "zubat": {"number": 41, "type": ["poison", "flying"]},
    "golbat": {"number": 42, "type": ["poison", "flying"]},

    "oddish": {"number": 43, "type": ["grass", "poison"]},
    "gloom": {"number": 44, "type": ["grass", "poison"]},
    "vileplume": {"number": 45, "type": ["grass", "poison"]},

    "paras": {"number": 46, "type": ["bug", "grass"]},
    "parasect": {"number": 47, "type": ["bug", "grass"]},

    "venonat": {"number": 48, "type": ["bug", "poison"]},
    "venomoth": {"number": 49, "type": ["bug", "poison"]},

    "diglett": {"number": 50, "type": ["ground"]},
    "dugtrio": {"number": 51, "type": ["ground"]},

    "meowth": {"number": 52, "type": ["normal"]},
    "persian": {"number": 53, "type": ["normal"]},

    "psyduck": {"number": 54, "type": ["water"]},
    "golduck": {"number": 55, "type": ["water"]},

    "mankey": {"number": 56, "type": ["fighting"]},
    "primeape": {"number": 57, "type": ["fighting"]},

    "growlithe": {"number": 58, "type": ["fire"]},
    "arcanine": {"number": 59, "type": ["fire"]},

    "poliwag": {"number": 60, "type": ["water"]},
    "poliwhirl": {"number": 61, "type": ["water"]},
    "poliwrath": {"number": 62, "type": ["water", "fighting"]},

    "abra": {"number": 63, "type": ["psychic"]},
    "kadabra": {"number": 64, "type": ["psychic"]},
    "alakazam": {"number": 65, "type": ["psychic"]},

    "machop": {"number": 66, "type": ["fighting"]},
    "machoke": {"number": 67, "type": ["fighting"]},
    "machamp": {"number": 68, "type": ["fighting"]},

    "bellsprout": {"number": 69, "type": ["grass", "poison"]},
    "weepinbell": {"number": 70, "type": ["grass", "poison"]},
    "victreebel": {"number": 71, "type": ["grass", "poison"]},

    "tentacool": {"number": 72, "type": ["water", "poison"]},
    "tentacruel": {"number": 73, "type": ["water", "poison"]},

    "geodude": {"number": 74, "type": ["rock", "ground"]},
    "graveler": {"number": 75, "type": ["rock", "ground"]},
    "golem": {"number": 76, "type": ["rock", "ground"]},

    "ponyta": {"number": 77, "type": ["fire"]},
    "rapidash": {"number": 78, "type": ["fire"]},

    "slowpoke": {"number": 79, "type": ["water", "psychic"]},
    "slowbro": {"number": 80, "type": ["water", "psychic"]},

    "magnemite": {"number": 81, "type": ["electric", "steel"]},
    "magneton": {"number": 82, "type": ["electric", "steel"]},

    "farfetchd": {"number": 83, "type": ["normal", "flying"]},

    "doduo": {"number": 84, "type": ["normal", "flying"]},
    "dodrio": {"number": 85, "type": ["normal", "flying"]},

    "seel": {"number": 86, "type": ["water"]},
    "dewgong": {"number": 87, "type": ["water", "ice"]},

    "grimer": {"number": 88, "type": ["poison"]},
    "muk": {"number": 89, "type": ["poison"]},

    "shellder": {"number": 90, "type": ["water"]},
    "cloyster": {"number": 91, "type": ["water", "ice"]},

    "gastly": {"number": 92, "type": ["ghost", "poison"]},
    "haunter": {"number": 93, "type": ["ghost", "poison"]},
    "gengar": {"number": 94, "type": ["ghost", "poison"]},

    "onix": {"number": 95, "type": ["rock", "ground"]},

    "drowzee": {"number": 96, "type": ["psychic"]},
    "hypno": {"number": 97, "type": ["psychic"]},

    "krabby": {"number": 98, "type": ["water"]},
    "kingler": {"number": 99, "type": ["water"]},

    "voltorb": {"number": 100, "type": ["electric"]},
    "electrode": {"number": 101, "type": ["electric"]},

    "exeggcute": {"number": 102, "type": ["grass", "psychic"]},
    "exeggutor": {"number": 103, "type": ["grass", "psychic"]},

    "cubone": {"number": 104, "type": ["ground"]},
    "marowak": {"number": 105, "type": ["ground"]},

    "hitmonlee": {"number": 106, "type": ["fighting"]},
    "hitmonchan": {"number": 107, "type": ["fighting"]},

    "lickitung": {"number": 108, "type": ["normal"]},

    "koffing": {"number": 109, "type": ["poison"]},
    "weezing": {"number": 110, "type": ["poison"]},

    "rhyhorn": {"number": 111, "type": ["ground", "rock"]},
    "rhydon": {"number": 112, "type": ["ground", "rock"]},

    "chansey": {"number": 113, "type": ["normal"]},

    "tangela": {"number": 114, "type": ["grass"]},

    "kangaskhan": {"number": 115, "type": ["normal"]},

    "horsea": {"number": 116, "type": ["water"]},
    "seadra": {"number": 117, "type": ["water"]},

    "goldeen": {"number": 118, "type": ["water"]},
    "seaking": {"number": 119, "type": ["water"]},

    "staryu": {"number": 120, "type": ["water"]},
    "starmie": {"number": 121, "type": ["water", "psychic"]},

    "mr_mime": {"number": 122, "type": ["psychic", "fairy"]},

    "scyther": {"number": 123, "type": ["bug", "flying"]},

    "jynx": {"number": 124, "type": ["ice", "psychic"]},

    "electabuzz": {"number": 125, "type": ["electric"]},
    "magmar": {"number": 126, "type": ["fire"]},

    "pinsir": {"number": 127, "type": ["bug"]},

    "tauros": {"number": 128, "type": ["normal"]},

    "magikarp": {"number": 129, "type": ["water"]},
    "gyarados": {"number": 130, "type": ["water", "flying"]},

    "lapras": {"number": 131, "type": ["water", "ice"]},

    "ditto": {"number": 132, "type": ["normal"]},

    "eevee": {"number": 133, "type": ["normal"], "z_move": "extreme evoboost"},
    "vaporeon": {"number": 134, "type": ["water"]},
    "jolteon": {"number": 135, "type": ["electric"]},
    "flareon": {"number": 136, "type": ["fire"]},

    "porygon": {"number": 137, "type": ["normal"]},

    "omanyte": {"number": 138, "type": ["rock", "water"]},
    "omastar": {"number": 139, "type": ["rock", "water"]},

    "kabuto": {"number": 140, "type": ["rock", "water"]},
    "kabutops": {"number": 141, "type": ["rock", "water"]},

    "aerodactyl": {"number": 142, "type": ["rock", "flying"]},

    "snorlax": {"number": 143, "type": ["normal"], "z_move": "pulverizing pancake"},

    "articuno": {"number": 144, "type": ["ice", "flying"]},
    "zapdos": {"number": 145, "type": ["electric", "flying"]},
    "moltres": {"number": 146, "type": ["fire", "flying"]},

    "dratini": {"number": 147, "type": ["dragon"]},
    "dragonair": {"number": 148, "type": ["dragon"]},
    "dragonite": {"number": 149, "type": ["dragon", "flying"]},

    "mewtwo": {"number": 150, "type": ["psychic"]},
    "mew": {"number": 151, "type": ["psychic"], "z_move": "genesis supernova"},

    "chikorita": {"number": 152, "type": ["grass"]},
    "bayleef": {"number": 153, "type": ["grass"]},
    "meganium": {"number": 154, "type": ["grass"]},

    "cyndaquil": {"number": 155, "type": ["fire"]},
    "quilava": {"number": 156, "type": ["fire"]},
    "typhlosion": {"number": 157, "type": ["fire"]},

    "totodile": {"number": 158, "type": ["water"]},
    "croconaw": {"number": 159, "type": ["water"]},
    "feraligatr": {"number": 160, "type": ["water"]},

    "sentret": {"number": 161, "type": ["normal"]},
    "furret": {"number": 162, "type": ["normal"]},

    "hoothoot": {"number": 163, "type": ["normal", "flying"]},
    "noctowl": {"number": 164, "type": ["normal", "flying"]},

    "ledyba": {"number": 165, "type": ["bug", "flying"]},
    "ledian": {"number": 166, "type": ["bug", "flying"]},

    "spinarak": {"number": 167, "type": ["bug", "poison"]},
    "ariados": {"number": 168, "type": ["bug", "poison"]},

    "crobat": {"number": 169, "type": ["poison", "flying"]},

    "chinchou": {"number": 170, "type": ["water", "electric"]},
    "lanturn": {"number": 171, "type": ["water", "electric"]},

    "pichu": {"number": 172, "type": ["electric"]},

    "cleffa": {"number": 173, "type": ["fairy"]},
    "igglybuff": {"number": 174, "type": ["normal", "fairy"]},
    "togepi": {"number": 175, "type": ["fairy"]},
    "togetic": {"number": 176, "type": ["fairy", "flying"]},

    "natu": {"number": 177, "type": ["psychic", "flying"]},
    "xatu": {"number": 178, "type": ["psychic", "flying"]},

    "mareep": {"number": 179, "type": ["electric"]},
    "flaaffy": {"number": 180, "type": ["electric"]},
    "ampharos": {"number": 181, "type": ["electric"]},

    "bellossom": {"number": 182, "type": ["grass"]},

    "marill": {"number": 183, "type": ["water", "fairy"]},
    "azumarill": {"number": 184, "type": ["water", "fairy"]},

    "sudowoodo": {"number": 185, "type": ["rock"]},

    "politoed": {"number": 186, "type": ["water"]},

    "hoppip": {"number": 187, "type": ["grass", "flying"]},
    "skiploom": {"number": 188, "type": ["grass", "flying"]},
    "jumpluff": {"number": 189, "type": ["grass", "flying"]},

    "aipom": {"number": 190, "type": ["normal"]},

    "sunkern": {"number": 191, "type": ["grass"]},
    "sunflora": {"number": 192, "type": ["grass"]},

    "yanma": {"number": 193, "type": ["bug", "flying"]},

    "wooper": {"number": 194, "type": ["water", "ground"]},
    "quagsire": {"number": 195, "type": ["water", "ground"]},

    "espeon": {"number": 196, "type": ["psychic"]},
    "umbreon": {"number": 197, "type": ["dark"]},

    "murkrow": {"number": 198, "type": ["dark", "flying"]},

    "slowking": {"number": 199, "type": ["water", "psychic"]},

    "misdreavus": {"number": 200, "type": ["ghost"]},

    "unown": {"number": 201, "type": ["psychic"]},

    "wobbuffet": {"number": 202, "type": ["psychic"]},

    "girafarig": {"number": 203, "type": ["normal", "psychic"]},

    "pineco": {"number": 204, "type": ["bug"]},
    "forretress": {"number": 205, "type": ["bug", "steel"]},

    "dunsparce": {"number": 206, "type": ["normal"]},

    "gligar": {"number": 207, "type": ["ground", "flying"]},

    "steelix": {"number": 208, "type": ["steel", "ground"]},

    "snubbull": {"number": 209, "type": ["fairy"]},
    "granbull": {"number": 210, "type": ["fairy"]},

    "qwilfish": {"number": 211, "type": ["water", "poison"]},

    "scizor": {"number": 212, "type": ["bug", "steel"]},

    "shuckle": {"number": 213, "type": ["bug", "rock"]},

    "heracross": {"number": 214, "type": ["bug", "fighting"]},

    "sneasel": {"number": 215, "type": ["dark", "ice"]},

    "teddiursa": {"number": 216, "type": ["normal"]},
    "ursaring": {"number": 217, "type": ["normal"]},

    "slugma": {"number": 218, "type": ["fire"]},
    "magcargo": {"number": 219, "type": ["fire", "rock"]},

    "swinub": {"number": 220, "type": ["ice", "ground"]},
    "piloswine": {"number": 221, "type": ["ice", "ground"]},

    "corsola": {"number": 222, "type": ["water", "rock"]},

    "remoraid": {"number": 223, "type": ["water"]},
    "octillery": {"number": 224, "type": ["water"]},

    "delibird": {"number": 225, "type": ["ice", "flying"]},

    "mantine": {"number": 226, "type": ["water", "flying"]},

    "skarmory": {"number": 227, "type": ["steel", "flying"]},

    "houndour": {"number": 228, "type": ["dark", "fire"]},
    "houndoom": {"number": 229, "type": ["dark", "fire"]},

    "kingdra": {"number": 230, "type": ["water", "dragon"]},

    "phanpy": {"number": 231, "type": ["ground"]},
    "donphan": {"number": 232, "type": ["ground"]},

    "porygon2": {"number": 233, "type": ["normal"]},

    "stantler": {"number": 234, "type": ["normal"]},

    "smeargle": {"number": 235, "type": ["normal"]},

    "tyrogue": {"number": 236, "type": ["fighting"]},
    "hitmontop": {"number": 237, "type": ["fighting"]},

    "smoochum": {"number": 238, "type": ["ice", "psychic"]},
    "elekid": {"number": 239, "type": ["electric"]},
    "magby": {"number": 240, "type": ["fire"]},

    "miltank": {"number": 241, "type": ["normal"]},

    "blissey": {"number": 242, "type": ["normal"]},

    "raikou": {"number": 243, "type": ["electric"]},
    "entei": {"number": 244, "type": ["fire"]},
    "suicune": {"number": 245, "type": ["water"]},

    "larvitar": {"number": 246, "type": ["rock", "ground"]},
    "pupitar": {"number": 247, "type": ["rock", "ground"]},
    "tyranitar": {"number": 248, "type": ["rock", "dark"]},

    "lugia": {"number": 249, "type": ["psychic", "flying"]},
    "ho_oh": {"number": 250, "type": ["fire", "flying"]},

    "celebi": {"number": 251, "type": ["psychic", "grass"]},

    "treecko": {"number": 252, "type": ["grass"]},
    "grovyle": {"number": 253, "type": ["grass"]},
    "sceptile": {"number": 254, "type": ["grass"]},

    "torchic": {"number": 255, "type": ["fire"]},
    "combusken": {"number": 256, "type": ["fire", "fighting"]},
    "blaziken": {"number": 257, "type": ["fire", "fighting"]},

    "mudkip": {"number": 258, "type": ["water"]},
    "marshtomp": {"number": 259, "type": ["water", "ground"]},
    "swampert": {"number": 260, "type": ["water", "ground"]},

    "poochyena": {"number": 261, "type": ["dark"]},
    "mightyena": {"number": 262, "type": ["dark"]},

    "zigzagoon": {"number": 263, "type": ["normal"]},
    "linoone": {"number": 264, "type": ["normal"]},

    "wurmple": {"number": 265, "type": ["bug"]},
    "silcoon": {"number": 266, "type": ["bug"]},
    "beautifly": {"number": 267, "type": ["bug", "flying"]},
    "cascoon": {"number": 268, "type": ["bug"]},
    "dustox": {"number": 269, "type": ["bug", "poison"]},

    "lotad": {"number": 270, "type": ["water", "grass"]},
    "lombre": {"number": 271, "type": ["water", "grass"]},
    "ludicolo": {"number": 272, "type": ["water", "grass"]},

    "seedot": {"number": 273, "type": ["grass"]},
    "nuzleaf": {"number": 274, "type": ["grass", "dark"]},
    "shiftry": {"number": 275, "type": ["grass", "dark"]},

    "taillow": {"number": 276, "type": ["normal", "flying"]},
    "swellow": {"number": 277, "type": ["normal", "flying"]},

    "wingull": {"number": 278, "type": ["water", "flying"]},
    "pelipper": {"number": 279, "type": ["water", "flying"]},

    "ralts": {"number": 280, "type": ["psychic", "fairy"]},
    "kirlia": {"number": 281, "type": ["psychic", "fairy"]},
    "gardevoir": {"number": 282, "type": ["psychic", "fairy"]},

    "surskit": {"number": 283, "type": ["bug", "water"]},
    "masquerain": {"number": 284, "type": ["bug", "flying"]},

    "shroomish": {"number": 285, "type": ["grass"]},
    "breloom": {"number": 286, "type": ["grass", "fighting"]},

    "slakoth": {"number": 287, "type": ["normal"]},
    "vigoroth": {"number": 288, "type": ["normal"]},
    "slaking": {"number": 289, "type": ["normal"]},

    "nincada": {"number": 290, "type": ["bug", "ground"]},
    "ninjask": {"number": 291, "type": ["bug", "flying"]},
    "shedinja": {"number": 292, "type": ["bug", "ghost"]},

    "whismur": {"number": 293, "type": ["normal"]},
    "loudred": {"number": 294, "type": ["normal"]},
    "exploud": {"number": 295, "type": ["normal"]},

    "makuhita": {"number": 296, "type": ["fighting"]},
    "hariyama": {"number": 297, "type": ["fighting"]},

    "azurill": {"number": 298, "type": ["normal", "fairy"]},

    "nosepass": {"number": 299, "type": ["rock"]},

    "skitty": {"number": 300, "type": ["normal"]},
    "delcatty": {"number": 301, "type": ["normal"]},

    "sableye": {"number": 302, "type": ["dark", "ghost"]},
    "mawile": {"number": 303, "type": ["steel", "fairy"]},

    "aron": {"number": 304, "type": ["steel", "rock"]},
    "lairon": {"number": 305, "type": ["steel", "rock"]},
    "aggron": {"number": 306, "type": ["steel", "rock"]},

    "meditite": {"number": 307, "type": ["fighting", "psychic"]},
    "medicham": {"number": 308, "type": ["fighting", "psychic"]},

    "electrike": {"number": 309, "type": ["electric"]},
    "manectric": {"number": 310, "type": ["electric"]},

    "plusle": {"number": 311, "type": ["electric"]},
    "minun": {"number": 312, "type": ["electric"]},

    "volbeat": {"number": 313, "type": ["bug"]},
    "illumise": {"number": 314, "type": ["bug"]},

    "roselia": {"number": 315, "type": ["grass", "poison"]},

    "gulpin": {"number": 316, "type": ["poison"]},
    "swalot": {"number": 317, "type": ["poison"]},

    "carvanha": {"number": 318, "type": ["water", "dark"]},
    "sharpedo": {"number": 319, "type": ["water", "dark"]},

    "wailmer": {"number": 320, "type": ["water"]},
    "wailord": {"number": 321, "type": ["water"]},

    "numel": {"number": 322, "type": ["fire", "ground"]},
    "camerupt": {"number": 323, "type": ["fire", "ground"]},

    "torkoal": {"number": 324, "type": ["fire"]},

    "spoink": {"number": 325, "type": ["psychic"]},
    "grumpig": {"number": 326, "type": ["psychic"]},

    "spinda": {"number": 327, "type": ["normal"]},

    "trapinch": {"number": 328, "type": ["ground"]},
    "vibrava": {"number": 329, "type": ["ground", "dragon"]},
    "flygon": {"number": 330, "type": ["ground", "dragon"]},

    "cacnea": {"number": 331, "type": ["grass"]},
    "cacturne": {"number": 332, "type": ["grass", "dark"]},

    "swablu": {"number": 333, "type": ["normal", "flying"]},
    "altaria": {"number": 334, "type": ["dragon", "flying"]},

    "zangoose": {"number": 335, "type": ["normal"]},
    "seviper": {"number": 336, "type": ["poison"]},

    "lunatone": {"number": 337, "type": ["rock", "psychic"]},
    "solrock": {"number": 338, "type": ["rock", "psychic"]},

    "barboach": {"number": 339, "type": ["water", "ground"]},
    "whiscash": {"number": 340, "type": ["water", "ground"]},

    "corphish": {"number": 341, "type": ["water"]},
    "crawdaunt": {"number": 342, "type": ["water", "dark"]},

    "baltoy": {"number": 343, "type": ["ground", "psychic"]},
    "claydol": {"number": 344, "type": ["ground", "psychic"]},

    "lileep": {"number": 345, "type": ["rock", "grass"]},
    "cradily": {"number": 346, "type": ["rock", "grass"]},

    "anorith": {"number": 347, "type": ["rock", "bug"]},
    "armaldo": {"number": 348, "type": ["rock", "bug"]},

    "feebas": {"number": 349, "type": ["water"]},
    "milotic": {"number": 350, "type": ["water"]},

    "castform": {"number": 351, "type": ["normal"]},

    "kecleon": {"number": 352, "type": ["normal"]},

    "shuppet": {"number": 353, "type": ["ghost"]},
    "banette": {"number": 354, "type": ["ghost"]},

    "duskull": {"number": 355, "type": ["ghost"]},
    "dusclops": {"number": 356, "type": ["ghost"]},

    "tropius": {"number": 357, "type": ["grass", "flying"]},

    "chimecho": {"number": 358, "type": ["psychic"]},

    "absol": {"number": 359, "type": ["dark"]},

    "wynaut": {"number": 360, "type": ["psychic"]},

    "snorunt": {"number": 361, "type": ["ice"]},
    "glalie": {"number": 362, "type": ["ice"]},

    "spheal": {"number": 363, "type": ["ice", "water"]},
    "sealeo": {"number": 364, "type": ["ice", "water"]},
    "walrein": {"number": 365, "type": ["ice", "water"]},

    "clamperl": {"number": 366, "type": ["water"]},
    "huntail": {"number": 367, "type": ["water"]},
    "gorebyss": {"number": 368, "type": ["water"]},

    "relicanth": {"number": 369, "type": ["water", "rock"]},
    "luvdisc": {"number": 370, "type": ["water"]},

    "bagon": {"number": 371, "type": ["dragon"]},
    "shelgon": {"number": 372, "type": ["dragon"]},
    "salamence": {"number": 373, "type": ["dragon", "flying"]},

    "beldum": {"number": 374, "type": ["steel", "psychic"]},
    "metang": {"number": 375, "type": ["steel", "psychic"]},
    "metagross": {"number": 376, "type": ["steel", "psychic"]},

    "regirock": {"number": 377, "type": ["rock"]},
    "regice": {"number": 378, "type": ["ice"]},
    "registeel": {"number": 379, "type": ["steel"]},

    "latias": {"number": 380, "type": ["dragon", "psychic"]},
    "latios": {"number": 381, "type": ["dragon", "psychic"]},

    "kyogre": {"number": 382, "type": ["water"]},
    "groudon": {"number": 383, "type": ["ground"]},
    "rayquaza": {"number": 384, "type": ["dragon", "flying"]},

    "jirachi": {"number": 385, "type": ["steel", "psychic"]},
    "deoxys": {"number": 386, "type": ["psychic"]},

    "turtwig": {"number": 387, "type": ["grass"]},
    "grotle": {"number": 388, "type": ["grass"]},
    "torterra": {"number": 389, "type": ["grass", "ground"]},

    "chimchar": {"number": 390, "type": ["fire"]},
    "monferno": {"number": 391, "type": ["fire", "fighting"]},
    "infernape": {"number": 392, "type": ["fire", "fighting"]},

    "piplup": {"number": 393, "type": ["water"]},
    "prinplup": {"number": 394, "type": ["water"]},
    "empoleon": {"number": 395, "type": ["water", "steel"]},

    "starly": {"number": 396, "type": ["normal", "flying"]},
    "staravia": {"number": 397, "type": ["normal", "flying"]},
    "staraptor": {"number": 398, "type": ["normal", "flying"]},

    "bidoof": {"number": 399, "type": ["normal"]},
    "bibarel": {"number": 400, "type": ["normal", "water"]},

    "kricketot": {"number": 401, "type": ["bug"]},
    "kricketune": {"number": 402, "type": ["bug"]},

    "shinx": {"number": 403, "type": ["electric"]},
    "luxio": {"number": 404, "type": ["electric"]},
    "luxray": {"number": 405, "type": ["electric"]},

    "budew": {"number": 406, "type": ["grass", "poison"]},
    "roserade": {"number": 407, "type": ["grass", "poison"]},

    "cranidos": {"number": 408, "type": ["rock"]},
    "rampardos": {"number": 409, "type": ["rock"]},

    "shieldon": {"number": 410, "type": ["rock", "steel"]},
    "bastiodon": {"number": 411, "type": ["rock", "steel"]},

    "burmy": {"number": 412, "type": ["bug"]},
    "wormadam": {"number": 413, "type": ["bug", "grass"]},
    "mothim": {"number": 414, "type": ["bug", "flying"]},

    "combee": {"number": 415, "type": ["bug", "flying"]},
    "vespiquen": {"number": 416, "type": ["bug", "flying"]},

    "pachirisu": {"number": 417, "type": ["electric"]},

    "buizel": {"number": 418, "type": ["water"]},
    "floatzel": {"number": 419, "type": ["water"]},

    "cherubi": {"number": 420, "type": ["grass"]},
    "cherrim": {"number": 421, "type": ["grass"]},

    "shellos": {"number": 422, "type": ["water"]},
    "gastrodon": {"number": 423, "type": ["water", "ground"]},

    "ambipom": {"number": 424, "type": ["normal"]},

    "drifloon": {"number": 425, "type": ["ghost", "flying"]},
    "drifblim": {"number": 426, "type": ["ghost", "flying"]},

    "buneary": {"number": 427, "type": ["normal"]},
    "lopunny": {"number": 428, "type": ["normal"]},

    "mismagius": {"number": 429, "type": ["ghost"]},

    "honchkrow": {"number": 430, "type": ["dark", "flying"]},

    "glameow": {"number": 431, "type": ["normal"]},
    "purugly": {"number": 432, "type": ["normal"]},

    "chingling": {"number": 433, "type": ["psychic"]},

    "stunky": {"number": 434, "type": ["poison", "dark"]},
    "skuntank": {"number": 435, "type": ["poison", "dark"]},

    "bronzor": {"number": 436, "type": ["steel", "psychic"]},
    "bronzong": {"number": 437, "type": ["steel", "psychic"]},

    "bonsly": {"number": 438, "type": ["rock"]},

    "mime_jr": {"number": 439, "type": ["psychic", "fairy"]},

    "happiny": {"number": 440, "type": ["normal"]},

    "chatot": {"number": 441, "type": ["normal", "flying"]},

    "spiritomb": {"number": 442, "type": ["ghost", "dark"]},

    "gible": {"number": 443, "type": ["dragon", "ground"]},
    "gabite": {"number": 444, "type": ["dragon", "ground"]},
    "garchomp": {"number": 445, "type": ["dragon", "ground"]},

    "munchlax": {"number": 446, "type": ["normal"]},

    "riolu": {"number": 447, "type": ["fighting"]},
    "lucario": {"number": 448, "type": ["fighting", "steel"]},

    "hippopotas": {"number": 449, "type": ["ground"]},
    "hippowdon": {"number": 450, "type": ["ground"]},

    "skorupi": {"number": 451, "type": ["poison", "bug"]},
    "drapion": {"number": 452, "type": ["poison", "dark"]},

    "croagunk": {"number": 453, "type": ["poison", "fighting"]},
    "toxicroak": {"number": 454, "type": ["poison", "fighting"]},

    "carnivine": {"number": 455, "type": ["grass"]},

    "finneon": {"number": 456, "type": ["water"]},
    "lumineon": {"number": 457, "type": ["water"]},

    "mantyke": {"number": 458, "type": ["water", "flying"]},

    "snover": {"number": 459, "type": ["grass", "ice"]},
    "abomasnow": {"number": 460, "type": ["grass", "ice"]},

    "weavile": {"number": 461, "type": ["dark", "ice"]},

    "magnezone": {"number": 462, "type": ["electric", "steel"]},

    "lickilicky": {"number": 463, "type": ["normal"]},

    "rhyperior": {"number": 464, "type": ["ground", "rock"]},

    "tangrowth": {"number": 465, "type": ["grass"]},

    "electivire": {"number": 466, "type": ["electric"]},

    "magmortar": {"number": 467, "type": ["fire"]},

    "togekiss": {"number": 468, "type": ["fairy", "flying"]},

    "yanmega": {"number": 469, "type": ["bug", "flying"]},

    "leafeon": {"number": 470, "type": ["grass"]},
    "glaceon": {"number": 471, "type": ["ice"]},

    "gliscor": {"number": 472, "type": ["ground", "flying"]},

    "mamoswine": {"number": 473, "type": ["ice", "ground"]},

    "porygon_z": {"number": 474, "type": ["normal"]},

    "gallade": {"number": 475, "type": ["psychic", "fighting"]},

    "probopass": {"number": 476, "type": ["rock", "steel"]},

    "dusknoir": {"number": 477, "type": ["ghost"]},

    "froslass": {"number": 478, "type": ["ice", "ghost"]},

    "rotom": {"number": 479, "type": ["electric", "ghost"]},

    "uxie": {"number": 480, "type": ["psychic"]},
    "mesprit": {"number": 481, "type": ["psychic"]},
    "azelf": {"number": 482, "type": ["psychic"]},

    "dialga": {"number": 483, "type": ["steel", "dragon"]},
    "palkia": {"number": 484, "type": ["water", "dragon"]},
    "heatran": {"number": 485, "type": ["fire", "steel"]},

    "regigigas": {"number": 486, "type": ["normal"]},

    "giratina": {"number": 487, "type": ["ghost", "dragon"]},

    "cresselia": {"number": 488, "type": ["psychic"]},

    "phione": {"number": 489, "type": ["water"]},
    "manaphy": {"number": 490, "type": ["water"]},

    "darkrai": {"number": 491, "type": ["dark"]},

    "shaymin": {"number": 492, "type": ["grass"]},

    "arceus": {"number": 493, "type": ["normal"]},

    "victini": {"number": 494, "type": ["psychic", "fire"]},

    "snivy": {"number": 495, "type": ["grass"]},
    "servine": {"number": 496, "type": ["grass"]},
    "serperior": {"number": 497, "type": ["grass"]},

    "tepig": {"number": 498, "type": ["fire"]},
    "pignite": {"number": 499, "type": ["fire", "fighting"]},
    "emboar": {"number": 500, "type": ["fire", "fighting"]},

    "oshawott": {"number": 501, "type": ["water"]},
    "dewott": {"number": 502, "type": ["water"]},
    "samurott": {"number": 503, "type": ["water"]},

    "patrat": {"number": 504, "type": ["normal"]},
    "watchog": {"number": 505, "type": ["normal"]},

    "lillipup": {"number": 506, "type": ["normal"]},
    "herdier": {"number": 507, "type": ["normal"]},
    "stoutland": {"number": 508, "type": ["normal"]},

    "purrloin": {"number": 509, "type": ["dark"]},
    "liepard": {"number": 510, "type": ["dark"]},

    "pansage": {"number": 511, "type": ["grass"]},
    "simisage": {"number": 512, "type": ["grass"]},
    "pansear": {"number": 513, "type": ["fire"]},
    "simisear": {"number": 514, "type": ["fire"]},
    "panpour": {"number": 515, "type": ["water"]},
    "simipour": {"number": 516, "type": ["water"]},

    "munna": {"number": 517, "type": ["psychic"]},
    "musharna": {"number": 518, "type": ["psychic"]},

    "pidove": {"number": 519, "type": ["normal", "flying"]},
    "tranquill": {"number": 520, "type": ["normal", "flying"]},
    "unfezant": {"number": 521, "type": ["normal", "flying"]},

    "blitzle": {"number": 522, "type": ["electric"]},
    "zebstrika": {"number": 523, "type": ["electric"]},

    "roggenrola": {"number": 524, "type": ["rock"]},
    "boldore": {"number": 525, "type": ["rock"]},
    "gigalith": {"number": 526, "type": ["rock"]},

    "woobat": {"number": 527, "type": ["psychic", "flying"]},
    "swoobat": {"number": 528, "type": ["psychic", "flying"]},

    "drilbur": {"number": 529, "type": ["ground"]},
    "excadrill": {"number": 530, "type": ["ground", "steel"]},

    "audino": {"number": 531, "type": ["normal"]},

    "timburr": {"number": 532, "type": ["fighting"]},
    "gurdurr": {"number": 533, "type": ["fighting"]},
    "conkeldurr": {"number": 534, "type": ["fighting"]},

    "tympole": {"number": 535, "type": ["water"]},
    "palpitoad": {"number": 536, "type": ["water", "ground"]},
    "seismitoad": {"number": 537, "type": ["water", "ground"]},

    "throh": {"number": 538, "type": ["fighting"]},
    "sawk": {"number": 539, "type": ["fighting"]},

    "sewaddle": {"number": 540, "type": ["bug", "grass"]},
    "swadloon": {"number": 541, "type": ["bug", "grass"]},
    "leavanny": {"number": 542, "type": ["bug", "grass"]},

    "venipede": {"number": 543, "type": ["bug", "poison"]},
    "whirlipede": {"number": 544, "type": ["bug", "poison"]},
    "scolipede": {"number": 545, "type": ["bug", "poison"]},

    "cottonee": {"number": 546, "type": ["grass", "fairy"]},
    "whimsicott": {"number": 547, "type": ["grass", "fairy"]},

    "petilil": {"number": 548, "type": ["grass"]},
    "lilligant": {"number": 549, "type": ["grass"]},

    "basculin": {"number": 550, "type": ["water"]},

    "sandile": {"number": 551, "type": ["ground", "dark"]},
    "krokorok": {"number": 552, "type": ["ground", "dark"]},
    "krookodile": {"number": 553, "type": ["ground", "dark"]},

    "darumaka": {"number": 554, "type": ["fire"]},
    "darmanitan": {"number": 555, "type": ["fire"]},

    "maractus": {"number": 556, "type": ["grass"]},

    "dwebble": {"number": 557, "type": ["bug", "rock"]},
    "crustle": {"number": 558, "type": ["bug", "rock"]},

    "scraggy": {"number": 559, "type": ["dark", "fighting"]},
    "scrafty": {"number": 560, "type": ["dark", "fighting"]},

    "sigilyph": {"number": 561, "type": ["psychic", "flying"]},

    "yamask": {"number": 562, "type": ["ghost"]},
    "cofagrigus": {"number": 563, "type": ["ghost"]},

    "tirtouga": {"number": 564, "type": ["water", "rock"]},
    "carracosta": {"number": 565, "type": ["water", "rock"]},

    "archen": {"number": 566, "type": ["rock", "flying"]},
    "archeops": {"number": 567, "type": ["rock", "flying"]},

    "trubbish": {"number": 568, "type": ["poison"]},
    "garbodor": {"number": 569, "type": ["poison"]},

    "zorua": {"number": 570, "type": ["dark"]},
    "zoroark": {"number": 571, "type": ["dark"]},

    "minccino": {"number": 572, "type": ["normal"]},
    "cinccino": {"number": 573, "type": ["normal"]},

    "gothita": {"number": 574, "type": ["psychic"]},
    "gothorita": {"number": 575, "type": ["psychic"]},
    "gothitelle": {"number": 576, "type": ["psychic"]},

    "solosis": {"number": 577, "type": ["psychic"]},
    "duosion": {"number": 578, "type": ["psychic"]},
    "reuniclus": {"number": 579, "type": ["psychic"]},

    "ducklett": {"number": 580, "type": ["water", "flying"]},
    "swanna": {"number": 581, "type": ["water", "flying"]},

    "vanillite": {"number": 582, "type": ["ice"]},
    "vanillish": {"number": 583, "type": ["ice"]},
    "vanilluxe": {"number": 584, "type": ["ice"]},

    "deerling": {"number": 585, "type": ["normal", "grass"]},
    "sawsbuck": {"number": 586, "type": ["normal", "grass"]},

    "emolga": {"number": 587, "type": ["electric", "flying"]},

    "karrablast": {"number": 588, "type": ["bug"]},
    "escavalier": {"number": 589, "type": ["bug", "steel"]},

    "foongus": {"number": 590, "type": ["grass", "poison"]},
    "amoonguss": {"number": 591, "type": ["grass", "poison"]},

    "frillish": {"number": 592, "type": ["water", "ghost"]},
    "jellicent": {"number": 593, "type": ["water", "ghost"]},

    "alomomola": {"number": 594, "type": ["water"]},

    "joltik": {"number": 595, "type": ["bug", "electric"]},
    "galvantula": {"number": 596, "type": ["bug", "electric"]},

    "ferroseed": {"number": 597, "type": ["grass", "steel"]},
    "ferrothorn": {"number": 598, "type": ["grass", "steel"]},

    "klink": {"number": 599, "type": ["steel"]},
    "klang": {"number": 600, "type": ["steel"]},
    "klinklang": {"number": 601, "type": ["steel"]},

    "tynamo": {"number": 602, "type": ["electric"]},
    "eelektrik": {"number": 603, "type": ["electric"]},
    "eelektross": {"number": 604, "type": ["electric"]},

    "elgyem": {"number": 605, "type": ["psychic"]},
    "beheeyem": {"number": 606, "type": ["psychic"]},

    "litwick": {"number": 607, "type": ["ghost", "fire"]},
    "lampent": {"number": 608, "type": ["ghost", "fire"]},
    "chandelure": {"number": 609, "type": ["ghost", "fire"]},

    "axew": {"number": 610, "type": ["dragon"]},
    "fraxure": {"number": 611, "type": ["dragon"]},
    "haxorus": {"number": 612, "type": ["dragon"]},

    "cubchoo": {"number": 613, "type": ["ice"]},
    "beartic": {"number": 614, "type": ["ice"]},

    "cryogonal": {"number": 615, "type": ["ice"]},

    "shelmet": {"number": 616, "type": ["bug"]},
    "accelgor": {"number": 617, "type": ["bug"]},

    "stunfisk": {"number": 618, "type": ["ground", "electric"]},

    "mienfoo": {"number": 619, "type": ["fighting"]},
    "mienshao": {"number": 620, "type": ["fighting"]},

    "druddigon": {"number": 621, "type": ["dragon"]},

    "golett": {"number": 622, "type": ["ground", "ghost"]},
    "golurk": {"number": 623, "type": ["ground", "ghost"]},

    "pawniard": {"number": 624, "type": ["dark", "steel"]},
    "bisharp": {"number": 625, "type": ["dark", "steel"]},

    "bouffalant": {"number": 626, "type": ["normal"]},

    "rufflet": {"number": 627, "type": ["normal", "flying"]},
    "braviary": {"number": 628, "type": ["normal", "flying"]},

    "vullaby": {"number": 629, "type": ["dark", "flying"]},
    "mandibuzz": {"number": 630, "type": ["dark", "flying"]},

    "heatmor": {"number": 631, "type": ["fire"]},

    "durant": {"number": 632, "type": ["bug", "steel"]},

    "deino": {"number": 633, "type": ["dark", "dragon"]},
    "zweilous": {"number": 634, "type": ["dark", "dragon"]},
    "hydreigon": {"number": 635, "type": ["dark", "dragon"]},

    "larvesta": {"number": 636, "type": ["bug", "fire"]},
    "volcarona": {"number": 637, "type": ["bug", "fire"]},

    "cobalion": {"number": 638, "type": ["steel", "fighting"]},
    "terrakion": {"number": 639, "type": ["rock", "fighting"]},
    "virizion": {"number": 640, "type": ["grass", "fighting"]},

    "tornadus": {"number": 641, "type": ["flying"]},
    "thundurus": {"number": 642, "type": ["electric", "flying"]},
    "reshiram": {"number": 643, "type": ["dragon", "fire"]},
    "zekrom": {"number": 644, "type": ["dragon", "electric"]},

    "landorus": {"number": 645, "type": ["ground", "flying"]},

    "kyurem": {"number": 646, "type": ["dragon", "ice"]},

    "keldeo": {"number": 647, "type": ["water", "fighting"]},

    "meloetta": {"number": 648, "type": ["normal", "psychic"]},

    "genesect": {"number": 649, "type": ["bug", "steel"]},

    "chespin": {"number": 650, "type": ["grass"]},
    "quilladin": {"number": 651, "type": ["grass"]},
    "chesnaught": {"number": 652, "type": ["grass", "fighting"]},

    "fennekin": {"number": 653, "type": ["fire"]},
    "braixen": {"number": 654, "type": ["fire"]},
    "delphox": {"number": 655, "type": ["fire", "psychic"]},

    "froakie": {"number": 656, "type": ["water"]},
    "frogadier": {"number": 657, "type": ["water"]},
    "greninja": {"number": 658, "type": ["water", "dark"]},

    "bunnelby": {"number": 659, "type": ["normal"]},
    "diggersby": {"number": 660, "type": ["normal", "ground"]},

    "fletchling": {"number": 661, "type": ["normal", "flying"]},
    "fletchinder": {"number": 662, "type": ["fire", "flying"]},
    "talonflame": {"number": 663, "type": ["fire", "flying"]},

    "scatterbug": {"number": 664, "type": ["bug"]},
    "spewpa": {"number": 665, "type": ["bug"]},
    "vivillon": {"number": 666, "type": ["bug", "flying"]},

    "litleo": {"number": 667, "type": ["fire", "normal"]},
    "pyroar": {"number": 668, "type": ["fire", "normal"]},

    "flabebe": {"number": 669, "type": ["fairy"]},
    "floette": {"number": 670, "type": ["fairy"]},
    "florges": {"number": 671, "type": ["fairy"]},

    "skiddo": {"number": 672, "type": ["grass"]},
    "gogoat": {"number": 673, "type": ["grass"]},

    "pancham": {"number": 674, "type": ["fighting"]},
    "pangoro": {"number": 675, "type": ["fighting", "dark"]},

    "furfrou": {"number": 676, "type": ["normal"]},

    "espurr": {"number": 677, "type": ["psychic"]},
    "meowstic": {"number": 678, "type": ["psychic"]},

    "honedge": {"number": 679, "type": ["steel", "ghost"]},
    "doublade": {"number": 680, "type": ["steel", "ghost"]},
    "aegislash": {"number": 681, "type": ["steel", "ghost"]},

    "spritzee": {"number": 682, "type": ["fairy"]},
    "aromatisse": {"number": 683, "type": ["fairy"]},

    "swirlix": {"number": 684, "type": ["fairy"]},
    "slurpuff": {"number": 685, "type": ["fairy"]},

    "inkay": {"number": 686, "type": ["dark", "psychic"]},
    "malamar": {"number": 687, "type": ["dark", "psychic"]},

    "binacle": {"number": 688, "type": ["rock", "water"]},
    "barbaracle": {"number": 689, "type": ["rock", "water"]},

    "skrelp": {"number": 690, "type": ["poison", "water"]},
    "dragalge": {"number": 691, "type": ["poison", "dragon"]},

    "clauncher": {"number": 692, "type": ["water"]},
    "clawitzer": {"number": 693, "type": ["water"]},

    "helioptile": {"number": 694, "type": ["electric", "normal"]},
    "heliolisk": {"number": 695, "type": ["electric", "normal"]},

    "tyrunt": {"number": 696, "type": ["rock", "dragon"]},
    "tyrantrum": {"number": 697, "type": ["rock", "dragon"]},

    "amaura": {"number": 698, "type": ["rock", "ice"]},
    "aurorus": {"number": 699, "type": ["rock", "ice"]},

    "sylveon": {"number": 700, "type": ["fairy"]},

    "hawlucha": {"number": 701, "type": ["fighting", "flying"]},

    "dedenne": {"number": 702, "type": ["electric", "fairy"]},

    "carbink": {"number": 703, "type": ["rock", "fairy"]},

    "goomy": {"number": 704, "type": ["dragon"]},
    "sliggoo": {"number": 705, "type": ["dragon"]},
    "goodra": {"number": 706, "type": ["dragon"]},

    "klefki": {"number": 707, "type": ["steel", "fairy"]},

    "phantump": {"number": 708, "type": ["ghost", "grass"]},
    "trevenant": {"number": 709, "type": ["ghost", "grass"]},

    "pumpkaboo": {"number": 710, "type": ["ghost", "grass"]},
    "gourgeist": {"number": 711, "type": ["ghost", "grass"]},

    "bergmite": {"number": 712, "type": ["ice"]},
    "avalugg": {"number": 713, "type": ["ice"]},

    "noibat": {"number": 714, "type": ["flying", "dragon"]},
    "noivern": {"number": 715, "type": ["flying", "dragon"]},

    "xerneas": {"number": 716, "type": ["fairy"]},
    "yveltal": {"number": 717, "type": ["dark", "flying"]},
    "zygarde": {"number": 718, "type": ["dragon", "ground"]},

    "diancie": {"number": 719, "type": ["rock", "fairy"]},
    "hoopa": {"number": 720, "type": ["psychic", "ghost"]},
    "volcanion": {"number": 721, "type": ["fire", "water"]},

    "rowlet": {"number": 722, "type": ["grass", "flying"]},
    "dartrix": {"number": 723, "type": ["grass", "flying"]},
    "decidueye": {"number": 724, "type": ["grass", "ghost"], "z_move": "sinister arrow raid"},

    "litten": {"number": 725, "type": ["fire"]},
    "torracat": {"number": 726, "type": ["fire"]},
    "incineroar": {"number": 727, "type": ["fire", "dark"], "z_move": "malicious moonsault"},

    "popplio": {"number": 728, "type": ["water"]},
    "brionne": {"number": 729, "type": ["water"]},
    "primarina": {"number": 730, "type": ["water", "fairy"], "z_move": "oceanic operetta"},

    "pikipek": {"number": 731, "type": ["normal", "flying"]},
    "trumbeak": {"number": 732, "type": ["normal", "flying"]},
    "toucannon": {"number": 733, "type": ["normal", "flying"]},

    "yungoos": {"number": 734, "type": ["normal"]},
    "gumshoos": {"number": 735, "type": ["normal"]},

    "grubbin": {"number": 736, "type": ["bug"]},
    "charjabug": {"number": 737, "type": ["bug", "electric"]},
    "vikavolt": {"number": 738, "type": ["bug", "electric"]},

    "crabrawler": {"number": 739, "type": ["fighting"]},
    "crabominable": {"number": 740, "type": ["fighting", "ice"]},

    "oricorio": {"number": 741, "type": ["fire", "flying"]},

    "cutiefly": {"number": 742, "type": ["bug", "fairy"]},
    "ribombee": {"number": 743, "type": ["bug", "fairy"]},

    "rockruff": {"number": 744, "type": ["rock"]},
    "lycanroc": {"number": 745, "type": ["rock"], "z_move": "splintered stormshards"},

    "wishiwashi": {"number": 746, "type": ["water"]},

    "mareanie": {"number": 747, "type": ["poison", "water"]},
    "toxapex": {"number": 748, "type": ["poison", "water"]},

    "mudbray": {"number": 749, "type": ["ground"]},
    "mudsdale": {"number": 750, "type": ["ground"]},

    "dewpider": {"number": 751, "type": ["water", "bug"]},
    "araquanid": {"number": 752, "type": ["water", "bug"]},

    "fomantis": {"number": 753, "type": ["grass"]},
    "lurantis": {"number": 754, "type": ["grass"]},

    "morelull": {"number": 755, "type": ["grass", "fairy"]},
    "shiinotic": {"number": 756, "type": ["grass", "fairy"]},

    "salandit": {"number": 757, "type": ["poison", "fire"]},
    "salazzle": {"number": 758, "type": ["poison", "fire"]},

    "stufful": {"number": 759, "type": ["normal", "fighting"]},
    "bewear": {"number": 760, "type": ["normal", "fighting"]},

    "bounsweet": {"number": 761, "type": ["grass"]},
    "steenee": {"number": 762, "type": ["grass"]},
    "tsareena": {"number": 763, "type": ["grass"]},

    "comfey": {"number": 764, "type": ["fairy"]},

    "oranguru": {"number": 765, "type": ["normal", "psychic"]},
    "passimian": {"number": 766, "type": ["fighting"]},

    "wimpod": {"number": 767, "type": ["bug", "water"]},
    "golisopod": {"number": 768, "type": ["bug", "water"]},

    "sandygast": {"number": 769, "type": ["ghost", "ground"]},
    "palossand": {"number": 770, "type": ["ghost", "ground"]},

    "pyukumuku": {"number": 771, "type": ["water"]},

    "type_null": {"number": 772, "type": ["normal"]},
    "silvally": {"number": 773, "type": ["normal"]},

    "minior": {"number": 774, "type": ["rock", "flying"]},

    "komala": {"number": 775, "type": ["normal"]},

    "turtonator": {"number": 776, "type": ["fire", "dragon"]},

    "togedemaru": {"number": 777, "type": ["electric", "steel"]},

    "mimikyu": {"number": 778, "type": ["ghost", "fairy"], "z_move": "let’s snuggle forever"},

    "bruxish": {"number": 779, "type": ["water", "psychic"]},

    "drampa": {"number": 780, "type": ["normal", "dragon"]},

    "dhelmise": {"number": 781, "type": ["ghost", "grass"]},

    "jangmo_o": {"number": 782, "type": ["dragon"]},
    "hakamo_o": {"number": 783, "type": ["dragon", "fighting"]},
    "kommo_o": {"number": 784, "type": ["dragon", "fighting"], "z_move": "clangorous soulblaze"},

    "tapu_koko": {"number": 785, "type": ["electric", "fairy"], "z_move": "guardian of alola"},
    "tapu_lele": {"number": 786, "type": ["psychic", "fairy"], "z_move": "guardian of alola"},
    "tapu_bulu": {"number": 787, "type": ["grass", "fairy"], "z_move": "guardian of alola"},
    "tapu_fini": {"number": 788, "type": ["water", "fairy"], "z_move": "guardian of alola"},

    "cosmog": {"number": 789, "type": ["psychic"]},
    "cosmoem": {"number": 790, "type": ["psychic"]},
    "solgaleo": {"number": 791, "type": ["psychic", "steel"], "z_move": "searing sunraze smash"},
    "lunala": {"number": 792, "type": ["psychic", "ghost"], "z_move": "menacing moonraze maelstrom"},

    "nihilego": {"number": 793, "type": ["rock", "poison"]},
    "buzzwole": {"number": 794, "type": ["bug", "fighting"]},
    "pheromosa": {"number": 795, "type": ["bug", "fighting"]},
    "xurkitree": {"number": 796, "type": ["electric"]},
    "celesteela": {"number": 797, "type": ["steel", "flying"]},
    "kartana": {"number": 798, "type": ["grass", "steel"]},
    "guzzlord": {"number": 799, "type": ["dark", "dragon"]},

    "necrozma": {"number": 800, "type": ["psychic"]},
    "ultra_necrozma": {"number": 800, "type": ["psychic", "dragon"], "z_move": "light that burns the sky"},

    "magearna": {"number": 801, "type": ["steel", "fairy"]},

    "marshadow": {"number": 802, "type": ["fighting", "ghost"], "z_move": "soul-stealing 7-star strike"},

    "poipole": {"number": 803, "type": ["poison"]},
    "naganadel": {"number": 804, "type": ["poison", "dragon"]},

    "stakataka": {"number": 805, "type": ["rock", "steel"]},
    "blacephalon": {"number": 806, "type": ["fire", "ghost"]},

    "zeraora": {"number": 807, "type": ["electric"]},

    "meltan": {"number": 808, "type": ["steel"]},
    "melmetal": {"number": 809, "type": ["steel"]},

    "grookey": {"number": 810, "type": ["grass"]},
    "thwackey": {"number": 811, "type": ["grass"]},
    "rillaboom": {"number": 812, "type": ["grass"]},

    "scorbunny": {"number": 813, "type": ["fire"]},
    "raboot": {"number": 814, "type": ["fire"]},
    "cinderace": {"number": 815, "type": ["fire"]},

    "sobble": {"number": 816, "type": ["water"]},
    "drizzile": {"number": 817, "type": ["water"]},
    "inteleon": {"number": 818, "type": ["water"]},

    "skwovet": {"number": 819, "type": ["normal"]},
    "greedent": {"number": 820, "type": ["normal"]},

    "rookidee": {"number": 821, "type": ["flying"]},
    "corvisquire": {"number": 822, "type": ["flying"]},
    "corviknight": {"number": 823, "type": ["flying", "steel"]},

    "blipbug": {"number": 824, "type": ["bug"]},
    "dottler": {"number": 825, "type": ["bug", "psychic"]},
    "orbeetle": {"number": 826, "type": ["bug", "psychic"]},

    "nickit": {"number": 827, "type": ["dark"]},
    "thievul": {"number": 828, "type": ["dark"]},

    "gossifleur": {"number": 829, "type": ["grass"]},
    "eldegoss": {"number": 830, "type": ["grass"]},

    "wooloo": {"number": 831, "type": ["normal"]},
    "dubwool": {"number": 832, "type": ["normal"]},

    "chewtle": {"number": 833, "type": ["water"]},
    "drednaw": {"number": 834, "type": ["water", "rock"]},

    "yamper": {"number": 835, "type": ["electric"]},
    "boltund": {"number": 836, "type": ["electric"]},

    "rolycoly": {"number": 837, "type": ["rock"]},
    "carkol": {"number": 838, "type": ["rock", "fire"]},
    "coalossal": {"number": 839, "type": ["rock", "fire"]},

    "applin": {"number": 840, "type": ["grass", "dragon"]},
    "flapple": {"number": 841, "type": ["grass", "dragon"]},
    "appletun": {"number": 842, "type": ["grass", "dragon"]},

    "silicobra": {"number": 843, "type": ["ground"]},
    "sandaconda": {"number": 844, "type": ["ground"]},

    "cramorant": {"number": 845, "type": ["flying", "water"]},

    "arrokuda": {"number": 846, "type": ["water"]},
    "barraskewda": {"number": 847, "type": ["water"]},

    "toxel": {"number": 848, "type": ["electric", "poison"]},
    "toxtricity": {"number": 849, "type": ["electric", "poison"]},

    "sizzlipede": {"number": 850, "type": ["fire", "bug"]},
    "centiskorch": {"number": 851, "type": ["fire", "bug"]},

    "clobbopus": {"number": 852, "type": ["fighting"]},
    "grapploct": {"number": 853, "type": ["fighting"]},

    "sinistea": {"number": 854, "type": ["ghost"]},
    "polteageist": {"number": 855, "type": ["ghost"]},

    "hatenna": {"number": 856, "type": ["psychic"]},
    "hattrem": {"number": 857, "type": ["psychic"]},
    "hatterene": {"number": 858, "type": ["psychic", "fairy"]},

    "impidimp": {"number": 859, "type": ["dark", "fairy"]},
    "morgrem": {"number": 860, "type": ["dark", "fairy"]},
    "grimmsnarl": {"number": 861, "type": ["dark", "fairy"]},

    "obstagoon": {"number": 862, "type": ["dark", "normal"]},

    "perrserker": {"number": 863, "type": ["steel"]},

    "cursola": {"number": 864, "type": ["ghost"]},

    "sirfetchd": {"number": 865, "type": ["fighting"]},

    "mr_rime": {"number": 866, "type": ["ice", "psychic"]},

    "runerigus": {"number": 867, "type": ["ground", "ghost"]},

    "milcery": {"number": 868, "type": ["fairy"]},
    "alcremie": {"number": 869, "type": ["fairy"]},

    "falinks": {"number": 870, "type": ["fighting"]},

    "pincurchin": {"number": 871, "type": ["electric"]},

    "snom": {"number": 872, "type": ["ice", "bug"]},
    "frosmoth": {"number": 873, "type": ["ice", "bug"]},

    "stonjourner": {"number": 874, "type": ["rock"]},

    "eiscue": {"number": 875, "type": ["ice"]},

    "indeedee": {"number": 876, "type": ["psychic", "normal"]},

    "morpeko": {"number": 877, "type": ["electric", "dark"]},

    "cufant": {"number": 878, "type": ["steel"]},
    "copperajah": {"number": 879, "type": ["steel"]},

    "dracozolt": {"number": 880, "type": ["electric", "dragon"]},
    "arctozolt": {"number": 881, "type": ["electric", "ice"]},
    "dracovish": {"number": 882, "type": ["water", "dragon"]},
    "arctovish": {"number": 883, "type": ["water", "ice"]},

    "duraludon": {"number": 884, "type": ["steel", "dragon"]},

    "dreepy": {"number": 885, "type": ["dragon", "ghost"]},
    "drakloak": {"number": 886, "type": ["dragon", "ghost"]},
    "dragapult": {"number": 887, "type": ["dragon", "ghost"]},

    "zacian": {"number": 888, "type": ["fairy"]},
    "zamazenta": {"number": 889, "type": ["fighting"]},

    "eternatus": {"number": 890, "type": ["poison", "dragon"]},

    "kubfu": {"number": 891, "type": ["fighting"]},
    "urshifu": {"number": 892, "type": ["fighting", "dark"]},

    "zarude": {"number": 893, "type": ["dark", "grass"]},

    "regieleki": {"number": 894, "type": ["electric"]},
    "regidrago": {"number": 895, "type": ["dragon"]},

    "glastrier": {"number": 896, "type": ["ice"]},
    "spectrier": {"number": 897, "type": ["ghost"]},

    "calyrex": {"number": 898, "type": ["psychic", "grass"]},

    "sprigatito": {"number": 906, "type": ["grass"]},
    "floragato": {"number": 907, "type": ["grass"]},
    "meowscarada": {"number": 908, "type": ["grass", "dark"]},

    "fuecoco": {"number": 909, "type": ["fire"]},
    "crocalor": {"number": 910, "type": ["fire"]},
    "skeledirge": {"number": 911, "type": ["fire", "ghost"]},

    "quaxly": {"number": 912, "type": ["water"]},
    "quaxwell": {"number": 913, "type": ["water"]},
    "quaquaval": {"number": 914, "type": ["water", "fighting"]},

    "lechonk": {"number": 915, "type": ["normal"]},
    "oinkologne": {"number": 916, "type": ["normal"]},

    "tarountula": {"number": 917, "type": ["bug"]},
    "spidops": {"number": 918, "type": ["bug"]},

    "nymble": {"number": 919, "type": ["bug"]},
    "lokix": {"number": 920, "type": ["bug", "dark"]},

    "pawmi": {"number": 921, "type": ["electric"]},
    "pawmo": {"number": 922, "type": ["electric", "fighting"]},
    "pawmot": {"number": 923, "type": ["electric", "fighting"]},

    "tandemaus": {"number": 924, "type": ["normal"]},
    "maushold": {"number": 925, "type": ["normal"]},

    "fidough": {"number": 926, "type": ["fairy"]},
    "dachsbun": {"number": 927, "type": ["fairy"]},

    "smoliv": {"number": 928, "type": ["grass", "normal"]},
    "dolliv": {"number": 929, "type": ["grass", "normal"]},
    "arboliva": {"number": 930, "type": ["grass", "normal"]},

    "squawkabilly": {"number": 931, "type": ["normal", "flying"]},

    "nacli": {"number": 932, "type": ["rock"]},
    "naclstack": {"number": 933, "type": ["rock"]},
    "garganacl": {"number": 934, "type": ["rock"]},

    "charcadet": {"number": 935, "type": ["fire"]},
    "armarouge": {"number": 936, "type": ["fire", "psychic"]},
    "ceruledge": {"number": 937, "type": ["fire", "ghost"]},

    "tadbulb": {"number": 938, "type": ["electric"]},
    "bellibolt": {"number": 939, "type": ["electric"]},

    "wattrel": {"number": 940, "type": ["electric", "flying"]},
    "kilowattrel": {"number": 941, "type": ["electric", "flying"]},

    "maschiff": {"number": 942, "type": ["dark"]},
    "mabosstiff": {"number": 943, "type": ["dark"]},

    "shroodle": {"number": 944, "type": ["poison", "normal"]},
    "grafaiai": {"number": 945, "type": ["poison", "normal"]},

    "bramblin": {"number": 946, "type": ["grass", "ghost"]},
    "brambleghast": {"number": 947, "type": ["grass", "ghost"]},

    "toedscool": {"number": 948, "type": ["ground", "grass"]},
    "toedscruel": {"number": 949, "type": ["ground", "grass"]},

    "klawf": {"number": 950, "type": ["rock"]},

    "capsakid": {"number": 951, "type": ["grass"]},
    "scovillain": {"number": 952, "type": ["grass", "fire"]},

    "rellor": {"number": 953, "type": ["bug"]},
    "rabsca": {"number": 954, "type": ["bug", "psychic"]},

    "flittle": {"number": 955, "type": ["psychic"]},
    "espathra": {"number": 956, "type": ["psychic"]},

    "tinkatink": {"number": 957, "type": ["fairy", "steel"]},
    "tinkatuff": {"number": 958, "type": ["fairy", "steel"]},
    "tinkaton": {"number": 959, "type": ["fairy", "steel"]},

    "wiglett": {"number": 960, "type": ["water"]},
    "wugtrio": {"number": 961, "type": ["water"]},

    "bombirdier": {"number": 962, "type": ["flying", "dark"]},

    "finizen": {"number": 963, "type": ["water"]},
    "palafin": {"number": 964, "type": ["water"]},

    "varoom": {"number": 965, "type": ["steel", "poison"]},
    "revavroom": {"number": 966, "type": ["steel", "poison"]},

    "cyclizar": {"number": 967, "type": ["dragon", "normal"]},

    "orthworm": {"number": 968, "type": ["steel"]},

    "glimmet": {"number": 969, "type": ["rock", "poison"]},
    "glimmora": {"number": 970, "type": ["rock", "poison"]},

    "greavard": {"number": 971, "type": ["ghost"]},
    "houndstone": {"number": 972, "type": ["ghost"]},

    "flamigo": {"number": 973, "type": ["flying", "fighting"]},

    "cetoddle": {"number": 974, "type": ["ice"]},
    "cetitan": {"number": 975, "type": ["ice"]},

    "veluza": {"number": 976, "type": ["water", "psychic"]},

    "dondozo": {"number": 977, "type": ["water"]},
    "tatsugiri": {"number": 978, "type": ["dragon", "water"]},

    "annihilape": {"number": 979, "type": ["fighting", "ghost"]},

    "clodsire": {"number": 980, "type": ["poison", "ground"]},

    "farigiraf": {"number": 981, "type": ["normal", "psychic"]},

    "dudunsparce": {"number": 982, "type": ["normal"]},

    "kingambit": {"number": 983, "type": ["dark", "steel"]},

    "great_tusk": {"number": 984, "type": ["ground", "fighting"]},
    "scream_tail": {"number": 985, "type": ["fairy", "psychic"]},
    "brute_bonnet": {"number": 986, "type": ["grass", "dark"]},
    "flutter_mane": {"number": 987, "type": ["ghost", "fairy"]},
    "slither_wing": {"number": 988, "type": ["bug", "fighting"]},
    "sandy_shocks": {"number": 989, "type": ["electric", "ground"]},

    "iron_treads": {"number": 990, "type": ["ground", "steel"]},
    "iron_bundle": {"number": 991, "type": ["ice", "water"]},
    "iron_hands": {"number": 992, "type": ["fighting", "electric"]},
    "iron_jugulis": {"number": 993, "type": ["dark", "flying"]},
    "iron_moth": {"number": 994, "type": ["fire", "poison"]},
    "iron_thorns": {"number": 995, "type": ["rock", "electric"]},

    "frigibax": {"number": 996, "type": ["dragon", "ice"]},
    "arctibax": {"number": 997, "type": ["dragon", "ice"]},
    "baxcalibur": {"number": 998, "type": ["dragon", "ice"]},

    "gimmighoul": {"number": 999, "type": ["ghost"]},
    "gholdengo": {"number": 1000, "type": ["steel", "ghost"]},

    "wo_chien": {"number": 1001, "type": ["dark", "grass"]},
    "chien_pao": {"number": 1002, "type": ["dark", "ice"]},
    "ting_lu": {"number": 1003, "type": ["dark", "ground"]},
    "chi_yu": {"number": 1004, "type": ["dark", "fire"]},

    "roaring_moon": {"number": 1005, "type": ["dragon", "dark"]},
    "iron_valiant": {"number": 1006, "type": ["fairy", "fighting"]},

    "koraidon": {"number": 1007, "type": ["fighting", "dragon"]},
    "miraidon": {"number": 1008, "type": ["electric", "dragon"]},

    "walking_wake": {"number": 1009, "type": ["water", "dragon"]},
    "iron_leaves": {"number": 1010, "type": ["grass", "psychic"]},

    "dipplin": {"number": 1011, "type": ["grass", "dragon"]},
    "poltchageist": {"number": 1012, "type": ["grass", "ghost"]},
    "sinistcha": {"number": 1013, "type": ["grass", "ghost"]},

    "okidogi": {"number": 1014, "type": ["poison", "fighting"]},
    "munkidori": {"number": 1015, "type": ["poison", "psychic"]},
    "fezandipiti": {"number": 1016, "type": ["poison", "fairy"]},

    "ogerpon": {"number": 1017, "type": ["grass"]},

    "archaludon": {"number": 1018, "type": ["steel", "dragon"]},
    "hydrapple": {"number": 1019, "type": ["grass", "dragon"]},
    "gouging_fire": {"number": 1020, "type": ["fire", "dragon"]},
    "raging_bolt": {"number": 1021, "type": ["electric", "dragon"]},
    "iron_boulder": {"number": 1022, "type": ["rock", "psychic"]},
    "iron_crown": {"number": 1023, "type": ["steel", "psychic"]},

    "terapagos": {"number": 1024, "type": ["normal"]},
    "pecharunt": {"number": 1025, "type": ["poison", "ghost"]}

}