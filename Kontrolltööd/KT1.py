"""
Küsi kasutaja vanust ja nime
"""

def name_and_age():
    name = input("Sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus: "))
    print(f"Sinu nimi on {name} ja sa oled {age}-aastane.")


"""
Tervita kasutajat nime pidi niimitu korda kui mitu aastat ta on täisealine olnud (Kordus)
"""

def user_greeting():
    name = input("Sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus: "))
    years = age - 18
    if age > 17:
        for i in range(years):
            print(f"Tere {name}!")
    else:
        print("Sa ei ole veel täisealine.")


"""
Kirjuta ekraanile nime lõpust 3 tähte.
"""

def last_symbols():
    name = input("Sisesta oma nimi: ")
    if len(name) > 2:
        print(name[-3:])
    else:
        print("Sinu nimi on lühem kui 3 tähte")


if __name__ == '__main__':
    name_and_age()
    user_greeting()
    last_symbols()