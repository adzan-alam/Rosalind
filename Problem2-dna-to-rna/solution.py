import sys


def main():
    if len(sys.argv) != 2:
        raise ValueError(
            "The usage of this program is as follows: \n python program.py datapath.txt"
        )
    filename = sys.argv[1]
    with open(filename, "r", encoding="utf-8") as file:
        dna = file.read()
        dna = dna.strip()

    rna = transcribe_dna(dna)
    print(rna)


def transcribe_dna(dna):
    rna = dna.replace("T", "U")
    return rna


if __name__ == "__main__":
    main()
