"""
Ülesanne 1

Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.
"""

def compute_rectangle():
    length = float(input("Sisesta ristküliku pikkus: "))
    width = float(input("Sisesta ristküliku laius: "))
    area = length * width
    circumference = 2 * (length + width)
    print(f"Antud ristküliku pindala on {area}")
    print(f"Antud ristküliku ümbermõõt on {circumference}")


"""
Ülesanne 2

Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile nimelise tervituse koos 
tekstiga, mis ütleb, kas tegemist on 7-18-aastase inimesega.
 """

def greet_by_name(name: str) -> str:
    return f"Tere {name}!"

def verify_age(age: int) -> str:
    if 7 <= age <= 18:
        return "Oled 7-18 aastane"
    else:
        return "Oled noorem või vanem kui 7-18 aastane"


    name = (input("Sisesta oma nimi: "))
    age = int(input("Sisesta oma vanus aastates täisarvuna: "))
    greeting = greet_by_name(name)
    age_text = verify_age(age)
    print(greeting, age_text, sep="\n")


    """
    Ülesanne 3

Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos vastusega. 

Näiteks:
Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5
"""

def calculate(num1: float, num2: float, operation: str) -> str:
    result = ""
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "//":
        result = num1 // num2
    elif operation == "**":
        result = num1 ** num2
    elif operation == "%":
        result = num1 % num2


    if result == "":
        return f"tundmatu tehe: {operation}"
    return f"{num1}{operation}{num2}={result}"


def dog_calculate(num1: float, num2: float, operation: str) -> str:
    result = ""
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "//":
        result = num1 // num2
    elif operation == "**":
        result = num1 ** num2
    elif operation == "%":
        result = num1 % num2


    if result == "":
        return f"URRRRRR GRRRR"
    return f"{round(result)*"auh "}"


if __name__ == '__main__':
    first = float(input("Sisestage esimene arv: "))
    second = float(input("Sisestage teine arv: "))
    op = input("Sisestage tehe: ")
    print(f"Tulemus: {dog_calculate(first, second, op)}")








