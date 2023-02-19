for i in range(8):
    for j in range(30, 38):
        code = "\033[{};{}m".format(i, j)
        print("{} ({}, {})".format(code + "Sample Text" + "\033[0m", i, j), end=" ")
    print()