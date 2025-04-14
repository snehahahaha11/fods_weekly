import numpy as np

'''
Description of program:
This program creates a NumPy array (vector) of size 10 filled with zeros.
Then it sets the fifth element (index 4) to 1.
The program demonstrates basic NumPy array creation and element manipulation.
'''

def create_special_vector():
    """
    Creates a zero vector of size 10 with the fifth value (index 4) set to 1
    
    Returns:
        A numpy array of size 10 with zeros and a 1 at index 4
    """
    # Create a vector of zeros
    vector = np.zeros(10)
    
    # Set the fifth value (index 4) to 1
    vector[4] = 1
    
    return vector

# Test the function
result = create_special_vector()
print(result)