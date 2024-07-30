def offspring_calculation(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return offspring_calculation(n - 1, k) + k * offspring_calculation(n - 2, k)

with open("rosalind_fib.txt", 'r') as file:
    data = file.read()
    datalist = data.split()


    n = int(datalist[0])
    k = int(datalist[1])

    print(offspring_calculation(n, k))


