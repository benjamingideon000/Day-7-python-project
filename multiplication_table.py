# multiplication_table.py

def multiplication_table():
    # Ask the user for input
    num = int(input("Enter a number: "))

    # Print the multiplication table
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

    # Bonus: Print tables for numbers 1-5
    print("\nMultiplication tables for numbers 1-5:")
    for j in range(1, 6):
        print(f"Multiplication table for {j}:")
        for i in range(1, 11):
            print(f"{j} x {i} = {j * i}")
        print()

if __name__ == "__main__":
    multiplication_table()

