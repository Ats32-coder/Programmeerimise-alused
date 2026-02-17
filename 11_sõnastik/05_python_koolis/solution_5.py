"""
Morsetähestik on koodikomplekt, kus igale tekstisümbolile vastab pikkadest ja lühikestest signaalidest koosnev kood (vt. https://et.wikipedia.org/wiki/Morse).
Ilmselt on kõigile teada appikutse "SOS" kood: "... --- ..." ehk kolm lühikest signaali ("S"), kolm pikka ("O") ja taas kolm lühikest.
Lühikesi signaale tähistatakse punktide, pikki aga kriipsudega.

Vajalik on sõnastik, kus on kirjas morse koodid (iga elemendi võtmeks tähistatav sümbol, väärtuseks koodi järjend punktidest ja kriipsudest).
Aja kokkuhoiu mõttes võid kasutada sellist rida:

tahestik = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..",
"j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}
Koosta programm, mis programmi käivitamisel tervitab kasutajat nii tavakeeles kui morse koodina, lubab seejärel kasutajal sisestada sõnu ning teisendab need sümbolhaaval morsetähestikku (lisades iga sümboli järele tühiku).
Sõnastik ei pruugi sisaldada kõikvõimalikke märke, seega tuleb iga sümboli puhul kontrollida, kas see üldse esineb sõnastikus. Tähe registrit ehk suur- ja väiketähti ei eristata.
Samuti tuleb otsustada, mida ette võtta nende tähtedega, mida inglise tähestikus pole (näiteks "õ", "ä" jne): ignoreerida või mõned neist teisendada (näiteks "õ" -> "o" vms).

Programm võiks küsida kasutajalt sõnu kas mingi arv kordi või töötada lõpmatult, kuni kasutaja sõna ei sisesta, vaid vajutab lihtsalt sisestusklahvile.
"""
morse_code = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..",
"j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...",
"t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}


def name_to_morse(name):
    result = []
    for char in name.lower():
        if char in morse_code:
            result.append(morse_code[char])
    return " ".join(result)


def name_and_greet():
    name = input("Sisesta oma nimi: ")

    print(f"Tere {name}")

    morse_name = name_to_morse(name)
    print(f"Sinu nimi morse koodis on {morse_name}")


if __name__ == '__main__':
    name_and_greet()