# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# git commit -m "Complete Assignment 5"
def single_table(number):
    print(f"\nMultiplication Table for {number}:")

    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


def all_tables(n):
    for number in range(1, n + 1):
        print(f"\nMultiplication Table for {number}:")

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

        print("---------------------------")


def main():

    # Part A
    number = int(input("Enter a number: "))

    if number <= 0:
        print("Error: Number must be greater than 0.")
        return

    single_table(number)

    # Part B
    n = int(input("\nEnter a number for tables from 1 to N: "))

    if n <= 0:
        print("Error: Number must be greater than 0.")
        return

    all_tables(n)


main()