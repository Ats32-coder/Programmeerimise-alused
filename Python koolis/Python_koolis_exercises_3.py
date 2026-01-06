"""
Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt 5
korda ja lisab ka tervituse järjekorranumber.
"""


#if __name__ == '__main__':
    #name = input("Sisesta oma nimi: ")
    #for i in range(5):
       #print(f"{i + 1}. Tere {name}!")



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
    #solve_infinite_sum()

    """
    Koosta programm, mis aitab lastel treenida liitmist. Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust.
    Kui vastus on õige, kiitma kasutajat, kui aga vale, andma õige vastuse ja esitama uue tehte. Järjest esitatavate tehete hulk võib 
    olla programmis ette antud (näiteks 10), samuti võib olla ette antud piirid, kui suuri arve kasutajalt küsitakse (näiteks 1 kuni 50).
    Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast viimast tehet tulemuse. Näiteks:
Tere! Õpime arvutama. Esitan 10 liitmistehet, püüa vastata õigesti.
5 + 16 =
>> 21
Tubli, õige vastus!
18 + 23 =
>> 39
Sinu vastus polnud õige. Õige vastus on 41.
[...]
2 + 5 =
>> 7
Tubli, õige vastus!
See oli viimane ülesanne. Kogusid 10-st punktist 7.

Täiendusi vabal valikul:

    Programm lubab kasutajal alguses sisestada, mitut tehet soovitakse.
    Esitatavate arvude piirid saab kasutaja ette anda (maksimum või nii miinimum kui maksimum).
    Küsitakse mitte ainult liitmistehteid, vaid ka teisi (lahutamine, korrutamine, jagamine).
    Vastavalt lõpptulemusele reageeritakse erinevalt: "Ülihea!", "Olid tubli!", "Korralik keskmine tulemus!", "Püüad järgmisel korral rohkem." vms. 
    """

from random import randint, choice

operations = ["+", "-", "*", "**", "//"]

def get_calculation(min_value: int, max_value: int) -> tuple[str, int]:
    num1 = randint(min_value, max_value)
    num2 = randint(min_value, max_value)
    operation = choice(operations)
    if operation == "+":
        correct_answer = num1 + num2
        return f"{num1} {operation} {num2} = ", correct_answer
    elif operation == "-":
        correct_answer = num1 - num2
        return f"{num1} {operation} {num2} = ", correct_answer
    elif operation == "*":
        correct_answer = num1 * num2
        return f"{num1} {operation} {num2} = ", correct_answer
    elif operation == "**":
        correct_answer = num1 ** num2
        return f"{num1} {operation} {num2} = ", correct_answer
    elif operation == "//":
        correct_answer = num1 // num2
        return f"{num1} {operation} {num2} = ", correct_answer
    return "Tundmatu tehe", 0


def test_user_knowledge(min_value: int, max_value: int) -> tuple[bool, int]:
    calculation, correct_answer = get_calculation(min_value, max_value)
    user_answer = int(input(calculation))
    return user_answer == correct_answer, correct_answer


def practice_addition(count: int, min_value: int, max_value: int) -> None:
    correct_count = 0
    for i in range(count):
        print(f"Harjutus {i+1}/{count}-st")
        is_answer_correct, correct_answer = test_user_knowledge(min_value, max_value)
        if is_answer_correct:
            print("Tubli! Vastasid õigesti.")
            correct_count += 1
        else:
            print(f"Vale vastus. Õige vastus on {correct_answer}. Harjuta rohkem.")
    print(f"See oli viimane ülesanne. Kogusid {count}-st punktist {correct_count}.")


#if __name__ == '__main__':
    #count = int(input("Mitu korda soovid harjutada?"))
    #min_value = int(input("Milline peaks olema väikseim täisarv harjutuses?"))
    #max_value = int(input("Milline peaks olema suurim täisarv harjutuses?"))
    #practice_addition(count, min_value, max_value)

"""
Koosta mäng, kus saate ära arvata arvuti poolt mõeldud täisarvu ühest kahekümneni. nt: 
Mõtlesin ühele täisarvule 1-20ni. Mis arv see on?
>> 15
Liiga suur, proovi uuesti.
>> 7
Liiga väike, proovi uuesti.
>> 9
Liiga väike, proovi uuesti.
>> 11
Tubli, arvasid ära. Arv oli 11.
Enne ülesande lahendamist mõelge välja mängu algoritm ja koostage selle kohta plokkskeem. 
"""

from random import randint

def play_guessing_game():
    correct = randint(1, 20)
    tries = 0
    while tries < 5:
        answer = int(input(f"Katse {tries+1}. Sisesta arv vahemikus 1-20: "))
        tries += 1
        if answer > correct:
            print("Liiga suur, proovi uuesti")
            continue
        if answer < correct:
            print("Liiga väike, proovi uuesti")
            continue
        print(f"Tubli, arvasid ära. Arv oli {correct}")
        break
    else:
        print(f"Katsed said otsa. Mõtlesin arvule {correct}")

#if __name__ == '__main__':
    #play_guessing_game()


"""
Väljasta ekraanile kõikvõimalikud kombinatsioonid kujul "x - y - z", kus x, y ja z on mistahes täisarvud 1-st 20-ni (20 kaasaarvatud). 
Samuti loenda, mitu sellist kombinatsiooni leiti.
"""

count = 0
for x in range(20):
    for y in range(20):
        for z in range(20):
            print(f"{x + 1} - {y + 1} - {z + 1}")
            count += 1
print(f"Kokku leiti {count} kombinatsiooni.")


"""
Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN.
Seejärel muutke programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d,
"""

def draw_square(size: int, symbol: str, alt: str):
    for row in range(size):
        for col in range(size):
            #print(f"{symbol}", end=" ")
            if row == col or row + col == size - 1:
                print(f"{alt}", end=" ")
            else:
                print(f"{symbol}", end=" ")
        print()

if __name__ == '__main__':
    size = int(input("Kui suurt ruutu soovid? "))
    draw_square(size, "o", "x")
    draw_square(size * 2, "I", "-")







