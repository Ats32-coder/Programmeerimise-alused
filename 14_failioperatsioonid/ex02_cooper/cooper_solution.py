"""
Ülesanne. Cooperi test
Cooper testis mõõdetakse, kui palju suudab inimene joosta 12 minutiga. On määratud erinevad hindenormid meestele ja naistele.
Koostada funktsioon, mis võtab argumentideks meetrite arvu ja jooksja soo ning tagastab:
•	Sõne „väga hea“, kui meetreid on meeste puhul vähemalt 2800 ja naiste puhul 2600 vähem
•	Sõne „nõrk“, kui meetreid on meeste puhul vähem kui 2000 ja naistel alla 1800
•	Sõne „rahuldav“ muudel juhtudel
•	Tulemused, mis jäävad alla „väga hea“, peavad lisaks teatama, mitu meetrit jäi järgmisest hindest puudu
Koostada programm, mis küsib kasutajalt:
•	failinime,
Programm peab:
•	lugema failist jooksutulemused (täisarvud) ja jooksjate sood (M või N);
•	funktsiooniga arvutama hinded ja väljastama need ekraanile
•	arvutama ja väljastama ekraanile sugude kaupa kõikide tulemuste täisarvuni ümardatud keskmised ning funktsiooni abil keskmised hinded.
Näide funktsiooni rakendamisest
# >>> hinda(1800,’N’)
’rahuldav, järgmisest hindest puudu 800 m’
# >>> hinda(1799,’N’)
’nõrk, järgmisest hindest puudu 1m’
# >>> hinda(2600,’N’)
’väga hea’
Näide programmi tööst
Faili cooper.txt sisu:
1900 N
1800 M
2700 M
2600 N
1400 M
3801 N
1500 N
1800 N

Programmi töö:
Sisestage failinimi: cooper.txt
N 1900 m, rahuldav, järgmisest hindest puudu 700 m
M 1800 m, nõrk, järgmisest hindest puudu 200 m
M 2700 m, rahuldav, järgmisest hindest puudu 100 m
N 2600 m, väga hea
M 1400 m, nõrk, järgmisest hindest puudu 600 m
N 3801 m, väga hea
N 1500 m, nõrk, järgmisest hindest puudu 300 m
N 1800 m, rahuldav, järgmisest hindest puudu 800 m
Keskmised:
M 1967 m, nõrk, järgmisest hindest puudu 33 m
N 2320 m, rahuldav, järgmisest hindest puudu 280 m
"""
def grades(meters, gender):
    if gender == "M":
            if meters >= 2800:
                return "väga hea"
            elif meters < 2000:
                missing = 2000 - meters
                return f"nõrk, järgmisest hindest puudu {missing} m"
            else:
                missing = 2800 - meters
                return f"rahuldav, järgmisest hindest puudu {missing} m"
    elif gender == "N":
            if meters >= 2600:
                return "väga hea"
            elif meters < 1800:
                missing = 1800 - meters
                return f"nõrk, järgmisest hindest puudu {missing} m"
            else:
                missing = 2600 - meters
                return f"rahuldav, järgmisest hindest puudu {missing} m"
    else:
        return "Tundmatu sugu"

def main():
    file_name = input("Sisestage failinimi: ")

    content = []

    with open(file_name, "r") as f:
        for rida in f:
            osad = rida.strip().split()
            if len(osad) == 2:
                meters = int(osad[0])
                gender = osad[1].upper()
                content.append((meters, gender))

    for meters, gender in content:
        result = grades(meters, gender)
        print(f"{gender} {meters} m, {result}")

    M = []
    N = []

    for meters, gender in content:
        if gender == "M":
            M.append(meters)
        elif gender == "N":
            N.append(meters)

    print("\nKeskmised:")

    if M:
        average_m = round(sum(M)/len(M))
        result_m = grades(average_m, "M")
        print(f"M {average_m} m, {result_m}")

    if N:
        average_n = round(sum(N)/len(N))
        result_n = grades(average_n, "N")
        print(f"N {average_n} m, {result_n}")

if __name__ == '__main__':
    main()
