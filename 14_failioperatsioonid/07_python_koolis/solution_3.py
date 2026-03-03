"""
Tee programm, mis väljastab failist luuletus.txt kasutaja poolt soovitud rea nt:

Mitmendat rida soovid kuvada:
>> 7
Error tuleb ette siis,
NB! Faili avamiseks ja rea väljastamiseks koosta eraldi alamprogramm (ehk funktsioon).
"""
from solution_2 import write_poem_file

def print_line_from_file(lineNumber: int, fileName: str) -> None:
    message = f"Luuletuse {lineNumber}. rida: "
    with open(fileName, encoding="utf-8") as f:
        for index, line in enumerate(f):
            if (index + 1) == lineNumber:
                print(message + line)
                break
        else:
            print("Viga! Luuletuses pole nii palju ridu.")

if __name__ == '__main__':
    file_name = "luuletus.txt"
    write_poem_file(file_name)
    user_input = input("Mitmendat rida soovid kuvada: ")
    if user_input.isdigit():
        print_line_from_file(int(user_input), file_name)
    else:
        print("Viga! Sisesta positiivne täisarv.")