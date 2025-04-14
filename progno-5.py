#Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user.

#Taking user input for principle, interest, time period
print("Calculating simple interest\n")
P = int(input("Value of Principle: "))
T = int(input("\n Time Period: "))
R = int(input("\n Rate of Interest: "))

#Calculating simple interest
Simple_Interest= (P*T*R)/100

#Displaying Output
print("The simple interest is ",Simple_Interest)