"""
Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

1. Väljasta linnad eraldi ridadena.
2. Järjesta need tähestikulisse järjekorda.
3. Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
4. Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
5. Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna",
kus linnade arv leitakse vastava funktsiooni abil.
"""

capitols = ["Tallinn", "Riia", "Tirana",
            "Helsinki", "Rooma", "Belgrad",
            "Vilnius", "Sofia", "Oslo", "Stockholm"]

def print_list(elements: list) -> None:
    for element in elements:
        print(element, end=", ")
    print()

def sort_in_place(elements: list) -> None:
    elements.sort()

def add_capitols(capitols: list[str], amount: int) -> None:
    for i in range(amount):
        capitols.append(input(f"{i + 1}. Sisesta euroopa pealinn: "))

def print_list_numbered(elements: list):
    for index, element in enumerate(elements):
        print(f"{index + 1}. {element}")

def summarize(capitols: list[str]) -> None:
    print(f"Meie järjendis on {len(capitols)} Euroopa pealinna")

if __name__ == '__main__':
    print_list(capitols)
    sort_in_place(capitols)
    print_list(capitols)
    add_capitols(capitols, 2)
    sort_in_place(capitols)
    print_list(capitols)
    print_list_numbered(capitols)
    summarize(capitols)