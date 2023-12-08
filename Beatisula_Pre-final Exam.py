print("CS112: Computer Programming 1 - Pre-Finals Output")
print("Created by: Nathaniel Rosell Beatisula")
print()

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    if primes:
        print(f"Prime numbers between {start} and {end} :", end=" ")
        print(" ".join(map(str, primes)))
        print()
    else:
        print(f"There are no prime numbers between {start} and {end}.")
        print()

while True:
    start = int(input("Enter the starting number (enter 0 to terminate): "))
    if start == 0:
        print("Program terminated.")
        print()
        break
    if start < 0:
        print("Enter a non-negative number for the starting range.")
        print()
        continue

    end = int(input("Enter the ending number: "))
    if end < start:
        print("Enter a number greater than the starting number.")
        print()
        continue

    display_primes(start, end)