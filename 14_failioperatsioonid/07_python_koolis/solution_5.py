"""
Palindroomiks nimetatakse sõna (ka sõnaühendit), mis on nii vasakult paremale kui paremalt vasakule lugedes täpselt ühesugunem
(näit. "kook", "kuulilennuteetunneliluuk" jne).
Loo programm, mis trükib ekraanile välja kõik tekstifailis olevad sõnad, mis on palindroomid.
Alustekstiks võid kasutada suvalist teksti, kuid katsetada tasuks ka sõnaloenditega, kus iga sõna asub eraldi real
(näit. eesti keele sõnade algvormid e. lemmad veebilehelt http://www.eki.ee/tarkvara/wordlist/).
"""
def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def check_file_for_palindromes(fileName: str) -> None:
    with open(fileName, encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if word and is_palindrome(word.lower()):
                print(word)


if __name__ == '__main__':
    file_name = "lemmad2013.txt"
    print(f"failis {file_name} esinevad järgmised palindroomid: ")
    check_file_for_palindromes(file_name)