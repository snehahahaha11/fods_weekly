import numpy as np

'''
Description of program:
This program creates a 3x4 matrix that resembles an identity matrix.
While a true identity matrix must be square, this program creates a rectangular
matrix with 1s on the main diagonal (where row index equals column index)
and 0s elsewhere. This demonstrates matrix creation and manipulation in NumPy.
'''

def create_identity_matrix():
    """
    Creates an identity matrix of shape (3,4)
    
    Returns:
        A numpy array representing a 3x4 identity-like matrix
    """
    # Note: A true identity matrix must be square, but we can create a 3x4 matrix
    # that has 1s on the main diagonal and 0s elsewhere
    
    # Create a 3x4 matrix of zeros
    matrix = np.zeros((3, 4))
    
    # Set 1s on the main diagonal where possible
    for i in range(min(3, 4)):
        matrix[i, i] = 1
    
    return matrix

# Test the function
result = create_identity_matrix()
print(result)