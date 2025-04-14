#Write a program to find the Euclidean distance between two coordinates take both the coordinates from the user as input.

#Taking both the coordinates as input
print("Finding the distance between two coordinates: \n")
x1 = int(input("First coordinate of the first point: "))
y1 = int(input("\n Second coordinate of the first point: "))
x2 = int(input("\n First coordinate of the second point: "))
y2 = int(input("\n Second coordinate of the second point: "))

#importing math to find square root
import math

#program to calculate the Euclidean distance
a =(x2-x1)**2
b=(y2-y1)**2
result = a+b
Euclidean_distance = (math.sqrt(result)) #using math.sqrt from the above import maths

#displaying the Euclidean distance in correct format
print("The Euclidean distance between two coordinates a(",x1,",",y1,") and b(",x2,",",y2,") is ",Euclidean_distance)