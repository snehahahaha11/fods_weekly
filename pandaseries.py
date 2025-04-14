import pandas as pd

'''
Description of program:
This program creates two Pandas Series objects with the same index values.
It then performs four basic arithmetic operations on these Series:
addition, subtraction, multiplication, and division.
The program demonstrates Pandas Series creation and element-wise operations
between Series objects. It shows how Pandas aligns data by index values
when performing operations.
'''

def pandas_series_operations():
    """
    Performs addition, subtraction, multiplication, and division on two Pandas Series
    
    Returns:
        The two Series and the results of operations
    """
    # Create two pandas Series
    series1 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    series2 = pd.Series([5, 10, 15, 20, 25], index=['a', 'b', 'c', 'd', 'e'])
    
    # Perform operations
    addition = series1 + series2
    subtraction = series1 - series2
    multiplication = series1 * series2
    division = series1 / series2
    
    return series1, series2, addition, subtraction, multiplication, division

# Test the function
s1, s2, add, sub, mul, div = pandas_series_operations()
print("Series 1:")
print(s1)
print("\nSeries 2:")
print(s2)
print("\nAddition:")
print(add)
print("\nSubtraction:")
print(sub)
print("\nMultiplication:")
print(mul)
print("\nDivision:")
print(div)