with open("rosalind_rna.txt", 'r') as f:
    data = f.read()
    data = data.replace("T", "U")

with open("rosalind_rna.txt", 'w') as f:
    f.write(data)