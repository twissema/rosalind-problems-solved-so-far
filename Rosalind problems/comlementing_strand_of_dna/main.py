
if __name__ == '__main__':
    with open("rosalind_revc.txt", 'r') as f:
        dna_strand = f.read()
        print(dna_strand)
        dna_list = ""

        for base in dna_strand:
            if base == 'A':
                dna_list += "T"
            elif base == 'T':
                dna_list += "A"
            elif base == 'G':
                dna_list += "C"
            elif base == 'C':
                dna_list += "G"

        print(dna_list)
        new_dna = "".join(dna_list[::-1])
        print(new_dna)
        with open("rosalind_revc.txt", 'w') as f:
            f.write(new_dna)
