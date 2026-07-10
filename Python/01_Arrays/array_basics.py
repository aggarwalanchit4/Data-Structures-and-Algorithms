# -----------------------------------------
# DSA Day 1 - Arrays Basics
# -----------------------------------------

# Creating an array
numbers = [10, 20, 30, 40, 50]

# Printing the entire array
print("Array:", numbers)

# Accessing elements
print("First Element :", numbers[0])
print("Third Element :", numbers[2])
print("Last Element  :", numbers[-1])

# Length of array
print("Length of Array:", len(numbers))

# Updating an element
numbers[1] = 100

print("Updated Array:", numbers)

# Traversing an array
print("\nTraversing the Array:")

for i in range(len(numbers)):
    print(numbers[i])