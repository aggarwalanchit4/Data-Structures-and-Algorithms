# -----------------------------------------
# Practice 1 - Access Array Elements
# -----------------------------------------

numbers = [10 , 20 , 30 , 40]
print("first element: ",numbers[0])
print("Last Element  :", numbers[-1])
print("Length        :", len(numbers))

# -----------------------------------------
# Practice 2 - Traverse an Array
# -----------------------------------------

numbers = [10 , 20 , 30 , 40 , 50]
for i in range(len(numbers)):
    print(numbers[i])

# -----------------------------------------
# Practice 3 – Update Array Elements
# -----------------------------------------

numbers = [10 , 20 , 30 , 40 , 50]
numbers[2] = 300
print(numbers)

# -----------------------------------------
# Challenge 1 - Find Largest Element
# -----------------------------------------

numbers = [12, 45, 7, 89, 23]
max_num = numbers[0] 
for i in range(len(numbers)) :
    if numbers[i] > max_num :
        max_num = numbers[i]

print(f"maximum number is : {max_num}")

# -----------------------------------------
# Challenge 2 - Find smallest Element
# -----------------------------------------

numbers = list(map(int, input("enter numbers in list: ").split()))
min_num = numbers[0]
for num in numbers :
    if num < min_num :
       min_num = num 
       
print(f"smallest number in the list is {min_num}")

# -----------------------------------------
# Challenge 3 - Find smallest and largest  Element in one loop
# -----------------------------------------

numbers = list(map(int, input("enter numbers in list: ").split()))
min_num = numbers[0]
max_num = numbers[0]
for num in numbers :
    if num < min_num :
       min_num = num 
    if num > max_num :
        max_num = num 

print(f"minimum number in the list is {min_num}")
print(f"maximum number in the list is : {max_num}")


       
       