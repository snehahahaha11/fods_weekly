#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2000 (both included). 

#declaring value of a and b
a = 1500
b = 2000

#Displaying so that user could understand
print("The number divisible by 7 but are not a multiple of 5 are ")  

#for loop 
#checking all numbers from 2000-3200 
for i in range(2000,3201 + 1):     
#checking the divisible of 7 and multiple of 5
    if i%7 == 0 and i%5==0:  
        print(i) #printing all the outputs
        