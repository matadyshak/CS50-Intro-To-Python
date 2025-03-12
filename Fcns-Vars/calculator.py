def main():
    x = int(input("What is X? "))
    print("X squared is", square(x))

def square(n):
    return pow(n, 2)


main()