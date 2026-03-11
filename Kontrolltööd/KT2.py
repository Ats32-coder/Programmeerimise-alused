"""
Koosta programm telefoniraamatu loomiseks.

1.       Peab saama sisestada nime ja telefoni numbrit

2.       Samal nimel võib olla ainult üks telefoni number

3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime

a.       Kui vastet pole, siis peab võimaldama lisamist

4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)

5.       Lisa funktsioon terve raamatu kuvamiseks
"""
file = "telefoniraamat.txt"
book = {}

"""Read file data"""
try:
    with open(file, "r", encoding="utf-8") as f:
        for row in f:
            if "-" in row:
                name, number = row.strip().split("-")
                book[name] = number
except FileNotFoundError:
    book = {}


def save():
    """Save the phonebook file"""
    with open(file, "w", encoding="utf-8") as f:
        for name, number in book.items():
            f.write(name + "-" + number + "\n")


def add():
    """Add new contact"""
    name = input("Sisesta nimi: ")
    if name in book:
        print("Sellel nimel on juba number.")
    else:
        number = input("Sisesta number: ")
        book[name] = number
        save()


def find_by_name():
    """Find the number based on the name"""
    name = input("Sisesta nimi: ")
    if name in book:
        print("Number:", book[name])
    else:
        print("Nime ei leitud.")
        choice = input("Kas lisada uus? (Y/N): ")
        if choice.upper() == "Y":
            number = input("Sisesta number: ")
            book[name] = number
            save()


def find_by_number():
    """Find name based on the number"""
    number = input("Sisesta number: ")
    for name, num in book.items():
        if num == number:
            print("Nimi:", name)
            return

    print("Numbrit ei leitud.")
    choice = input("Kas lisada uus kontakt? (Y/N): ")
    if choice.upper() == "Y":
        name = input("Sisesta nimi: ")
        if name in book:
            print("Sellel nimel on juba number.")
        else:
            book[name] = number
            save()


def show_all():
    """Shows the whole phonebook"""
    for name, number in book.items():
        print(name, "-", number)


def menu():
    """Menu"""
    while True:
        print("\n1 : Lisa uus kontakt")
        print("2 : Otsi nime järgi numbrit")
        print("3 : Otsi numbri järgi nime")
        print("4 : Kuva kõik kontaktid")
        print("5 : Lõpeta")

        choice = input("Vali menüüst (nr): ")

        if choice == "1":
            add()
        elif choice == "2":
            find_by_name()
        elif choice == "3":
            find_by_number()
        elif choice == "4":
            show_all()
        elif choice == "5":
            break

if __name__ == '__main__':
    menu()
