def m(i):
    if i == 1:
        return 1/2
    return i / (i + 1) + m(i - 1)


for i in range(1, 21, 1):
    print("m({0}) = {1:.4f}".format(i, m(i)))

