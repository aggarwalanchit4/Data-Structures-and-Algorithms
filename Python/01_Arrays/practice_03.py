# -----------------------------------------
# Practice 1 - Count Even and Odd Numbers
# -----------------------------------------

numbers = list(map(int, input("enter numbers: ").split()))
count_even = 0
count_odd = 0
for num in numbers :
    if num % 2 == 0:
        count_even += 1
    else :
        count_odd +=1

print(f"count of even numbers is : {count_even}")
print(f"count of odd numbers is : {count_odd}")

# -----------------------------------------
# Practice 2 - Count Positive and Negative Numbers
# -----------------------------------------

numbers = list(map(int, input("enter numbers: ").split()))
count_positive = 0
count_negative = 0
zeros = 0
for num in numbers :
    if num > 0:
        count_positive += 1
    elif num < 0 :
        count_negative +=1
    else :
        zeros += 1

print(f"count of positive numbers is : {count_positive}")
print(f"count of negative numbers is : {count_negative}")
print(f"count of zeros is :{zeros}")

# -----------------------------------------
# Practice 3 – Linear Search
# -----------------------------------------

numbers = list(map(int, input("enter numbers: ").split()))
search_num = int(input("enter number to search: "))
found = False
for num in numbers:
    if search_num == num :
        found = True
        break
if found :
    print("element found")
else :
    print("not found") 

# -----------------------------------------
# Practice 4 – Linear Search with index
# -----------------------------------------

numbers = list(map(int, input("enter numbers: ").split()))
search_num = int(input("enter number to search: "))
found = False
for i in range(len(numbers)):
    if search_num == numbers[i] :
        found = True
        break
if found :
    print(f"element found at index {i}")
else :
    print("not found") 
