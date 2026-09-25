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

    analysis = dna_analyse(dna)
    print(analysis)


def dna_analyse(dna):
    """
    Given functions takes DNA string as a input and return a f-string having no of each nucleotide and total dna content
    Args:
        dna (_type_): _description_
    """
    count = 0
    A = 0
    T = 0
    G = 0
    C = 0
    for nucleotide in dna:
        count += 1

        if nucleotide == "A":
            A += 1
        elif nucleotide == "T":
            T += 1
        elif nucleotide == "G":
            G += 1
        elif nucleotide == "C":
            C += 1
        else:
            raise ValueError(
                "Abnormal nucleotide detected : Nucleotide can only be A,T,G,C \n "
            )
    result = f"Total length of DNA : {count} Nucleotides.\n \nA Count  : {A} \nC Count  : {C} \nG Count  : {G} \nT Count  : {T} \n"
    return result


if __name__ == "__main__":
    main()
