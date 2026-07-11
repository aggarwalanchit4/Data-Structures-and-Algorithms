# -----------------------------------------
# Practice 1 - sum of all elements
# -----------------------------------------

numbers = list(map(int, input("Enter numbers: ").split())) 
total = 0
for num in numbers :
    total = total + num 

print(f"sum of the elements in list is :{total}")

# -----------------------------------------
# Practice 2 - Average of Array Elements
# -----------------------------------------

numbers = list(map(int, input("Enter numbers: ").split())) 
total = 0
for num in numbers :
    total = total + num 

avg = total / len(numbers)
print(f"average of the elements in list is :{avg}")
