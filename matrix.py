import numpy as np

'''
Description of program:
This program creates a 5x5 matrix where each row contains the values [0, 1, 2, 3, 4].
The program demonstrates how to create and manipulate arrays to form specific matrix patterns.
It uses NumPy's arange and tile functions to efficiently generate the structured matrix.
'''

def create_row_matrix():
    """
    Creates a 5x5 matrix with row values ranging from 0 to 4
    
    Returns:
        A 5x5 numpy array where each row contains values from 0 to 4
    """
    # Create a row vector [0, 1, 2, 3, 4]
    row = np.arange(5)
    
    # Repeat the row 5 times to create a 5x5 matrix
    matrix = np.tile(row, (5, 1))
    
    return matrix

# Test the function
result = create_row_matrix()
print(result)