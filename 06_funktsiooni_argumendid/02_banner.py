"""
Erinevates poodides ja veebikauplustes võib kohata reklaame, mis kutsuvad inimesi ostlema. Reklaamimiseks kasutatakse näiteks bännereid, mis
soovitud reklaamlauset korduvalt kuvavad.

Esmalt koostada funktsioon banner, mis võtab argumendiks reklaamlause, mida soovitakse kuvada; tagastab reklaamlause, kus kõik tähed on suured tähed.
"""


def bannerize(slogan: str) -> str:
    return slogan.upper()


if __name__ == '__main__':
    repeat_count = int(input("Mitu korda soovid sloganit korrata? "))
    slogan = input("Milline on sinu slogan? ")
    banner_text = bannerize(slogan)
    print(f"{banner_text}\n" * repeat_count)