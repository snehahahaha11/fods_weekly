#Write a function to check whether the given number is prime or not.

def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # Check for factors from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
