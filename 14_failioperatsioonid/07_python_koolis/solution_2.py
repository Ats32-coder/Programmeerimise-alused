"""
Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette rea järjekorranumbri ja iga rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse.
"""
content = """Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin."""


def write_poem_file(filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def rows_and_numbers(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            clean_line = line.strip()
            print(f"{i}. {clean_line} ({len(clean_line)})")


if __name__ == '__main__':
    file_name = "luuletus.txt"
    write_poem_file(file_name)
    rows_and_numbers(file_name)