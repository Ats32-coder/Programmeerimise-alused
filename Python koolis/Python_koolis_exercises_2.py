"""
Ülesanne 1

Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.
"""
import math


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

#if __name__ == '__main__':
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


#if __name__ == '__main__':
    first = float(input("Sisestage esimene arv: "))
    second = float(input("Sisestage teine arv: "))
    op = input("Sisestage tehe: ")
    print(f"Tulemus: {dog_calculate(first, second, op)}")


    """
    Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja väljastab tulemuse Fahrenheiti kraadides.
    Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui teistpidi? Proovi. 
    """


def convert_to_fahrenheit(celsius_temperature: float) -> float:
    """Convert given Celsius temperature fo Fahrenheit"""
    return celsius_temperature * 1.8 + 32


def convert_to_celsius(fahrenheit_temperature: float) -> float:
    """Convert given Fahrenheit temperature to Celsius"""
    return (fahrenheit_temperature - 32) / 1.8


#if __name__ == '__main__':
    unit = input("Määra sisestatava temperatuuri ühik (C/F): ")
    if unit.upper() == "C":
        temperature_celsius = float(input("Sisesta temperatuur Celsiuse kraadides: "))
        temperature_fahrenheit = convert_to_fahrenheit(temperature_celsius)
        print(f"{temperature_celsius}C on {temperature_fahrenheit:.2f}F kraadi")
    elif unit.upper() == "F":
        temperature_fahrenheit = float(input("Sisesta temperatuur Fahrenheit kraadides: "))
        temperature_celsius = convert_to_celsius(temperature_fahrenheit)
        print(f"{temperature_fahrenheit}C on {temperature_celsius:.2f}F kraadi")
    else:
        print(f"Sisestatud tundmatu temperatuuri ühik - {unit}")
        print("Programm toetab C - Celsius ja F - Fahrenheit kraade")


"""Loo programm, mis küsib kasutajalt ruutvõrrandi liikmete (ruutliige, lineaarliige, vabaliige) kordajad ning arvutab 
nende põhjal diskriminandi ja väljastab selle põhjal ruutvõrrandi lahendid. Nagu tead, võib lahendeid vastavalt 
diskriminandi väärtusele olla üks või kaks, kuid lahendid võivad ka puududa.
"""


def calculate_discriminant(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c


def solve_quadratic_equation(a, b, discriminant, useAddition):
    if useAddition:
        top = -b + math.sqrt(discriminant)
    else:
        top = -b - math.sqrt(discriminant)
    bottom = 2 * a
    return top / bottom


if __name__ == '__main__':
    print("Arvutame ruutvõrrandit!")
    a = float(input("Sisesta ruutliige: "))
    if a == 0:
        print("Ruutliige ei tohi olla null.")
    else:
        b = float(input("Sisesta lineaarliige: "))
        c = float(input("Sisesta vabaliige: "))
        discriminant = calculate_discriminant(a, b, c)
        if discriminant < 0:
            print("Lahendid puuduvad")
        elif discriminant == 0:
            solution = solve_quadratic_equation(a, b, discriminant, True)
            print(f"Lahendid on võrdsed: {solution}")
        else:
            solution1 = solve_quadratic_equation(a, b, discriminant, True)
            solution2 = solve_quadratic_equation(a, b, discriminant, False)
            print(f"Lahendid on võrdsed: {solution1} ja {solution2}")










