with open('rosalind_dna_1_dataset.txt', 'r') as f:
    f = f.read()
    num_A = f.count('A')
    num_T = f.count('T')
    num_C = f.count('C')
    num_G = f.count('G')
    print(num_A, num_C, num_G, num_T)