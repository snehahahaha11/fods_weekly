#WAP that prompts the user for two integer values and displays the results of the first number divided by the second, with exactly two decimal places displayed. 

#Prompt the user for 2 integer values
print("\n Enter any 2 numbers for their division: ")
#taking 1st number input
num1 = int(input("\n First Number : ")) 
#taking 2nd number input
num2 = int(input("\n Second Number : ")) 

#calculate division
div = num1/num2

#print the result of the user input with two decimal places displayed.
print(f"The result of {num1} divided by {num2} is {div:.2f}")