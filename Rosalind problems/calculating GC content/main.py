def cal_max_gc(fdict):
    new_dict = {}

    for key, value in fdict.items():
            gc_count = 0
            for i in fdict[key]:
                if i in ["G", "C"]:
                    gc_count += 1

            new_dict[key] = (gc_count/value.__len__())*100

    return f"{max(new_dict, key=new_dict.get)}\n{max(new_dict.values())}"

def main():
    fasta_dict = {}
    with open("rosalind_gc.txt", "r") as f:
        currentkey = ""
        filedata = f.readlines()

        for lines in filedata:
            if lines.startswith(">"):
                currentkey = lines.strip(">\n")
                fasta_dict[currentkey] = ""
            else:
                fasta_dict[currentkey] += lines.strip()

    #print(cal_max_gc(fasta_dict))
    print(fasta_dict)





if __name__ == "__main__":
    main()