"""
Juubelile on kutsutud hulk inimesi, kellest osa on teatanud, et nad tulevad ja ülejäänute kohta ei ole midagi teada.
Peo eelarve koosneb kahest osast: söök ja ruumi rent.
Söögi peale arvestatakse iga osaleja kohta 10 eurot. Ruumi rent maksab sõltumata osalejate arvust 55 eurot. Planeerimiseks on vaja programmi, mis arvutab
maksimaalse eelarve (arvestades, et kõik kutsutud inimesed tulevad kohale) ja minimaalse eelarve
(arvestades, et kohale tulevad ainult need, kes on juba seda teatanud).
"""


def calculate_budget(guests:int) -> int:
    """
    Calculate party budget
    
    Place costs $5 + 10 for each guest
    """
    place_price = 55
    price_per_guest = 10
    return place_price + price_per_guest * guests


if __name__ == '__main__':
    invited_guests = int(input("Mitu inimest on people kutsutud: "))
    confirmed_guests = int(input("Mitu inimest tuleb? "))
    min_budget = calculate_budget(confirmed_guests)
    max_budget = calculate_budget(invited_guests)
    print(f"Maksimaalne eelarve on {max_budget} eurot")