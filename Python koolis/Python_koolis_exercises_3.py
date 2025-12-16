"""
Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt 5
korda ja lisab ka tervituse järjekorranumber.
"""


if __name__ == '__main__':
    name = input("Sisesta oma nimi: ")
    for i in range(5):
        print(f"{i + 1}. Tere {name}!")



"""
Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta,
vaid vajutab lihtsalt sisestusklahvi. Proovige seda ülesannet lahendada nii while- kui for-tsükliga.
"""


def solve_using_for():
    total = 0
    for i in range(10):
        number = float(input(f"FOR Sisesta {i + 1}. arv: "))
        total += number
    print(f"Sisestatud arvude summa on {total}")


def solve_using_while():
    total = 0
    count = 0
    while count < 10:
        number = float(input(f"WHILE Sisesta {count + 1}. arv: "))
        total += number
        count += 1
    print(f"Sisestatud arvude summa on {total}")


def solve_infinite_sum():
    total = 0
    count = 0
    while True:
        text_input = input(f"INFINITE Sisesta {count + 1}. arv: ")
        if text_input == "":
            break
        number = float(text_input)
        total += number
        count += 1
    print(f"Sisestatud arvude summa on {total}")


if __name__ == '__main__':
    #solve_using_for()
    #solve_using_while()
    solve_infinite_sum()



