"""
Koosta programm, mis küsib kasutajalt rea, mille järele ta soovib failis luuletus.txt uut rida lisada ning seejärel lisab kasutaja poolt sisestatud rea nt:

Sisesta rida, mille järele soovid uut rida lisada:
>> Padja, teki viskan maha,
Sisesta rida, mida soovid lisada:
>> üles ärgata ma ei taha,
Tulemus failis luuletus.txt:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
üles ärgata ma ei taha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
"""
from solution_2 import write_poem_file

if __name__ == '__main__':
    file_name = "luuletus.txt"
    write_poem_file(file_name)

    poem_line = input("Sisesta rida, mille järele soovid uut rida lisada: ").strip()
    line_to_append = input("Sisesta rida, mida soovid lisada: ").strip()

    """1. Loe faili read mällu"""
    with open(file_name, "r", encoding="utf-8") as f:
        read_files = f.readlines()

    """2. käime läbi rida haaval ja võrdleme käesoleva rea teksti kasutaja sisestatud tekstiga
        kui kattub siis,
            jäta rea number meelde ja katkesta tsükkel
        kui ei leidnud sobivat rida siis,
            teata, et soovitud rida ei leitud ja lõpetame programmi"""
    index = -1
    for i in range(len(read_files)):
        if read_files[i].strip() == poem_line:
            index = i
            break
    if index == -1:
        print("Soovitud rida ei leitud.")
    else:

        """3. Lisa mälus olevasse järjendisse meelde jäetud kohale kasutaja lisatud tekst"""
        read_files.insert(index + 1, line_to_append + "\n")

        """4. Kirjuta faili ja prindi uus luuletus"""
        with open(file_name, "w", encoding="utf-8") as f:
            f.writelines(read_files)
        print("\nTulemus failis luuletus.txt:\n")
        print("".join(read_files))


