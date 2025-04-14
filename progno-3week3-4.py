#Write a function to check whether the given number is Armstrong or not

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of number of digits
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == n

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    #displaying the result
    if is_armstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")
