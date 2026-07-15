# -----------------------------------------
# Practice 1 – Check if an Array is Sorted
# -----------------------------------------

numbers = list(map(int, input("enter elements in array : ").split()))
is_sorted = True
for i in range(len(numbers) - 1) :
    if numbers[i] > numbers[i+1] :
        is_sorted = False
        break

if is_sorted :
    print("sorted")
else:
    print("not sorted")

# -----------------------------------------
# Practice 2 – Second Largest Element
# -----------------------------------------


numbers = list(map(int, input("enter elements in array : ").split()))
greatest = numbers[0]
second_greatest = numbers[0]

for num in numbers:

    if num > greatest:
        second_greatest = greatest
        greatest = num
    elif num > second_greatest and num != greatest:
        second_greatest = num

print(second_greatest)

# -----------------------------------------
# Practice 3 – Largest and Second Largest Element
# -----------------------------------------

numbers = list(map(int, input("enter elements in array : ").split()))
greatest = numbers[0]
second_greatest = numbers[0]

for num in numbers:

    if num > greatest:
        second_greatest = greatest
        greatest = num
    elif num > second_greatest and num != greatest:
        second_greatest = num

print(f"Largest = {greatest}")
print(f"Second Largest = {second_greatest}")