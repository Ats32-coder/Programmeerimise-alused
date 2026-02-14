"""
Koosta programm, mis "viskab täringut" kolm korda ehk väljastab ekraanile 3 juhusliku täringuviske tulemused. Et ekraanipilt oleks realistlikum,
esita tulemused graafiliselt, selleks kasuta nn. ASCII graafikat (https://en.wikipedia.org/wiki/ASCII_art): imiteeri tekstisümbolite abil täringu külje kujutist. Täiendamiseks:

    Kasutaja võib alguses ise valida, mitu korda täringut visata.
    Mängida võib mitu inimest, programmi alguses küsitakse inimeste nimesid.
    Täringut imiteeritakse kolmemõõtmelisena.
"""
from random import randint


dice_ascii = [
"""┌─────────┐
│         │
│    ●    │
│         │
└─────────┘""",

"""┌─────────┐
│  ●      │
│         │
│      ●  │
└─────────┘""",

"""┌─────────┐
│  ●      │
│    ●    │
│      ●  │
└─────────┘""",

"""┌─────────┐
│  ●   ●  │
│         │
│  ●   ●  │
└─────────┘""",

"""┌─────────┐
│  ●   ●  │
│    ●    │
│  ●   ●  │
└─────────┘""",

"""┌─────────┐
│  ●   ●  │
│  ●   ●  │
│  ●   ●  │
└─────────┘"""
]


def throw_dice() -> tuple[int, str]:
    throw_result = randint(1,6)
    return throw_result, dice_ascii[throw_result-1]


def play_turn(throw_count, name="Player"):
    for i in range(throw_count):
        throw_result, dice_ascii = throw_dice()
        print(dice_ascii)
        print(f"{name} veeretas {throw_result}")


if __name__ == '__main__':
    throw_count = input("Mitut täringut soovid visata?")
    if throw_count.isdigit():
        throw_count = int(throw_count)
    else:
        throw_count = 3
    players_count = input("Mitu mängijat")
    if not players_count.isdigit():
        for i in range(throw_count):
            print(throw_dice()[1])
    else:
        players_count = int(players_count)
        player_names = []
        for i in range(players_count):
            player_names.append(input(f"Sisesta {i+1}. mängija nimi: "))
        game_cycle = 1
        while True:
            for name in player_names:
                play_turn(throw_count, name)
                input("Järgmise mängija kord. ENTER")
            print(f"{game_cycle}. vooru lõpp. Kas jätkata [Y/n]")
            game_cycle += 1
            if input() == "n":
                break