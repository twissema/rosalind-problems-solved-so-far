
if __name__ == "__main__":
    with open("rosalind_hamm.txt", 'r') as f:
        data = f.read().split("\n")
        counter = 0

        for i in range(data[0].__len__()):
            if data[0][i] != data[1][i]:
                counter+= 1
        print(counter)