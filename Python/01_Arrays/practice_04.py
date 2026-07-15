# -----------------------------------------
# Practice 1 – Reverse an Array
# -----------------------------------------

numbers = list(map(int,input("enter numbers: ").split()))
reverse_numbers = []
for i in range(len(numbers)-1,-1,-1):
    reverse_numbers.append(numbers[i])

print(reverse_numbers)

# -----------------------------------------
# Practice 2 – Copy an Array
# -----------------------------------------

numbers = list(map(int,input("enter numbers: ").split()))
numbers_copy =[]
for num in numbers:
    
    numbers_copy.append(num)

print(numbers_copy)

# -----------------------------------------
# Practice 3 – Merge Two Arrays
# -----------------------------------------
numbers = list(map(int,input("enter numbers: ").split()))
numbers_2nd = list(map(int,input("enter numbers: ").split()))
merged = []
for num in numbers :
    merged.append(num)
for num in numbers_2nd :
    merged.append(num)
print(merged)