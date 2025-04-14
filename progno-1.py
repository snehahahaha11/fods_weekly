#Write a program to take a number input from the user and display whether the number is even or odd.

#giving input
print("\n Enter a number to find if it is odd or even? \n")
num = int(input("Enter any number: ")) #taking input and storing in 'num'

#checking if the number is odd or even
if(num%2==0): #to determine if the number is even number
    print("\n The number", num, "is even number") 
else: #if it not even number the program will display it as odd through else condition
    print("\n The number", num, " is odd number")
