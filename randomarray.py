import numpy as np

'''
Description of program:
This program takes two inputs from the user: number of rows (a) and number of columns (b).
It then creates a random NumPy array of shape (a, b) with values between 0 and 1.
The program calculates and displays the average value of all elements in the array.
This demonstrates user input, random array generation, and basic array statistics in NumPy.
'''

def generate_random_array():
    """
    Generates a random array with shape specified by the user and calculates its average
    
    Returns:
        A random numpy array and its average value
    """
    # Get user input for array dimensions
    a = int(input("Enter number of rows: "))
    b = int(input("Enter number of columns: "))
    
    # Generate random array of shape (a, b)
    random_array = np.random.rand(a, b)
    
    # Calculate average of the array
    array_avg = np.mean(random_array)
    
    return random_array, array_avg

# Test the function
array, avg = generate_random_array()
print("Generated array:")
print(array)
print("\nAverage of the array:", avg)