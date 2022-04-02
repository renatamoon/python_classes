# LIST COMPREHENSION

numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

# the standard way by using for:
for number in numbers:
    doubled_numbers.append(number * 2)

print("OUTPUT: ", doubled_numbers) # OUTPUT:  [0, 2, 4, 6, 8]

# -------------------- using list comprehension

doubled_nums = [number * 2 for number in numbers]
print("OUTPUT 2: ", doubled_nums) # OUTPUT 2:  [0, 2, 4, 6, 8]

# ------------------- using ranges

double_nums = [number * 2 for number in range(5)]
print(double_nums) # [0, 2, 4, 6, 8]

# ------------------- another way

friends_age = [22, 32, 25, 44]

age_strings = [f"My friend is (age) years old." for age in friends_age]
print(age_strings)

# ----------------- another way

names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print("OUTPUT: ", lower) # OUTPUT:  ['rolf', 'bob', 'jen']

# ------------ using if statements

friends = ["Rolf", "Bob", "Jen"]
friend = input("Enter your friend name: ").capitalize()


if friend in friends:
    print(f'{friend} is one of your friends')
else:
    print("Not one of your friends!")