"""
num_of_subjects = int(input("Enter the number of subjects: "))
marks_list = []
for i in range(num_of_subjects):
    marks = int(input(f"Enter the marks {i + 1}:"))
    marks_list.append(marks)

marks_tuple = tuple(marks_list)
sum = 0
for marks in marks_tuple:
    sum += marks
print(marks_list)
print(f"The total number of marks is: {sum}")
"""

""""
num = input("Enter the numbers with space: ")
num_tuple = tuple(int(x) for x in num.split())

small_count = 0
medium_count = 0
large_count = 0

for i in num_tuple:
    if i<=10:
        print(i, "Small")
        small_count += 1
    elif i<=99:
        print(i, "Medium")
        medium_count += 1
    else:
        print(i, "Large")
        large_count += 1

print(num_tuple)
print("Small count:", small_count)
print("Medium count:", medium_count)
print("Large count:", large_count)
"""

new = input("Enter the numbers with space: ")
num_tuple = tuple(int(x) for x in new.split())

new_tuple = ()

for i in num_tuple:
    new_tuple += (i * i,)

print(new_tuple)












