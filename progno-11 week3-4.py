#Create three dictionaries: [7]
#dic1 = {1:10, 2:20}
#dic2 = {3:30, 4:40}
#dic3 = {5:50, 6:60}
#(a) Write code to concatenate these dictionaries to create a new one. 
#Create a variable called nums to store the resulting dictionary. 
#(b) Write code to add a new key/value pair to the dictionary nums: (7, 70)
#(c) Write code to update the value of the item with key 3 in nums to 80
#(d) Write code to remove the third item from dictionary nums.
#(e) Write code to sum all the items in the dictionary nums
#(f) Write code to multiply all the items in the dictionary nums
#(g) Write code to retrieve the maximum and minimum values in nums.

if __name__ == "__main__":
    # (a) Concatenate the dictionaries
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    nums = {**dic1, **dic2, **dic3}
    print("Initial concatenated dictionary (nums):", nums)

    # (b) Add a new key/value pair (7, 70)
    nums[7] = 70
    print("After adding (7, 70):", nums)

    # (c) Update the value of key 3 to 80
    if 3 in nums:
        nums[3] = 80
    print("After updating key 3 to 80:", nums)

    # (d) Remove the third item (by insertion order)
    # In Python 3.7+ dictionaries preserve insertion order.
    key_to_remove = list(nums.keys())[2]  # third item has index 2
    removed_value = nums.pop(key_to_remove)
    print(f"After removing the third item (key {key_to_remove}: {removed_value}):", nums)

    # (e) Sum all the values in nums
    total_sum = sum(nums.values())
    print("Sum of all values in nums:", total_sum)

    # (f) Multiply all the values in nums
    product = 1
    for value in nums.values():
        product *= value
    print("Product of all values in nums:", product)

    # (g) Retrieve the maximum and minimum values in nums
    max_value = max(nums.values())
    min_value = min(nums.values())
    print("Maximum value in nums:", max_value)
    print("Minimum value in nums:", min_value)
